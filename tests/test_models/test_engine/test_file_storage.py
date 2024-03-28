#!/usr/bin/python3
"""Defines Unit test module for file_storage module
        i.e models/engine/file_stroage.py
    test methods:
    all
    new
    save
    reload
"""

import unittest
from datetime import datetime
import time
import os
import json
import models
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage class"""

    file_path = "file.json"
    storage._FileStorage__objects.clear()

    def test_all(self):
        """test contents of __objects dictionary
            with and without objects
        """
        self.assertEqual(storage.all(), {})
        test_obj = BaseModel()
        obj_id = str("{}.{}".format(test_obj.__class__.__name__, test_obj.id))
        obj_dict = storage.all()
        key = next(iter(obj_dict))
        self.assertEqual(key, obj_id)

    def test_new(self):
        """check instance calls to FileStorage
            when new objects of BaseModel are created
        """
        # clear object dict, create objects
        storage._FileStorage__objects.clear()
        object_dict = {}
        for i in range(3):
            key = "obj{}".format(i)
            object_dict[key] = BaseModel()
        self.assertEqual(len(storage.all()), 3)

    try:
        os.remove(file_path)
    except:
        pass

    def test_save(self):
        """test save() method
        create objects, save and check file
        """
        file_path = "file.json"
        self.assertFalse(os.path.exists(file_path))
        storage.save()
        self.assertTrue(os.path.exists(file_path))
        # open file and check if its now empty
        with open(file_path, 'r') as jfile:
            jdict = json.load(jfile)
        self.assertNotEqual(jdict, {})

    def test_reload(self):
        """test relaod() method"""

        file_path = "file.json"
        if not os.path.exists(file_path):
            return
        # open file and check if its now empty
        with open(file_path, 'r') as jfile:
            j_dict = json.load(jfile)
        self.assertNotEqual(j_dict, {})
