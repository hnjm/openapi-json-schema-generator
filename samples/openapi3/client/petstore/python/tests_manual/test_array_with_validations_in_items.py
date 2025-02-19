# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import sys
import unittest

import petstore_api
from petstore_api.components.schema.array_with_validations_in_items import ArrayWithValidationsInItems


class TestArrayWithValidationsInItems(unittest.TestCase):
    """ArrayWithValidationsInItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testArrayWithValidationsInItems(self):
        """Test ArrayWithValidationsInItems"""

        valid_values = [-1, 5, 7]
        for valid_value in valid_values:
            inst = ArrayWithValidationsInItems([valid_value])
            assert isinstance(inst, ArrayWithValidationsInItems)
            assert inst == (valid_value,)

        with self.assertRaisesRegex(
            petstore_api.exceptions.ApiValueError,
            r"Invalid value `8`, must be a value less than or equal to `7` at \('args\[0\]', 0\)"
        ):
            ArrayWithValidationsInItems([8])

        with self.assertRaisesRegex(
            petstore_api.exceptions.ApiValueError,
            r"Invalid value `\(Decimal\('1'\), Decimal\('2'\), Decimal\('3'\)\)`, number of items must be less than or equal to `2` at \('args\[0\]',\)"
        ):
            ArrayWithValidationsInItems([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
