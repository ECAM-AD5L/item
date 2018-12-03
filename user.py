from flask import Flask
from flask_restful import Api, Resource, reqparse


class User():
    def __init__(self, id, nom, prenom, mdp, ddn, mail, adr_livraison, code_pos, ville, pays, tel, num_carte):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
        self.ddn = ddn
        self.mail = mail
        self.adr_livraison = adr_livraison
        self.code_pos = code_pos
        self.ville = ville
        self.pays = pays
        self.tel = tel
        self.num_carte = num_carte

    def get_id(self):
        return self.id

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_mdp(self):
        return self.mdp

    def get_ddn(self):
        return self.ddn

    def get_mail(self):
        return self.mail

    def get_adr_livraison(self):
        return self.adr_livraison

    def get_code_pos(self):
        return self.code_pos

    def get_ville(self):
        return self.ville

    def get_pays(self):
        return self.pays

    def get_tel(self):
        return self.tel

    def get_num_carte(self):
        return self.num_carte

    def GET(self, name):
        pass

    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass

