# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

from petstore_api import schemas, exceptions
from petstore_api.components.schema.object_with_inline_composition_property import ObjectWithInlineCompositionProperty


class TestObjectWithInlineCompositionProperty(unittest.TestCase):
    """ObjectWithInlineCompositionProperty unit test stubs"""

    def test_ObjectWithInlineCompositionProperty(self):
        """Test ObjectWithInlineCompositionProperty"""
        model = ObjectWithInlineCompositionProperty(someProp='a')
        self.assertTrue(
            isinstance(
                model["someProp"],
                ObjectWithInlineCompositionProperty.Schema_.Properties.SomeProp
            )
        )
        self.assertTrue(isinstance(model["someProp"], schemas.StrSchema))

        # error thrown on length < 1
        with self.assertRaises(exceptions.ApiValueError):
            ObjectWithInlineCompositionProperty(someProp='')


if __name__ == '__main__':
    unittest.main()
