# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import sys
import unittest

import petstore_api
from petstore_api.schemas import AnyTypeSchema, DictSchema, IntSchema, StrSchema, Float32Schema, DateSchema
from petstore_api.components.schema.danish_pig import DanishPig
from petstore_api.components.schema.basque_pig import BasquePig
from petstore_api.components.schema.no_additional_properties import NoAdditionalProperties
from petstore_api.components.schema.address import Address
from petstore_api.components.schema.apple_req import AppleReq
from petstore_api.components.schema.banana_req import BananaReq
from petstore_api.components.schema.player import Player

class TestCombineObjectSchemas(unittest.TestCase):
    pass
#     def test_invalid_combo_additional_properties_missing(self):
#         regex_err = (
#             r"Cannot combine additionalProperties schemas from.+?DanishPig.+?and.+?NoAdditionalProperties.+?"
#             r"in.+?Combo.+?because additionalProperties does not exist in both schemas"
#         )
#         with self.assertRaisesRegex(petstore_api.ApiTypeError, regex_err):
#             class Combo(DanishPig, NoAdditionalProperties):
#                 pass
#
#     def test_invalid_combo_both_no_addprops(self):
#         regex_err = (
#             r"Cannot combine schemas from.+?AppleReq.+?and.+?BananaReq.+?"
#             r"in.+?Combo.+?because cultivar is missing from.+?BananaReq.+?"
#         )
#         with self.assertRaisesRegex(petstore_api.ApiTypeError, regex_err):
#             class Combo(AppleReq, BananaReq):
#                 pass
#
#     def test_valid_no_addprops(self):
#         class FirstSchema(DictSchema):
#
#
#             class a(IntSchema):
#                 _validations = {
#                     'inclusive_maximum': 20,
#                 }
#
#             b = Float32Schema
#
#             _additional_properties = None
#
#         class SecondSchema(DictSchema):
#
#
#             class a(IntSchema):
#                 _validations = {
#                     'inclusive_minimum': 10,
#                 }
#
#             b = Float32Schema
#
#             _additional_properties = None
#
#         class Combo(FirstSchema, SecondSchema):
#             pass
#
#         assert Combo._additional_properties is None
#         self.assertEqual(Combo._property_names, ('a', 'b'))
#         assert Combo.a._validations == {
#             'inclusive_maximum': 20,
#             'inclusive_minimum': 10,
#         }
#         assert Combo.b is Float32Schema
#
#
#     def test_valid_combo_additional_properties_anytype_prim(self):
#         class TwoPropsAndIntegerAddProp(DictSchema):
#             a = StrSchema
#             b = Float32Schema
#             _additional_properties = IntSchema
#
#         class OnePropAndAnyTypeAddProps(DictSchema):
#             c = IntSchema
#             _additional_properties = AnyTypeSchema
#
#         class Combo(TwoPropsAndIntegerAddProp, OnePropAndAnyTypeAddProps):
#             pass
#
#         assert Combo._additional_properties is TwoPropsAndIntegerAddProp._additional_properties
#         self.assertEqual(Combo._property_names, ('a', 'b', 'c'))
#         assert Combo.a is TwoPropsAndIntegerAddProp.a
#         assert Combo.b is TwoPropsAndIntegerAddProp.b
#         assert Combo.c is OnePropAndAnyTypeAddProps.c
#
#     def test_invalid_type_disagreement(self):
#         class StrSchemaA(DictSchema):
#             a = StrSchema
#             _additional_properties = AnyTypeSchema
#
#         class FloatSchemaA(DictSchema):
#             a = Float32Schema
#             _additional_properties = AnyTypeSchema
#
#         regex_err = (
#             r"Cannot combine schemas.+?StrSchema.+?and.+?Float32Schema.+?"
#             r"in.+?a.+?because their types do not intersect"
#         )
#         with self.assertRaisesRegex(petstore_api.ApiTypeError, regex_err):
#             class Combo(StrSchemaA, FloatSchemaA):
#                 pass
#
#     def test_valid_combo_including_self_reference(self):
#
#         class EnemyPlayerAndA(DictSchema):
#             a = DateSchema
#
#             class enemyPlayer(DictSchema):
#                 heightCm = IntSchema
#                 _additional_properties = AnyTypeSchema
#
#             _additional_properties = AnyTypeSchema
#
#         class Combo(Player, EnemyPlayerAndA):
#             # we have a self reference where Player.enemyPlayer = Player
#             pass
#
#         """
#         For Combo
#         name is from Player
#         enemyPlayer is from Player + EnemyPlayerAndA
#         a is from EnemyPlayerAndA
#         """
#         self.assertEqual(Combo._property_names, ('a', 'enemyPlayer', 'name'))
#         self.assertEqual(Combo.enemyPlayer.__bases__, (EnemyPlayerAndA.enemyPlayer, Player))
#         """
#         For Combo.enemyPlayer
#         heightCm is from EnemyPlayerAndA.enemyPlayer
#         name is from Player.enemyPlayer
#         enemyPlayer is from Player.enemyPlayer
#         """
#         self.assertEqual(Combo.enemyPlayer._property_names, ('enemyPlayer', 'heightCm', 'name'))


if __name__ == '__main__':
    unittest.main()
