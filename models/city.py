#!/usr/bin/python3
"""defines the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    represents city Class
    Inherits from BaseModel

    Attributes:
        name (str): the name of the city
        state_id (str): the state id
    """

    name = ""
    state_id = ""
