# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.additionalproperties_should_not_look_in_applicators import AdditionalpropertiesShouldNotLookInApplicators
from unit_test_api import configuration


class TestAdditionalpropertiesShouldNotLookInApplicators(unittest.TestCase):
    """AdditionalpropertiesShouldNotLookInApplicators unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_properties_defined_in_allof_are_not_examined_fails(self):
        # properties defined in allOf are not examined
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AdditionalpropertiesShouldNotLookInApplicators.from_openapi_data_(
                {
                    "foo":
                        1,
                    "bar":
                        True,
                },
                configuration_=self.configuration_
            )

    def test_valid_test_case_passes(self):
        # valid test case
        AdditionalpropertiesShouldNotLookInApplicators.from_openapi_data_(
            {
                "foo":
                    False,
                "bar":
                    True,
            },
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
