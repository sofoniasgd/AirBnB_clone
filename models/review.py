#!/usr/bin/python3
"""review module. contains review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review class that inherits from Base class.
    public class attributes
        place_id (str) it will be the Place.id
        user_id (str) it will be the User.id
        text (str)
    """

    place_id = ""
    user_id = ""
    text = ""
