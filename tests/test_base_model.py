#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import datetime
from time import sleep
import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """Tests for Initialization of BaseModel objects."""

    def test_init_no_args(self):
        """Tests if instance is of BaseModel class"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_unique_ids(self):
        """Tests if ids are unique"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at_updated_at(self):
        """Tests if updated and created at attributes are same at first"""
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    def test_str_representation(self):
        """Tests __str__"""
        time_dummy = datetime.datetime.now()
        time_str = repr(time_dummy)
        base = BaseModel()
        base.id = 1
        base.created_at = base.updated_at = time_dummy
        base_str = base.__str__()
        self.assertIn("[BaseModel] (<1>)", base_str)
        self.assertIn("'id': 1", base_str)
        self.assertIn("'created_at': " + time_str, base_str)
        self.assertIn("'updated_at': " + time_str, base_str)


class TestSave(unittest.TestCase):
    """Tests the save method"""
    def test_save(self):
        """Tests the updated time after save"""
        base = BaseModel()
        upt_1 = base.updated_at
        sleep(1)
        base.save()
        self.assertNotEqual(upt_1, base.updated_at)
        self.assertLess(upt_1, base.updated_at)

class TestToDict(unittest.TestCase):
    """Tests the to_dict method"""
    def test_type(self):
        """Tests dict is returned"""
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)

    def test_keys(self):
        """Test for all keys"""
        base = BaseModel()
        self.assertIn('__class__', base.to_dict())
        self.assertIn('created_at', base.to_dict())
        self.assertIn('updated_at', base.to_dict())
        self.assertIn('id', base.to_dict())

    def test_time_format(self):
        my_time = datetime.datetime.now()
        base = BaseModel()
        base.created_at = base.updated_at = my_time
        my_dict = base.to_dict()
        self.assertEqual(my_dict['created_at'], my_time.isoformat())
        self.assertEqual(my_dict['updated_at'], my_time.isoformat())


if __name__ == "__main__":
    unittest.main()