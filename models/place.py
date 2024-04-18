#!/usr/bin/python3
"""place module. contains place class """


from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a place class that inherits from Base class.
    public class attributes:
        city_id (str) it wil be Place.id(overrides BaseModel.id)
        user_id (str) it wil be User.id(overrides BaseModel.id)
        name (str)
        description (str)
        number_rooms (int)
        number_bathrooms (int)
        max_guest (int)
        price_by_night (int)
        latitude (float)
        longitude (float)
        amenity_ids (list)  it will be the list of Amenity.id

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
