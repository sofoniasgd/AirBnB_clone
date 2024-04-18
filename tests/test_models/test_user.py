#!/usr/bin/python3
"""Defines Unit test module for user module
        i.e models/user.py
    test classesi:
    instantiation
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.user import User
from models import storage

class TestUser(unittest.TestCase):
    """Test class for user class"""

    def test_instantiation_kwargs(self):
        """test types of instance attributes in User
            when attribute dictionary(**kwargs) is passed
        """
        # create a dictionary of attributes
        create = datetime.now()
        create = datetime.isoformat(create)
        update = datetime.now()
        update = datetime.isoformat(update)
        test_dict = {'name': 'sofonias', 'age': 27}
        test_dict['created_at'] = create
        test_dict['updated_at'] = update
        test_dict['email'] = "sof@ss.ss"
        test_dict['password'] = "lamepass"
        test_dict['first_name'] = "soff"
        test_dict['last_name'] = "dubb"


        obj = User(**test_dict)
        self.assertEqual(obj.name, 'sofonias')
        self.assertEqual(obj.age, 27)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.email, "sof@ss.ss")
        self.assertEqual(obj.password, "lamepass")
        self.assertEqual(obj.first_name, "soff")
        self.assertEqual(obj.last_name, "dubb")

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

