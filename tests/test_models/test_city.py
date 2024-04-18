#!/usr/bin/python3
"""Defines Unit test module for city module
        i.e models/city.py
    test classesi:
    instantiation
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Test class for city class"""

    def test_state_id(self):
        """ test class attribute state_id"""

        obj = City()
        self.assertEqual(obj.state_id, "")
        state = "addis ababa"
        obj.state_id = state
        self.assertEqual(obj.state_id, state)

    def test_name(self):
        """ test class attribute name"""

        obj = City()
        self.assertEqual(obj.name, "")
        name = "lame"
        obj.name = name
        self.assertEqual(obj.name, name)

    def test_instantiation_kwargs(self):
        """test types of instance attributes in City
            when attribute dictionary(**kwargs) is passed
        """
        # create a dictionary of attributes
        create = datetime.now()
        create = datetime.isoformat(create)
        update = datetime.now()
        update = datetime.isoformat(update)
        test_dict = {}
        test_dict['created_at'] = create
        test_dict['updated_at'] = update
        test_dict['state_id'] = "soff"
        test_dict['name'] = "dubb"

        obj = City(**test_dict)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.state_id, "soff")
        self.assertEqual(obj.name, "dubb")


class TestStr(unittest.TestCase):
    """test class for __str__
     __str__: should print:
    [<class name>] (<self.id>) <self.__dict__>
    """

    def test_str(self):
        """test the __str__ method"""
        obj = BaseModel()
        string = str(obj)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)
