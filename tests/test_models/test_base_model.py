#!/usr/bin/python3
"""Defines Unit test module for base_model module
        i.e models/base_model.py
    test classes:
    instantiation
    save
    to_dict
"""

import unittest
import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel class"""

    def test_instantiation_types(self):
        """check types of instance attributes in BaseModel
            attributes to check:
                id (str)
                created_at (datetime)
                updated_at (datetime)
        """
        # setting up objects.
        controlobject = BaseModel()
        object1 = BaseModel()
        # test types and id uniqueness
        self.assertNotEqual(controlobject.id, object1.id)
        self.assertIsInstance(controlobject.id, str)
        self.assertIsInstance(controlobject.created_at, datetime.datetime)
        self.assertIsInstance(controlobject.updated_at, datetime.datetime)


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


class Testsave(unittest.TestCase):
    """Test calss for save method"""

    def test_save(self):
        # setup object
        testobj = BaseModel()
        # test before save(create_at and update_at time should be same)
        timedelta = testobj.updated_at - testobj.created_at
        self.assertFalse(timedelta.seconds > 0)
        # delay 2 seconds then test after save using time difference
        time.sleep(2)
        testobj.save()
        timedelta2 = testobj.updated_at - testobj.created_at
        self.assertTrue(timedelta2.seconds > 0)


class Test_to_dict(unittest.TestCase):
    """Test class for to_dict method"""

    def test_correct_keys(self):
        """check if instance contains correct keys"""
        obj = BaseModel()
        dictionary = obj.to_dict()
        keys = dictionary.keys()
        self.assertIn('id', keys)
        self.assertIn('created_at', keys)
        self.assertIn('updated_at', keys)

    def test_added_attributes(self):
        """test for added instance attributes"""
        obj = BaseModel()
        # setup new instance attributes and test to_dict()
        obj.fname = "sofonias"
        obj.mname = "dubale"
        obj.lname = "gashaw"
        dictionary = obj.to_dict()
        keys = dictionary.keys()
        self.assertIn('fname', keys)
        self.assertIn('mname', keys)
        self.assertIn('lname', keys)
