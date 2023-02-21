#!/usr/bin/python3
"""Definir id du User"""


import email
from models.base_model import BaseModel


class User(BaseModel):
    """definir class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
