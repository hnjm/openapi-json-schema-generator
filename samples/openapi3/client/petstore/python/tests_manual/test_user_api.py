# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""
import unittest
from unittest.mock import patch

import petstore_api
from petstore_api import api_client
from petstore_api.apis.tags.user_api import UserApi
from petstore_api.rest import RESTClientObject
from petstore_api.configurations import api_configuration

from . import ApiTestMixin


class TestUserApi(ApiTestMixin):
    """UserApi unit test stubs"""
    configuration = api_configuration.ApiConfiguration()
    api = UserApi(api_client=api_client.ApiClient(configuration=configuration))

    def test_create_user(self):
        """Test case for create_user

        Create user  # noqa: E501
        """
        pass

    def test_create_users_with_array_input(self):
        """Test case for create_users_with_array_input

        Creates list of users with given input array  # noqa: E501
        """
        pass

    def test_create_users_with_list_input(self):
        """Test case for create_users_with_list_input

        Creates list of users with given input array  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        pass

    def test_get_user_by_name(self):
        from petstore_api.components.schema import user

        # serialization + deserialization works
        with patch.object(RESTClientObject, 'request') as mock_request:
            value_simple = dict(
                id=1,
                username='first last',
                firstName='first',
                lastName='last'
            )
            body = user.User(**value_simple)
            mock_request.return_value = self.response(
                self.json_bytes(value_simple)
            )

            api_response = self.api.get_user_by_name(
                path_params=dict(username='first last')
            )
            self.assert_request_called_with(
                mock_request,
                'http://petstore.swagger.io:80/v2/user/first%20last',
                method='GET',
                accept_content_type='application/xml, application/json',
                content_type=None
            )

            assert isinstance(api_response.body, user.User)
            assert api_response.body == body

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system  # noqa: E501
        """
        pass

    def test_logout_user(self):
        """Test case for logout_user

        Logs out current logged in user session  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Updated user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
