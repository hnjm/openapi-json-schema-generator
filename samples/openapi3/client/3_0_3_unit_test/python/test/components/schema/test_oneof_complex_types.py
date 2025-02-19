# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.oneof_complex_types import OneofComplexTypes
from unit_test_api import configuration


class TestOneofComplexTypes(unittest.TestCase):
    """OneofComplexTypes unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_first_oneof_valid_complex_passes(self):
        # first oneOf valid (complex)
        OneofComplexTypes.from_openapi_data_(
            {
                "bar":
                    2,
            },
            configuration_=self.configuration_
        )

    def test_neither_oneof_valid_complex_fails(self):
        # neither oneOf valid (complex)
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofComplexTypes.from_openapi_data_(
                {
                    "foo":
                        2,
                    "bar":
                        "quux",
                },
                configuration_=self.configuration_
            )

    def test_both_oneof_valid_complex_fails(self):
        # both oneOf valid (complex)
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofComplexTypes.from_openapi_data_(
                {
                    "foo":
                        "baz",
                    "bar":
                        2,
                },
                configuration_=self.configuration_
            )

    def test_second_oneof_valid_complex_passes(self):
        # second oneOf valid (complex)
        OneofComplexTypes.from_openapi_data_(
            {
                "foo":
                    "baz",
            },
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
