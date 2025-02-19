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
from petstore_api.schemas import BoolClass
from petstore_api.components.schema.whale import Whale


class TestWhale(unittest.TestCase):
    """Whale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Whale(self):
        # test that the hasBaleen __bool__ method is working, True input
        whale = Whale(
            className='whale',
            hasBaleen=True
        )
        assert isinstance(whale["hasBaleen"], BoolClass)
        self.assertTrue(whale["hasBaleen"])

        # test that the hasBaleen __bool__ method is working, False input
        whale = Whale(
            className='whale',
            hasBaleen=False
        )
        assert isinstance(whale["hasBaleen"], BoolClass)
        self.assertFalse(whale["hasBaleen"])


if __name__ == '__main__':
    unittest.main()
