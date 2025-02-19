# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.allof_with_base_schema import AllofWithBaseSchema
from unit_test_api import configuration


class TestAllofWithBaseSchema(unittest.TestCase):
    """AllofWithBaseSchema unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_valid_passes(self):
        # valid
        AllofWithBaseSchema.from_openapi_data_(
            {
                "foo":
                    "quux",
                "bar":
                    2,
                "baz":
                    None,
            },
            configuration_=self.configuration_
        )

    def test_mismatch_first_allof_fails(self):
        # mismatch first allOf
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofWithBaseSchema.from_openapi_data_(
                {
                    "bar":
                        2,
                    "baz":
                        None,
                },
                configuration_=self.configuration_
            )

    def test_mismatch_base_schema_fails(self):
        # mismatch base schema
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofWithBaseSchema.from_openapi_data_(
                {
                    "foo":
                        "quux",
                    "baz":
                        None,
                },
                configuration_=self.configuration_
            )

    def test_mismatch_both_fails(self):
        # mismatch both
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofWithBaseSchema.from_openapi_data_(
                {
                    "bar":
                        2,
                },
                configuration_=self.configuration_
            )

    def test_mismatch_second_allof_fails(self):
        # mismatch second allOf
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofWithBaseSchema.from_openapi_data_(
                {
                    "foo":
                        "quux",
                    "bar":
                        2,
                },
                configuration_=self.configuration_
            )


if __name__ == '__main__':
    unittest.main()
