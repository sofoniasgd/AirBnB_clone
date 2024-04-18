#!/usr/bin/python3
"""Defines Unit test module for review module
        i.e models/review.py
    test classesi:
    instantiation
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.review import Review
from models import storage

class TestReview(unittest.TestCase):
    """Test class for review class"""

    def test_place_id(self):
        """ test class attribute place_id"""

        obj = Review()
        self.assertEqual(obj.place_id, "")
        place_id = "add"
        obj.place_id = place_id
        self.assertEqual(obj.place_id, place_id)

    def test_user_id(self):
        """ test class attribute user_id"""

        obj = Review()
        self.assertEqual(obj.user_id, "")
        usr = "sof01"
        obj.user_id = usr
        self.assertEqual(obj.user_id, usr)

    def test_text(self):
        """ test class attribute text"""

        obj = Review()
        self.assertEqual(obj.text, "")
        text = "text"
        obj.text = text
        self.assertEqual(obj.text, text)

    def test_instantiation_kwargs(self):
        """test types of instance attributes in Review
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
        test_dict['place_id'] = "add01"
        test_dict['user_id'] = "usr01"
        test_dict['text'] = "goodreview"


        obj = Review(**test_dict)
        self.assertEqual(obj.name, 'sofonias')
        self.assertEqual(obj.age, 27)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.place_id, "add01")
        self.assertEqual(obj.user_id, "usr01")
        self.assertEqual(obj.text, "goodreview")

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

