# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_the_default_keyword_does_not_do_anything_if_the_property_is_missing_request_body.post import operation as post  # noqa: E501
from unit_test_api import schemas, api_client
from unit_test_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPost(ApiTestMixin, unittest.TestCase):
    """
    Post unit test stubs
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_config=schema_config)
    api = post.ApiForPost(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body = ''

    def test_missing_properties_are_not_filled_in_with_the_default_passes(self):
        content_type = 'application/json'
        # missing properties are not filled in with the default
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                }
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
                content_type=content_type
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_an_explicit_property_value_is_checked_against_maximum_passing_passes(self):
        content_type = 'application/json'
        # an explicit property value is checked against maximum (passing)
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "alpha":
                        1,
                }
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
                content_type=content_type
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_an_explicit_property_value_is_checked_against_maximum_failing_fails(self):
        content_type = 'application/json'
        # an explicit property value is checked against maximum (failing)
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "alpha":
                        5,
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

if __name__ == '__main__':
    unittest.main()
