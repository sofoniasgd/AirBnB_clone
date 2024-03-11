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

    # setting up objects.
    controlobject = BaseModel()


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


class Testto_dict(unittest.TestCase):
    """Test class for to_dict method"""
    pass
