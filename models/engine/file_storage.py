#!/usr/bin/python3
"""model de storage"""


from models.base_model import BaseModel
import json
import os
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class pour file storage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects with key"""
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON"""
        jdict = {}
        for keys, values in FileStorage.__objects.items():
            jdict[keys] = values.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(jdict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                FileStorage.__objects[keys] = eval(val['__class__'])(**val)
