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


class AdditionalPropertiesValidator(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            frozendict.frozendict,
        }
        
        class AllOf:
            
            
            class _0(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties = schemas.AnyTypeSchema
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                ) -> 'AdditionalPropertiesValidator.Schema_.AllOf._0':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class _1(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    
                    class AdditionalProperties(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class Schema_:
                            # any type
                            min_length = 3
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'AdditionalPropertiesValidator.Schema_.AllOf._1.Schema_.AdditionalProperties':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                ) -> 'AdditionalPropertiesValidator.Schema_.AllOf._1':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class _2(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    
                    class AdditionalProperties(
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class Schema_:
                            # any type
                            max_length = 5
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'AdditionalPropertiesValidator.Schema_.AllOf._2.Schema_.AdditionalProperties':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                ) -> 'AdditionalPropertiesValidator.Schema_.AllOf._2':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            classes = [
                _0,
                _1,
                _2,
            ]


    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'AdditionalPropertiesValidator':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
