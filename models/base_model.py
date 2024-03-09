#!/usr/bin/python3
"""Base model module
    contains BaseModel class
"""
import uuid
from datetime import datetime

class BaseModel:
    """ Defines a Base class 
    it defines all common attributes for all other classes
    """
    def __init__(self, id, created_at, updated_at):
        """init method for BaseModel class
        
        initializes instance attributes
        
        Args:
            id (): 
            created_at ()
            updated_at ()
        
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
