#!/usr/bin/python3
"""Base model module
    contains BaseModel class
"""

from uuid import uuid4
from datetime import datetime

from models import storage


class BaseModel:
    """ Defines a Base class
    it defines all common attributes for all other classes
    """
    def __init__(self, *args, **kwargs):
        """constructor for BaseModel

        uses keyworded arguments to make instance attributes
            * each key is an attribute name
                !!except(__class__)!!
            * each value of the key is now value of the attribute
            * created_at and updated_at should be converted to
                datetime objects from string
        if no argument dict passed then use default instance attributes
            Attributes:
                id (str):
                created_at (datetime)
                updated_at (datetime)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                # convert time attribes to datetime objects
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # !! calling new(self) of storage if new instance
            storage.new(self)


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
        # !! calling save(self) of storage !!
        storage.save()

    def to_dict(self):
        """returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        # format for dates: %Y-%m-%dT%H:%M:%S.%f then convert to string
        created = self.created_at.isoformat()
        # print(type(created))
        # print(created.isoformat())
        # print(type(created.isoformat()))
        updated = self.updated_at.isoformat()
        dictionary['created_at'] = created
        dictionary['updated_at'] = updated
        return dictionary
