#!/usr/bin/env python3
#=================================================================
# Interface ODOO avec l'API XML-RPC
#-----------------------------------------------------------------
# https://www.odoo.com/documentation/15.0/developer/misc/api/odoo.html
# Accéder à l'interface Web Odoo en mode debug => localhost:8069/web?debug=1
#=================================================================
import xmlrpc.client

class IF_ErpOdoo:
    """Classe objet d'interface de l'ERP Odoo en XML-RPC"""
    
    def __init__(self, erp_ipaddr, erp_port, erp_db, erp_user, erp_pwd):
        """Constructeur de la classe"""
        self.mErpIpAddr = erp_ipaddr
        self.mErpIpPort = erp_port
        self.mErpDB = erp_db
        self.mErpUser = erp_user
        self.mErpPwd = erp_pwd
        self.mUserId = 0
        self.mModels = None

    def connect(self):
        """Methode de connexion à l'ERP Odoo"""
        erp_url = f'http://{self.mErpIpAddr}:{self.mErpIpPort}'
        print("Connexion ODOO")
        print(f"@URL={erp_url}")

        try:
            common = xmlrpc.client.ServerProxy(f'{erp_url}/xmlrpc/2/common')
            version = common.version()
            print(f"Odoo version: {version['server_version']}")
        except ConnectionRefusedError:
            print("Odoo Server not found or connection rejected")
            return False

        self.mUserId = common.authenticate(self.mErpDB, self.mErpUser, self.mErpPwd, {})
        if self.mUserId:
            print(f"Odoo authentication successful: {self.mUserId}")
            self.mModels = xmlrpc.client.ServerProxy(f'{erp_url}/xmlrpc/2/object')
            return True
        else:
            print(f'Odoo Server authentication rejected: DB={self.mErpDB}, User={self.mErpUser}')
            return False

    def getFields(self):
        """Récupération des champs de la production MRP"""
        if not self.mUserId or not self.mModels:
            print("Not authenticated. Please connect first.")
            return

        listing = self.mModels.execute_kw(self.mErpDB, self.mUserId, self.mErpPwd,
                                          'mrp.production', 'fields_get',
                                          [], {'attributes': []})
        for attr in listing:
            print(f' - {attr}')

    def getManufOrderToDo(self):
        """Récupération des ordres de fabrication à traiter"""
        if not self.mUserId or not self.mModels:
            print("Not authenticated. Please connect first.")
            return

        fields = ['name', 'date_planned_start', 'product_id', 'product_qty', 'qty_producing', 'state']
        limit = 10
        mo_list = self.mModels.execute_kw(self.mErpDB, self.mUserId, self.mErpPwd,
                                          'mrp.production', 'search_read',
                                          [[('state', '=', 'confirmed'), ('qty_produced', '!=', 'product_qty')]],
                                          {'fields': fields, 'limit': limit})
        for mo_dico in mo_list:
            print('----------------------------')
            for k in mo_dico.keys():
                print(f' - {k} : {mo_dico[k]}')

    def checkAccessRights(self):
        """Vérification des droits d'accès à l'écriture sur les ordres de fabrication"""
        if not self.mUserId or not self.mModels:
            print("Not authenticated. Please connect first.")
            return

        access = self.mModels.execute_kw(self.mErpDB, self.mUserId, self.mErpPwd,
                                         'mrp.production', 'check_access_rights',
                                         ['write'], {'raise_exception': False})
        print(f"Manufacturing Order write access rights: {access}")

#=================================================================
if __name__ == "__main__":
    # Création de l'objet Odoo et connexion
    ifOdoo = IF_ErpOdoo("192.168.0.17", "8069", "vitre", "inter", "inter")
    
    if ifOdoo.connect():
        ifOdoo.getFields()
        ifOdoo.checkAccessRights()
        ifOdoo.getManufOrderToDo()
    else:
        print("Connection to Odoo server failed.")
