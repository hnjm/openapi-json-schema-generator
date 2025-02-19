# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""
import unittest
import collections

from petstore_api import api_client, exceptions, schemas

from . import ParamTestCase


class TestParameter(unittest.TestCase):
    invalid_inputs = (
        True,
        False
    )

    def test_query_style_form_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='?color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='?color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='?color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='?color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='?color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue&color=black&color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?R=100&G=200&B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.QueryParameter):
                name='color'
                style=api_client.ParameterStyle.FORM
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.QueryParameter):
                        name='color'
                        style=api_client.ParameterStyle.FORM
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_cookie_style_form_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='color=hello world')
            ),
            ParamTestCase(
                '',
                dict(color='color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue&color=black&color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100&G=200&B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.CookieParameter):
                name='color'
                style=api_client.ParameterStyle.FORM
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.CookieParameter):
                        name='color'
                        style=api_client.ParameterStyle.FORM
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_simple_in_path_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100,G=200,B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.PathParameter):
                name='color'
                style=api_client.ParameterStyle.SIMPLE
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.PathParameter):
                        name='color'
                        style=api_client.ParameterStyle.SIMPLE
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_simple_in_header_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100,G=200,B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.HeaderParameter):
                name='color'
                style=api_client.ParameterStyle.SIMPLE
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.HeaderParameter):
                        name='color'
                        style=api_client.ParameterStyle.SIMPLE
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_label_in_path_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='.1')
            ),
            ParamTestCase(
                3.14,
                dict(color='.3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='.blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='.hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='.')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='.blue.black.brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='.blue.black.brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='.R.100.G.200.B.150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='.R=100.G=200.B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.PathParameter):
                name='color'
                style=api_client.ParameterStyle.LABEL
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.PathParameter):
                        name='color'
                        style=api_client.ParameterStyle.LABEL
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_matrix_in_path_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color=';color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color=';color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color=';color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color=';color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color=';color')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color=';color=blue,black,brown')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color=';color=blue;color=black;color=brown'),
                explode=True
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color=';color=R,100,G,200,B,150')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color=';R=100;G=200;B=150'),
                explode=True
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.PathParameter):
                name='color'
                style=api_client.ParameterStyle.MATRIX
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.PathParameter):
                        name='color'
                        style=api_client.ParameterStyle.MATRIX
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_space_delimited_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue%20black%20brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R%20100%20G%20200%20B%20150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.QueryParameter):
                name='color'
                style=api_client.ParameterStyle.SPACE_DELIMITED
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.QueryParameter):
                        name='color'
                        style=api_client.ParameterStyle.SPACE_DELIMITED
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_style_pipe_delimited_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue|black|brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R|100|G|200|B|150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.QueryParameter):
                name='color'
                style=api_client.ParameterStyle.PIPE_DELIMITED
                schema=schemas.AnyTypeSchema
                explode=test_case.explode

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                for explode_value in (True, False):
                    class Parameter(api_client.QueryParameter):
                        name='color'
                        style=api_client.ParameterStyle.PIPE_DELIMITED
                        schema=schemas.AnyTypeSchema
                        explode=explode_value

                    Parameter.serialize(invalid_input)

    def test_path_params_no_style(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.PathParameter):
                name='color'
                schema=schemas.AnyTypeSchema

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                class Parameter(api_client.PathParameter):
                    name='color'
                    schema=schemas.AnyTypeSchema

                Parameter.serialize(invalid_input)

    def test_header_params_no_style(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='1')
            ),
            ParamTestCase(
                3.14,
                dict(color='3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='hello world')
            ),
            ParamTestCase(
                '',
                dict(color='')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='blue,black,brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R,100,G,200,B,150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.HeaderParameter):
                name='color'
                schema=schemas.AnyTypeSchema

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                class Parameter(api_client.HeaderParameter):
                    name='color'
                    schema=schemas.AnyTypeSchema

                Parameter.serialize(invalid_input)

    def test_query_params_no_style(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='?color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='?color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='?color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='?color=hello%20world')
            ),
            ParamTestCase(
                '',
                dict(color='?color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='?color=blue&color=black&color=brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='?R=100&G=200&B=150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.QueryParameter):
                name='color'
                schema=schemas.AnyTypeSchema

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                class Parameter(api_client.QueryParameter):
                    name='color'
                    schema=schemas.AnyTypeSchema

                Parameter.serialize(invalid_input)

    def test_cookie_params_no_style(self):
        test_cases = (
            ParamTestCase(
                None,
                dict(color='')
            ),
            ParamTestCase(
                1,
                dict(color='color=1')
            ),
            ParamTestCase(
                3.14,
                dict(color='color=3.14')
            ),
            ParamTestCase(
                'blue',
                dict(color='color=blue')
            ),
            ParamTestCase(
                'hello world',
                dict(color='color=hello world')
            ),
            ParamTestCase(
                '',
                dict(color='color=')
            ),
            ParamTestCase(
                [],
                dict(color='')
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                dict(color='color=blue&color=black&color=brown')
            ),
            ParamTestCase(
                {},
                dict(color='')
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                dict(color='R=100&G=200&B=150')
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.CookieParameter):
                name='color'
                schema=schemas.AnyTypeSchema

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

        with self.assertRaises(exceptions.ApiValueError):
            for invalid_input in self.invalid_inputs:
                class Parameter(api_client.CookieParameter):
                    name='color'
                    schema=schemas.AnyTypeSchema

                Parameter.serialize(invalid_input)

    def test_header_content_json_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                {'color': 'null'}
            ),
            ParamTestCase(
                1,
                {'color': '1'}
            ),
            ParamTestCase(
                3.14,
                {'color': '3.14'}
            ),
            ParamTestCase(
                'blue',
                {'color': '"blue"'}
            ),
            ParamTestCase(
                'hello world',
                {'color': '"hello world"'}
            ),
            ParamTestCase(
                '',
                {'color': '""'}
            ),
            ParamTestCase(
                True,
                {'color': 'true'}
            ),
            ParamTestCase(
                False,
                {'color': 'false'}
            ),
            ParamTestCase(
                [],
                {'color': '[]'}
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                {'color': '["blue", "black", "brown"]'}
            ),
            ParamTestCase(
                {},
                {'color': '{}'}
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                {'color': '{"R": 100, "G": 200, "B": 150}'}
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.HeaderParameter):


                class __MediaType(api_client.MediaType):
                    schema = schemas.AnyTypeSchema

                name='color'
                content={'application/json': __MediaType}

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

    def test_query_content_json_serialization(self):
        test_cases = (
            ParamTestCase(
                None,
                {'color': '?color=null'}
            ),
            ParamTestCase(
                1,
                {'color': '?color=1'}
            ),
            ParamTestCase(
                3.14,
                {'color': '?color=3.14'}
            ),
            ParamTestCase(
                'blue',
                {'color': '?color=%22blue%22'}
            ),
            ParamTestCase(
                'hello world',
                {'color': '?color=%22hello%20world%22'}
            ),
            ParamTestCase(
                '',
                {'color': '?color=%22%22'}
            ),
            ParamTestCase(
                True,
                {'color': '?color=true'}
            ),
            ParamTestCase(
                False,
                {'color': '?color=false'}
            ),
            ParamTestCase(
                [],
                {'color': '?color=%5B%5D'}
            ),
            ParamTestCase(
                ['blue', 'black', 'brown'],
                {'color': '?color=%5B%22blue%22%2C%22black%22%2C%22brown%22%5D'}
            ),
            ParamTestCase(
                {},
                {'color': '?color=%7B%7D'}
            ),
            ParamTestCase(
                dict(R=100, G=200, B=150),
                {'color': '?color=%7B%22R%22%3A100%2C%22G%22%3A200%2C%22B%22%3A150%7D'}
            ),
        )
        for test_case in test_cases:
            class Parameter(api_client.QueryParameter):


                class __MediaType(api_client.MediaType):
                    schema = schemas.AnyTypeSchema

                name='color'
                content={'application/json': __MediaType}

            serialization = Parameter.serialize(test_case.payload)
            self.assertEqual(serialization, test_case.expected_serialization)

    def test_throws_error_for_unimplemented_serialization(self):
        with self.assertRaises(NotImplementedError):
            class Parameter(api_client.HeaderParameter):


                class __MediaType(api_client.MediaType):
                    schema = schemas.AnyTypeSchema

                name='color'
                content={'text/plain': __MediaType}

            Parameter.serialize(None)


if __name__ == '__main__':
    unittest.main()
