# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import sys
import unittest
from datetime import date, datetime, timezone

import petstore_api
from petstore_api.components.schema.array_holding_any_type import ArrayHoldingAnyType
from petstore_api.schemas import NoneClass, BoolClass


class TestArrayHoldingAnyType(unittest.TestCase):
    """ArrayHoldingAnyType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testArrayHoldingAnyType(self):
        """Test ArrayHoldingAnyType"""

        enum_values = [True, False]
        for enum_value in enum_values:
            inst = ArrayHoldingAnyType([enum_value])
            assert isinstance(inst, ArrayHoldingAnyType)
            assert isinstance(inst, tuple)
            assert isinstance(inst[0], BoolClass)
            assert bool(inst[0]) is enum_value

        inst = ArrayHoldingAnyType([None])
        assert isinstance(inst, ArrayHoldingAnyType)
        assert isinstance(inst, tuple)
        assert isinstance(inst[0], NoneClass)

        input_to_stored_value = [
            (0, 0),
            (3.14, 3.14),
            (date(1970, 1, 1), '1970-01-01'),
            (datetime(1970, 1, 1, 0, 0, 0), '1970-01-01T00:00:00'),
            (datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc), '1970-01-01T00:00:00+00:00'),
            ([], ()),
            ({}, {}),
            ('hi', 'hi'),
        ]
        for input, stored_value in input_to_stored_value:
            inst = ArrayHoldingAnyType([input])
            assert isinstance(inst, ArrayHoldingAnyType)
            assert isinstance(inst, tuple)
            assert inst[0] == stored_value

if __name__ == '__main__':
    unittest.main()
