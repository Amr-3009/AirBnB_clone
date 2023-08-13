#!/usr/bin/python3
"""Defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    represents Review Class

    Attributes:
        place_id (str): place id
        user_id (str): user_id
        text (str): review content
    """

    place_id = ""
    user_id = ""
    text = ""
