#!/usr/bin/python3
"""Creation de la class ModelBase qui va définir 
les attributs et les methodes"""


import uuid
from datetime import datetime
import json


class BaseModel:
    def __init__(self):
        """id permettra d'avoir un identifiant unique transformer en str a chaque
        instancation de class BaseModel"""
        self.id = str(uuid.uuid4())

        """attribuer la date et l'heure a la création de instance class BaseModel"""
        self.created_at = datetime.now()

        """Permet d'attribut la date et l'heure quand une instance"""
        self.updated_at = datetime.now()
        
    def __str__(self):
        """Methode special qui return la chaine suivante"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        
    def to_dict(self):
        """On va return un dictionner avec les noms (clées) et les valeur d'un attributs"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
    
    def save(self):
        self.updated_at = datetime.now()
        data = self.to_dict()
        filename = "{}.json".format(datetime.now().strftime("%Y%m%d%H%M%S%f"))
        with open(filename, 'w') as f:
            json.dump(data, f)
