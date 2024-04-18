#!/usr/bin/python3
"""city module. contains city class """


from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city class that inherits from Base class.
    public class attributes:
        state_id (str) it will be the State.id(overrides BaseModel.id)
        name (str)
    """

    state_id = ""
    name = ""
