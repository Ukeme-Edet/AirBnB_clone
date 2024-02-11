#!/usr/bin/python3

"""
This module contains the Place class, which inherits from BaseModel.
Public class attributes:
    city_id: string - empty string
    user_id: string - empty string
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes the Place object."""
        super().__init__(*args, **kwargs)
