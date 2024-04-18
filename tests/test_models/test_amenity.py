#!/usr/bin/python3
"""Defines Unit test module for amenity module
        i.e models/amenity.py
    test classes:
        testAmenity
        teststr
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Test class for amenity class"""

    def test_name(self):
        """ test class attribute name"""

        obj = Amenity()
        self.assertEqual(obj.name, "")
        lname = "lame"
        obj.name = lname
        self.assertEqual(obj.name, lname)

    def test_instantiation_kwargs(self):
        """test types of instance attributes in Amenity
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
        test_dict['name'] = "dubb"


        obj = Amenity(**test_dict)
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
        obj = BaseModel()
        string = str(obj)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)

