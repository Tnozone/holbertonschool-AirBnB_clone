#!/usr/bin/python3
"""Base model"""


import json
import os


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        if obj:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to JSON"""
        jdict = {}
        for keys, values in FileStorage.__objetcs.items():
            jdict[keys] = values.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(jdict, file)

    def reload(self):
        """deserializes the JSON file"""
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                FileStorage.__objects[keys] = eval(val['__class__'])(**val)
