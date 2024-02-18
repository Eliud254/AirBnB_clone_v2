#!/usr/bin/python3
"""
Tests of Place model
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test documentation of the Place model"""

    def __init__(self, *args, **kwargs):
        """Initialization of place test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_docstring(self):
        """Testing docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_city_id(self):
        """Testing city_id"""
        new = self.value(city_id="")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Testing user_id """
        new = self.value(user_id="")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Testing name """
        new = self.value(name="")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Testing description"""
        new = self.value(description="")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Testing number of rooms"""
        new = self.value(number_rooms=0)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Testing number of bathrooms"""
        new = self.value(number_bathrooms=0)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Testing max_guest """
        new = self.value(max_guest=0)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Testing price_by_night"""
        new = self.value(price_by_night=0)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Testing latitude"""
        new = self.value(latitude=0.0)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Testing longitude"""
        new = self.value(longitude=0.0)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Testing amenity_ids """
        new = self.value(amenity_ids=[])
        self.assertEqual(type(new.amenity_ids), list)
