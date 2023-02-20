#!/usr/bin/python3
"""Creation de la class ModelBase qui va définir 
les attributs et les methodes"""


import uuid
from datetime import datetime

class BaseModel:

    """On va etuliser args et kwargs pour
        la création d'une base d'un model"""
    def __init__(self, *args, **kwargs):
            """Dans la méthode __init__(), on vérifie si l'argument kwargs est présent, ce qui
              indique que l'objet doit être créé à partir d'un dictionnaire. Si kwargs n'est pas vide, 
              on parcour chaque paire clé-valeur dans le dictionnaire. Si la clé est created_at 
              ou updated_at, on converti la valeur de la chaîne de caractères en objet datetime. 
              Ensuite, vous utilisez la méthode setattr() pour définir l'attribut de l'objet correspondant 
              à la clé avec la valeur."""
            if kwargs:
                 for key, value in kwargs.items():
                      if key == 'created_at' or key == 'updated_at':
                           """convertie l'objet en datatime"""
                           value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                      if key != '__class__':
                           setattr(self, key, value)
            if not kwargs:
                
                """id permettra d'avoir un identifiant unique transformer en str a chaque
                instancation de class BaseModel"""
                self.id = str(uuid.uuid4())

                """attribuer la date et l'heure a la création de instance class BaseModel"""
                self.created_at = datetime.now()

                """Permet d'attribut la date et l'heure quand une instance et mofifier"""
                self.updated_at = self.created_at
        
    def __str__(self):
        """Methode special qui return la chaine suivante"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        """A chaque fois qu'il y aura une modification, l'attribut sera mise à jour"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """On va return un dictionner avec les noms (clées) et les valeur des attributs"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
