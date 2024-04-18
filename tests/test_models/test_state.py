#!/usr/bin/python3
"""Defines Unit test module for state module
        i.e models/state.py
    test classes:
        TestState
        Teststr
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.state import State
from models import storage

class TestState(unittest.TestCase):
    """Test class for state class"""

    def test_name(self):
        """ test class attribute name"""

        obj = State()
        self.assertEqual(obj.name, "")
        name = "lame"
        obj.name = name
        self.assertEqual(obj.name, name)

    def test_instantiation_kwargs(self):
        """test types of instance attributes in State
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
        test_dict['name'] = "dubb"


        obj = State(**test_dict)
        self.assertEqual(obj.age, 27)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.name, "dubb")

class TestStr(unittest.TestCase):
    """test class for __str__
     __str__: should print:
    [<class name>] (<self.id>) <self.__dict__>
    """

    def test_str(self):
        """test the __str__ method"""
        obj = State()
        string = str(obj)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)

