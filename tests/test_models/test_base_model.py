#!/usr/bin/python3
"""
Tests of Base model
"""
import inspect
import models
import unittest
import datetime
import json
import os
from models.base_model import BaseModel
from uuid import UUID

BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db", "basemodel not supported"
)
class TestBaseModelDocs(unittest.TestCase):
    """Testing  to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Setting up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Testing for the existence of module docstring"""
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Testing for the BaseModel class docstring"""
        self.assertIsNot(
            BaseModel.__doc__, None, "BaseModel class needs a docstring"
        )
        self.assertTrue(
            len(BaseModel.__doc__) >= 1, "BaseModel class needs a docstring"
        )

    def test_func_docstrings(self):
        """Test for  presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0]),
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0]),
                )


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db", "basemodel not supported"
)
class test_basemodel(unittest.TestCase):
    """Class to test documentation of the Base model"""

    def __init__(self, *args, **kwargs):
        """Initialization  the class"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Setting up base model tests"""
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_default(self):
        """The default test"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Keyword argument for tests"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """TypeError when the keyword argument is an integer"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test saved"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation"""
        i = self.value()
        self.assertEqual(
            str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__)
        )

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test keyword argument is none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test one keyword argument"""
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        new.save()
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
