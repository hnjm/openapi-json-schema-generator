# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import unittest

import frozendict

from petstore_api.components.schema import apple
from petstore_api.components.schema import banana
from petstore_api.components.schema.gm_fruit import GmFruit
from petstore_api import schemas

class TestGmFruit(unittest.TestCase):
    """GmFruit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGmFruit(self):
        """Test GmFruit"""

        # make an instance of GmFruit, a composed schema anyOf model
        # banana test
        length_cm = 20.3
        color = 'yellow'
        cultivar = 'banaple'
        fruit = GmFruit(lengthCm=length_cm, color=color, cultivar=cultivar)
        assert isinstance(fruit, banana.Banana)
        assert isinstance(fruit, apple.Apple)
        assert isinstance(fruit, frozendict.frozendict)
        assert isinstance(fruit, GmFruit)
        # check its properties
        self.assertEqual(fruit['lengthCm'], length_cm)
        self.assertEqual(fruit['color'], color)

        # check the dict representation
        self.assertEqual(
            fruit,
            {
                'lengthCm': length_cm,
                'color': color,
                'cultivar': cultivar
            }
        )

        # unset key access raises KeyError
        with self.assertRaises(KeyError):
            fruit["origin"]
        with self.assertRaises(AttributeError):
            fruit.origin
        assert fruit.get_item_("origin") is schemas.unset

        with self.assertRaises(KeyError):
            fruit['unknown_variable']
        assert fruit.get_item_("unknown_variable") is schemas.unset
        # with getattr
        self.assertTrue(getattr(fruit, 'origin', 'some value'), 'some value')

        # including extra parameters works
        GmFruit(
            color=color,
            length_cm=length_cm,
            cultivar=cultivar,
            unknown_property='some value'
        )

        # including input parameters for both anyOf instances works
        color = 'orange'
        fruit = GmFruit(
            color=color,
            cultivar=cultivar,
            length_cm=length_cm
        )
        self.assertEqual(fruit['color'], color)
        self.assertEqual(fruit['cultivar'], cultivar)
        self.assertEqual(fruit['length_cm'], length_cm)

        # make an instance of GmFruit, a composed schema anyOf model
        # apple test
        color = 'red'
        cultivar = 'golden delicious'
        origin = 'California'
        fruit = GmFruit(color=color, cultivar=cultivar, origin=origin)
        # check its properties
        self.assertEqual(fruit['color'], color)
        self.assertEqual(fruit['cultivar'], cultivar)
        self.assertEqual(fruit['origin'], origin)

        # check the dict representation
        self.assertEqual(
            fruit,
            {
                'color': color,
                'cultivar': cultivar,
                'origin': origin,
            }
        )


if __name__ == '__main__':
    unittest.main()
