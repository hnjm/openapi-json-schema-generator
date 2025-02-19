# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

from petstore_api.components.schema.additional_properties_class import AdditionalPropertiesClass
from petstore_api import schemas


class TestAdditionalPropertiesClass(unittest.TestCase):
    """AdditionalPropertiesClass unit test stubs"""

    def test_additional_properties_class(self):
        inst = AdditionalPropertiesClass({})
        with self.assertRaises(KeyError):
            inst["map_property"]
        assert inst.get_item_("map_property") is schemas.unset
        with self.assertRaises(AttributeError):
            inst.map_property

        inst = AdditionalPropertiesClass(map_property={})
        map_property = inst["map_property"]
        assert map_property == {}


if __name__ == '__main__':
    unittest.main()
