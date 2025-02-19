# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import unittest

import frozendict

import petstore_api
from petstore_api.components.schema.cat import Cat
from petstore_api.components.schema.dog import Dog
from petstore_api.components.schema.animal import Animal
from petstore_api.schemas import StrSchema, BoolSchema


class TestAnimal(unittest.TestCase):
    """Animal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnimal(self):
        """Test Animal"""

        regex_err = (
            r"Invalid discriminator value was passed in to Animal.className "
            r"Only the values \['Cat', 'Dog'\] are allowed at \('args\[0\]', 'className'\)"
        )
        with self.assertRaisesRegex(petstore_api.ApiValueError, regex_err):
            Animal(className='Fox', color='red')

        animal = Animal(className='Cat', color='black')
        assert isinstance(animal, frozendict.frozendict)
        assert isinstance(animal, Cat)
        assert isinstance(animal, Cat.Schema_.AllOf.classes[1])
        assert isinstance(animal, Animal)
        assert set(animal.keys()) == {'className', 'color'}
        assert animal.className == 'Cat'
        assert animal["color"] == 'black'
        assert isinstance(animal["color"], StrSchema)
        assert isinstance(animal.className, StrSchema)

        # pass in optional param
        animal = Animal(className='Cat', color='black', declawed=True)
        assert isinstance(animal, Animal)
        assert isinstance(animal, frozendict.frozendict)
        assert isinstance(animal, Cat)
        assert isinstance(animal, Cat.Schema_.AllOf.classes[1])
        assert set(animal.keys()) == {'className', 'color', 'declawed'}
        assert animal.className == 'Cat'
        assert animal["color"] == 'black'
        assert bool(animal["declawed"]) is True
        assert isinstance(animal["color"], StrSchema)
        assert isinstance(animal.className, StrSchema)
        assert isinstance(animal["declawed"], BoolSchema)

        # make a Dog
        animal = Animal(className='Dog', color='black')
        assert isinstance(animal, Animal)
        assert isinstance(animal, frozendict.frozendict)
        assert isinstance(animal, Dog)
        assert isinstance(animal, Dog.Schema_.AllOf.classes[1])
        assert set(animal.keys()) == {'className', 'color'}
        assert animal.className == 'Dog'
        assert animal["color"] == 'black'
        assert isinstance(animal["color"], StrSchema)
        assert isinstance(animal.className, StrSchema)

        # pass in optional param
        animal = Animal(className='Dog', color='black', breed='Labrador')
        assert isinstance(animal, Animal)
        assert isinstance(animal, frozendict.frozendict)
        assert isinstance(animal, Dog)
        assert isinstance(animal, Dog.Schema_.AllOf.classes[1])
        assert set(animal.keys()) == {'className', 'color', 'breed'}
        assert animal.className == 'Dog'
        assert animal["color"] == 'black'
        assert animal["breed"] == 'Labrador'
        assert isinstance(animal.className, StrSchema)
        assert isinstance(animal["color"], StrSchema)
        assert isinstance(animal["breed"], StrSchema)


if __name__ == '__main__':
    unittest.main()
