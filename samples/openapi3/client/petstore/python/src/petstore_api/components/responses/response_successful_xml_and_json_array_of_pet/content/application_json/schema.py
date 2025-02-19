# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class Schema(
    schemas.ListSchema
):


    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items() -> typing.Type['ref_pet.RefPet']:
            return ref_pet.RefPet

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union['ref_pet.RefPet', dict, frozendict.frozendict], ...
            ],
            typing.List[
                typing.Union['ref_pet.RefPet', dict, frozendict.frozendict]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'Schema':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> 'ref_pet.RefPet':
        return super().__getitem__(i)

from petstore_api.components.schema import ref_pet
