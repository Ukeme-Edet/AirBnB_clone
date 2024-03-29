#!/usr/bin/python3

"""
This module contains the Amenity class, which inherits from BaseModel.
Public class attributes:
    name: string - empty string
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity object."""
        super().__init__(*args, **kwargs)
