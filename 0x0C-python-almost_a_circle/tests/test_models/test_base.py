#!/usr/bin/python3
"""Test cases for base.py class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for base
    """
    def test_base_exist(self):
        """Test if base exist
        """
        a = Base()
        assert a

    def test_base_id(self):
        """Test if id is being set properly
        note it should equal 2 because of the
        previous test.
        """
        a = Base()
        assert a.id == 2

    def test_to_json_string_empty(self):
        """Test for empty list
        """
        a = Base()
        assert a.to_json_string([]) == "[]"

    def test_to_json_string_None(self):
        """Test for list == None
        """
        a = Base()
        assert a.to_json_string(None) == "[]"

    def test_to_json_string_std_return(self):
        """Test for std return value
        """
        a = Base()
        b = {"width": 10, "height": 7, "x": 2, "y": 8}
        assert a.to_json_string([b]) == \
            '[{"width": 10, "height": 7, "x": 2, "y": 8}]'

    def test_to_json_string_bad_type_int(self):
        """Test to see what happens when int is passed
        """
        a = Base()
        assert a.to_json_string(1) == '1'

    def test_to_json_string_bad_type_float(self):
        """Test to see what happens when float is passed
        """
        a = Base()
        assert a.to_json_string(1.0) == "1.0"

    def test_to_json_string_bad_type_str(self):
        """Test to see what happens when str is passed
        """
        a = Base()
        assert a.to_json_string("1") == '"1"'

    def test_to_json_string_bad_type_bool(self):
        """Test to see what happens when bool is passed
        """
        a = Base()
        assert a.to_json_string(True) == "true"
