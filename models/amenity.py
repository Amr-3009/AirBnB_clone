#!/usr/bin/python3
"""Defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    Inherits from BaseModel

    Attributes:
        name (str): The name of amenity
    """
    name = ""
