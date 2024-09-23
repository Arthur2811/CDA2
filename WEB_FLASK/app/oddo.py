#!/usr/bin/env python3
"""
Interface Odoo avec l'API XML-RPC
https://www.odoo.com/documentation/15.0/developer/misc/api/odoo.html

Accéder à l'interface Web Odoo en mode debug => localhost:8069/web?debug
"""

import xmlrpc.client

class IFOdoo:
    """Classe objet d'interface de l'ERP Odoo en XML-RPC"""

    def __init__(self, erp_ipaddr, erp_port, erp_user, erp_pwd):
        """Initialisation des paramètres de connexion"""
        self.erp_ipaddr = erp_ipaddr
        self.erp_port = erp_port
        self.erp_user = erp_user
        self.erp_pwd = erp_pwd
        self.connection = None

    def __del__(self):
        """Destruction de l'objet et déconnexion"""
        if self.connection:
            self.connection = None

    def connect(self):
        """Connexion à l'ERP Odoo via XML-RPC"""
        url = f"http://{self.erp_ipaddr}:{self.erp_port}/xmlrpc/2/common"
        self.connection = xmlrpc.client.ServerProxy(url)

    def getFields(self):
        """Méthode pour récupérer les champs"""
        # Implémentation à ajouter
        pass

    def getManufactureOrdersToDo(self):
        """Méthode pour récupérer les ordres de fabrication à faire"""
        # Implémentation à ajouter
        pass
