# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.by_int import ByInt
from unit_test_api import configuration


class TestByInt(unittest.TestCase):
    """ByInt unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_int_by_int_fail_fails(self):
        # int by int fail
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ByInt.from_openapi_data_(
                7,
                configuration_=self.configuration_
            )

    def test_int_by_int_passes(self):
        # int by int
        ByInt.from_openapi_data_(
            10,
            configuration_=self.configuration_
        )

    def test_ignores_non_numbers_passes(self):
        # ignores non-numbers
        ByInt.from_openapi_data_(
            "foo",
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
