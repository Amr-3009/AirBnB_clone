#!/usr/bin/python3
"""user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class
    inherits from BaseModel

    Public Class Attributes:
        email: string
        password: string
        first_name: string
        last_name: string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
