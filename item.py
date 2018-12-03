from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

class Item():
    def __init__(self, id, nom, prix, commentaire, description):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.commentaire = commentaire
        self.description = description

    def get_nom(self):
        return self.nom

    def get_prix(self):
        return self.prix

    def get_id(self):
        return self.id

    def get_commentaire(self):
        return self.commentaire

    def get_description(self):
        return self.description

    def GET(self, name):
        pass

    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass


class Commentaire():
    def __init__(self, note, texte):
        self.note = note
        self.texte = texte

    def get_note(self):
        return self.note

    def get_texte(self):
        return self.texte


class Description():
    def __init__(self, couleur, modele):
        self.couleur = couleur
        self.modele = modele

    def get_couleur(self):
        return self.couleur

    def get_modele(self):
        return self.modele