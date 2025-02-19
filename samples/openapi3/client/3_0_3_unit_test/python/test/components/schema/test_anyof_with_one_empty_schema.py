# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.anyof_with_one_empty_schema import AnyofWithOneEmptySchema
from unit_test_api import configuration


class TestAnyofWithOneEmptySchema(unittest.TestCase):
    """AnyofWithOneEmptySchema unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_string_is_valid_passes(self):
        # string is valid
        AnyofWithOneEmptySchema.from_openapi_data_(
            "foo",
            configuration_=self.configuration_
        )

    def test_number_is_valid_passes(self):
        # number is valid
        AnyofWithOneEmptySchema.from_openapi_data_(
            123,
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
