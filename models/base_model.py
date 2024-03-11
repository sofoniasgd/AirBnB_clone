#!/usr/bin/python3
"""Base model module
    contains BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines a Base class
    it defines all common attributes for all other classes
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        """init method for BaseModel class

        initializes instance attributes

        Args:
            id ():
            created_at ()
            updated_at ()

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str() method to display specific text"""

        # get classname
        classn = str(self.__class__.__name__)
        # format string: [<class name>] (<self.id>) <self.__dict__>
        string = "[{}] ({}) {}".format(classn, self.id, str(self.__dict__))
        return string

    def save(self):
        """updates the public instance attribute
        i.e "updated_at" with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        # format for dates: %Y-%m-%dT%H:%M:%S.%f then convert to string
        dictionary['created_at'] = str(self.created_at.isoformat())
        dictionary['updated_at'] = str(self.updated_at.isoformat())
        return dictionary
