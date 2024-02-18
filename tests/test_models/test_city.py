#!/usr/bin/python3
"""
Tests of City model
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test documentation of the City model"""

    def __init__(self, *args, **kwargs):
        """Initialization of city test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute"""
        new = self.value(state_id="")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute"""
        new = self.value(name="")
        self.assertEqual(type(new.name), str)

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(City.__doc__)
