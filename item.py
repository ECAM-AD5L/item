import os
from pymongo import MongoClient
import json
from flask import request

client = MongoClient('mongodb://admin:password1@ds117334.mlab.com:17334/item')
db = client.item
collection = db.items
print(collection)


def get():
    not_f = "Not Found"
    search = collection.find()
    dico = {}

    i=0
    for s in search:
        print(s)
        dico[i] = json.dumps(str(s))
        i+=1

    return (dico)

def get_i(id):
    search = collection.find_one({'id':id})
    print("-----------------")
    print(search)
    dico = {}

    if search != None:
        return json.dumps(str(search))
    else:
        return "Not deleted"

def delete(id):
    search = collection.find_one({'id':id})
    print("-----------------")
    print(search)
    dico = {}

    if search != None:
        collection.remove(search)
        return "deleted"
    else:
        return "Not deleted"


def insert():
    r = request.form
    id = r["id"]
    name = r["name"]
    price = r["price"]
    color = r["color"]
    model = r["model"]
    if (id=="") or (name=="") or (price=="") or (color=="") or (model==""):
        return "Not inserted"
    else:
        item={
            "id": id,
            "name": name,
            "price": price,
            "description": {
                "color": color,
                "model": model
            }
        }

        rec = collection.insert_one(item)
        if rec != None:
            return "Inserted"
        else:
            return "Not inserted"
        # print("Done", rec)


def insert_():
        #item example for test
        item = {
            "id":"2",
            "name": "Samsung S9",
            "price": "800€",
            "description": {
                "color": "black",
                "model": "64GB"
            }
        }

        rec = collection.insert_one(item)
        print("Done", rec)


if __name__ == '__main__':
    insert_()






















#
# class Item():
#     def __init__(self, id, nom, prix, commentaire, description):
#         self.id = id
#         self.nom = nom
#         self.prix = prix
#         self.commentaire = commentaire
#         self.description = description
#
#     def get_nom(self):
#         return self.nom
#
#     def get_prix(self):
#         return self.prix
#
#     def get_id(self):
#         return self.id
#
#     def get_commentaire(self):
#         return self.commentaire
#
#     def get_description(self):
#         return self.description
#
#     def GET(self, name):
#         pass
#
#     def POST(self):
#         pass
#
#     def PUT(self):
#         pass
#
#     def DELETE(self):
#         pass
#
#
# class Commentaire():
#     def __init__(self, note, texte):
#         self.note = note
#         self.texte = texte
#
#     def get_note(self):
#         return self.note
#
#     def get_texte(self):
#         return self.texte
#
#
# class Description():
#     def __init__(self, couleur, modele):
#         self.couleur = couleur
#         self.modele = modele
#
#     def get_couleur(self):
#         return self.couleur
#
#     def get_modele(self):
#         return self.modele