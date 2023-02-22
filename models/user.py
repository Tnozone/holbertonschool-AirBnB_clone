#!/usr/bin/python3
"""Definir id du User"""


import email
from models.base_model import BaseModel
"""Cette classe User permet de définir un modèle de données pour représenter 
un utilisateur dans notre application. Elle hérite de la classe BaseModel, 
ce qui signifie qu'elle bénéficie de tous les attributs et méthodes de la classe mère."""


class User(BaseModel):
    """definir class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
