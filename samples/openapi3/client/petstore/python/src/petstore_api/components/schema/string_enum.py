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


class StringEnum(
    schemas.NoneBase,
    schemas.StrBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            schemas.NoneClass,
            str,
        }
        enum_value_to_name = {
            "placed": "PLACED",
            "approved": "APPROVED",
            "delivered": "DELIVERED",
            "single quoted": "SINGLE_QUOTED",
            "multiple\nlines": "MULTIPLE_LINE_FEED_LF_LINES",
            "double quote \n with newline": "DOUBLE_QUOTE_LINE_FEED_LF_WITH_NEWLINE",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def PLACED(cls):
        return cls("placed")
    
    @schemas.classproperty
    def APPROVED(cls):
        return cls("approved")
    
    @schemas.classproperty
    def DELIVERED(cls):
        return cls("delivered")
    
    @schemas.classproperty
    def SINGLE_QUOTED(cls):
        return cls("single quoted")
    
    @schemas.classproperty
    def MULTIPLE_LINE_FEED_LF_LINES(cls):
        return cls("multiple\nlines")
    
    @schemas.classproperty
    def DOUBLE_QUOTE_LINE_FEED_LF_WITH_NEWLINE(cls):
        return cls("double quote \n with newline")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        arg_: typing.Union[None, str],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'StringEnum':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
