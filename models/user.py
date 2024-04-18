#!/usr/bin/python3
"""user module contains user class """


from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user class
    public class atributes
        email: (str)
        password: (str)
        first_name: (str)
        last_name: (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
