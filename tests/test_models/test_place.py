#!/usr/bin/python3
"""Defines Unit test module for place module
        i.e models/place.py
    test classesi:
        TestPlace
        TestStr
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test class for place class"""

    def test_city_id(self):
        """ test class attribute city_id"""

        obj = Place()
        self.assertEqual(obj.city_id, "")
        city_id = "test@test.com"
        obj.city_id = city_id
        self.assertEqual(obj.city_id, city_id)

    def test_user_id(self):
        """ test class attribute user_id"""

        obj = Place()
        self.assertEqual(obj.user_id, "")
        psw = "p@55w0rd"
        obj.user_id = psw
        self.assertEqual(obj.user_id, psw)

    def test_name(self):
        """ test class attribute name"""

        obj = Place()
        self.assertEqual(obj.name, "")
        name = "name"
        obj.name = name
        self.assertEqual(obj.name, name)

    def test_description(self):
        """ test class attribute description"""

        obj = Place()
        self.assertEqual(obj.description, "")
        desc = "lame"
        obj.description = desc
        self.assertEqual(obj.description, desc)

    def test_number_rooms(self):
        """ test class attribute number_rooms"""

        obj = Place()
        self.assertEqual(obj.number_rooms, 0)
        rooms = 5
        obj.number_rooms = rooms
        self.assertEqual(obj.number_rooms, rooms)

    def test_number_bathrooms(self):
        """ test class attribute number_bathrooms"""

        obj = Place()
        self.assertEqual(obj.number_bathrooms, 0)
        brooms = 2
        obj.number_bathrooms = brooms
        self.assertEqual(obj.number_bathrooms, brooms)

    def test_max_guest(self):
        """ test class attribute max_guest"""

        obj = Place()
        self.assertEqual(obj.max_guest, 0)
        mxguest = 2
        obj.max_guest = mxguest
        self.assertEqual(obj.max_guest, mxguest)

    def test_price_by_night(self):
        """ test class attribute price_by_night"""

        obj = Place()
        self.assertEqual(obj.price_by_night, 0)
        price = 100
        obj.price_by_night = price
        self.assertEqual(obj.price_by_night, price)

    def test_latitude(self):
        """ test class attribute latitude"""

        obj = Place()
        self.assertEqual(obj.latitude, 0.0)
        lat = 9.047736
        obj.latitude = lat
        self.assertEqual(obj.latitude, lat)

    def test_longitude(self):
        """ test class attribute longitude"""

        obj = Place()
        self.assertEqual(obj.longitude, 0.0)
        longt = 38.707057
        obj.longitude = longt
        self.assertEqual(obj.longitude, longt)

    def test_amenity_ids(self):
        """ test class attribute amenity_ids"""

        obj = Place()
        self.assertEqual(obj.amenity_ids, [])
        amids = ["parking", "front porch", "jacuzzi"]
        obj.amenity_ids = amids
        self.assertEqual(obj.amenity_ids, amids)

    def test_instantiation_kwargs(self):
        """test types of instance attributes in Place
            when attribute dictionary(**kwargs) is passed
        """
        # create a dictionary of attributes
        create = datetime.now()
        create = datetime.isoformat(create)
        update = datetime.now()
        update = datetime.isoformat(update)
        test_dict = {'fname': 'sofonias', 'age': 27}
        test_dict['created_at'] = create
        test_dict['updated_at'] = update
        test_dict['city_id'] = "Addis ababa"
        test_dict['user_id'] = "sofi1"
        test_dict['name'] = "soff"
        test_dict['description'] = "desc"
        test_dict['number_rooms'] = 3
        test_dict['number_bathrooms'] = 1
        test_dict['max_guest'] = 1
        test_dict['price_by_night'] = 50
        test_dict['latitude'] = 3.0
        test_dict['longitude'] = 30.0
        test_dict['amenity_ids'] = ["par01", "por01", "jac01"]

        obj = Place(**test_dict)
        self.assertEqual(obj.fname, 'sofonias')
        self.assertEqual(obj.age, 27)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.city_id, "Addis ababa")
        self.assertEqual(obj.user_id, "sofi1")
        self.assertEqual(obj.name, "soff")
        self.assertEqual(obj.description, "desc")
        self.assertEqual(obj.number_rooms, 3)
        self.assertEqual(obj.number_bathrooms, 1)
        self.assertEqual(obj.max_guest, 1)
        self.assertEqual(obj.price_by_night, 50)
        self.assertEqual(obj.latitude, 3.0)
        self.assertEqual(obj.longitude, 30.0)
        self.assertEqual(obj.amenity_ids, ["par01", "por01", "jac01"])


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
