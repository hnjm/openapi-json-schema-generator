# coding: utf-8
"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import typing

from petstore_api import server


@dataclasses.dataclass
class Server2(server.Server):
    '''
    staging server with no variables
    '''
    _url: str = "https://localhost:8080"
