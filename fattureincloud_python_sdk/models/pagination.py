# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class Pagination(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    current_page: Optional[StrictInt] = Field(None, description="Current page number.")
    first_page_url: Optional[StrictStr] = Field(None, description="First page url.")
    var_from: Optional[StrictInt] = Field(
        None, alias="from", description="First result of the page."
    )
    last_page: Optional[StrictInt] = Field(None, description="Last page number.")
    last_page_url: Optional[StrictStr] = Field(None, description="Last page url.")
    next_page_url: Optional[StrictStr] = Field(None, description="Next page url")
    path: Optional[StrictStr] = Field(None, description="Request path.")
    per_page: Optional[StrictInt] = Field(
        None, description="Number of result per page."
    )
    prev_page_url: Optional[StrictStr] = Field(None, description="Previous page url.")
    to: Optional[StrictInt] = Field(None, description="Last result of the page.")
    total: Optional[StrictInt] = Field(None, description="Total number of results")
    __properties = [
        "current_page",
        "first_page_url",
        "from",
        "last_page",
        "last_page_url",
        "next_page_url",
        "path",
        "per_page",
        "prev_page_url",
        "to",
        "total",
    ]

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
    def from_json(cls, json_str: str) -> Pagination:
        """Create an instance of Pagination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Pagination:
        """Create an instance of Pagination from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Pagination.parse_obj(obj)

        _obj = Pagination.parse_obj(
            {
                "current_page": obj.get("current_page")
                if obj.get("current_page") is not None
                else None,
                "first_page_url": obj.get("first_page_url")
                if obj.get("first_page_url") is not None
                else None,
                "var_from": obj.get("from") if obj.get("from") is not None else None,
                "last_page": obj.get("last_page")
                if obj.get("last_page") is not None
                else None,
                "last_page_url": obj.get("last_page_url")
                if obj.get("last_page_url") is not None
                else None,
                "next_page_url": obj.get("next_page_url")
                if obj.get("next_page_url") is not None
                else None,
                "path": obj.get("path") if obj.get("path") is not None else None,
                "per_page": obj.get("per_page")
                if obj.get("per_page") is not None
                else None,
                "prev_page_url": obj.get("prev_page_url")
                if obj.get("prev_page_url") is not None
                else None,
                "to": obj.get("to") if obj.get("to") is not None else None,
                "total": obj.get("total") if obj.get("total") is not None else None,
            }
        )
        return _obj
