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
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # get class name of obj and append key
        key = str(obj.__class__.__name__)
        key += "." + obj.id
        # print("|||key is=>{}|||".format(key))
        json_of_obj = obj.to_dict()
        FileStorage.__objects[key] = json_of_obj
        for key, value in FileStorage.__objects.items():
            print("<<key={}>>".format(key))
            for key2, value2 in value.items():
                print("|dict key={}|type={}|value={}|".format(key2, type(value2), value2))
        ###

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
        try:
            jfile = open(FileStorage.__file_path, mode='w', encoding='utf-8')
        except OSError:
            return
        else:
            json.dump(FileStorage.__objects, jfile)
            jfile.close()

    def reload(self):
        """deserializes the JSON file to __objects
        Deserialize only if the JSON file at (__file_path) exists
        else, do nothing
        if file doesnt exist no exception should be raised
        """
        # check if file name attribute exists
        if not FileStorage.__file_path:
            return
        # check if file exists
        # filexists = os.path.isfile(FileStorage.__file_path)
        # if not filexists:
        #   return
        # with open(FileStorage.__file_path, 'r') as jfile:
        #   FileStorage.__objects = json.load(jfile)
        
        try:
            try:
                jfile = open(FileStorage.__file_path, mode='r', encoding='utf-8')
            except FileNotFoundError:
                return
            FileStorage.__objects = json.load(jfile)
        except JSONDecodeError:
            jfile.close()
