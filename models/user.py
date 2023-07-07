#!/usr/bin/python3
"""
User creation class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """inheritated class User from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
