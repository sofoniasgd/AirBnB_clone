#!/usr/bin/python3
"""File Serialization/Desialization."""


import json
from json.decoder import JSONDecodeError
import os


class FileStorage():
    """Serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        __file_path (str): - path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id
            ex: to store a BaseModel object with id=12121212,
            the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # get class name of obj and append key
        key = str(obj.__class__.__name__)
        key += "." + obj.id
        # print("|||key is=>{}|||".format(key))
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        path: __file_path
        """
        # check if file name attribute exists
        # if not FileStorage.__file_path:
        #   return

        # serialize __objects to file
        # with open(FileStorage.__file_path, 'w') as jfile:
        #  json.dump(FileStorage.__objects, jfile)
        obj_dict = FileStorage.__objects
        json_dict = {}
        for key, value in obj_dict.items():
            json_dict[key] = value.to_dict()

        try:
            jfile = open(FileStorage.__file_path, mode='w', encoding='utf-8')
        except OSError:
            return
        else:
            json.dump(json_dict, jfile)
            jfile.close()

    def reload(self):
        """deserializes the JSON file to __objects
        Deserialize only if the JSON file at (__file_path) exists
        else, do nothing
        if file doesnt exist no exception should be raised
        """
        from models.base_model import BaseModel
        from models.user import User
        # check if file name attribute exists
        if not FileStorage.__file_path:
            return
        # open file and load to dictionary
        path = FileStorage.__file_path
        try:
            try:
                jfile = open(path, mode='r', encoding='utf-8')
            except FileNotFoundError:
                return
            json_dict = json.load(jfile)
        except JSONDecodeError:
            jfile.close()
        # deserialize =class'str'>>class'BaseModel' into class'BaseModel'
        for key, value in json_dict.items():
            obj = value
            o_type = ""
            # get object type from __class__ attribute
            for att_type, att_name in obj.items():
                if att_type == '__class__':
                    o_type = att_name
                    obj.pop("__class__")
                    break
            # create object creatrion expression and use eval()
            code = o_type + '(**obj)'
            FileStorage.__objects[key] = eval(code)
