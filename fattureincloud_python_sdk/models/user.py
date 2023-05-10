# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.28
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class User(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="User identifier.")
    name: Optional[StrictStr] = Field(None, description="Full name of the user.")
    first_name: Optional[StrictStr] = Field(None, description="First name of the user.")
    last_name: Optional[StrictStr] = Field(None, description="Last name of the user.")
    email: Optional[StrictStr] = Field(None, description="Email of the user.")
    hash: Optional[StrictStr] = None
    picture: Optional[StrictStr] = Field(None, description="Picture of the user.")
    __properties = ["id", "name", "first_name", "last_name", "email", "hash", "picture"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return User.parse_obj(obj)

        _obj = User.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "first_name": obj.get("first_name")
                if obj.get("first_name") is not None
                else None,
                "last_name": obj.get("last_name")
                if obj.get("last_name") is not None
                else None,
                "email": obj.get("email") if obj.get("email") is not None else None,
                "hash": obj.get("hash") if obj.get("hash") is not None else None,
                "picture": obj.get("picture")
                if obj.get("picture") is not None
                else None,
            }
        )
        return _obj
