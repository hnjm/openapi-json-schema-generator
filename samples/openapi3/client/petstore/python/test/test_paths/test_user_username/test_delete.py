# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.user_username.delete import operation as delete  # noqa: E501
from petstore_api import schemas, api_client
from petstore_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestDelete(ApiTestMixin, unittest.TestCase):
    """
    Delete unit test stubs
        Delete user  # noqa: E501
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_config=schema_config)
    api = delete.ApiForDelete(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body = ''

if __name__ == '__main__':
    unittest.main()
