# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from fattureincloud_python_sdk.models.event_type import EventType


class WebhooksSubscription(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictStr] = Field(None, description="Unique identifier")
    sink: Optional[StrictStr] = Field(None, description="Webhooks callback uri.")
    verified: Optional[StrictBool] = Field(
        None,
        description="[Read Only] True if the webhooks subscription has been verified.",
    )
    types: Optional[conlist(EventType)] = Field(
        None, description="Webhooks events types."
    )
    __properties = ["id", "sink", "verified", "types"]

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
    def from_json(cls, json_str: str) -> WebhooksSubscription:
        """Create an instance of WebhooksSubscription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhooksSubscription:
        """Create an instance of WebhooksSubscription from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WebhooksSubscription.parse_obj(obj)

        _obj = WebhooksSubscription.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "sink": obj.get("sink") if obj.get("sink") is not None else None,
                "verified": obj.get("verified")
                if obj.get("verified") is not None
                else None,
                "types": obj.get("types"),
            }
        )
        return _obj