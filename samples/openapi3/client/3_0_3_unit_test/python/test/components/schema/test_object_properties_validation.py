# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.object_properties_validation import ObjectPropertiesValidation
from unit_test_api import configuration


class TestObjectPropertiesValidation(unittest.TestCase):
    """ObjectPropertiesValidation unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_ignores_arrays_passes(self):
        # ignores arrays
        ObjectPropertiesValidation.from_openapi_data_(
            [
            ],
            configuration_=self.configuration_
        )

    def test_ignores_other_non_objects_passes(self):
        # ignores other non-objects
        ObjectPropertiesValidation.from_openapi_data_(
            12,
            configuration_=self.configuration_
        )

    def test_one_property_invalid_is_invalid_fails(self):
        # one property invalid is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ObjectPropertiesValidation.from_openapi_data_(
                {
                    "foo":
                        1,
                    "bar":
                        {
                        },
                },
                configuration_=self.configuration_
            )

    def test_both_properties_present_and_valid_is_valid_passes(self):
        # both properties present and valid is valid
        ObjectPropertiesValidation.from_openapi_data_(
            {
                "foo":
                    1,
                "bar":
                    "baz",
            },
            configuration_=self.configuration_
        )

    def test_doesn_t_invalidate_other_properties_passes(self):
        # doesn&#x27;t invalidate other properties
        ObjectPropertiesValidation.from_openapi_data_(
            {
                "quux":
                    [
                    ],
            },
            configuration_=self.configuration_
        )

    def test_both_properties_invalid_is_invalid_fails(self):
        # both properties invalid is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ObjectPropertiesValidation.from_openapi_data_(
                {
                    "foo":
                        [
                        ],
                    "bar":
                        {
                        },
                },
                configuration_=self.configuration_
            )


if __name__ == '__main__':
    unittest.main()
