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
from pydantic import BaseModel, Field, StrictBool


class EmailScheduleInclude(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    document: Optional[StrictBool] = Field(
        None,
        description="If set to true, the email will have a button to view the document",
    )
    delivery_note: Optional[StrictBool] = Field(
        None,
        description="If set to true, the email will have a button to view the delivery note",
    )
    attachment: Optional[StrictBool] = Field(
        None,
        description="If set to true, the email will have a button to view the attachment",
    )
    accompanying_invoice: Optional[StrictBool] = Field(
        None,
        description="If set to true, the email will have a button to view the accompanying invoice",
    )
    __properties = ["document", "delivery_note", "attachment", "accompanying_invoice"]

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
    def from_json(cls, json_str: str) -> EmailScheduleInclude:
        """Create an instance of EmailScheduleInclude from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmailScheduleInclude:
        """Create an instance of EmailScheduleInclude from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EmailScheduleInclude.parse_obj(obj)

        _obj = EmailScheduleInclude.parse_obj(
            {
                "document": obj.get("document")
                if obj.get("document") is not None
                else None,
                "delivery_note": obj.get("delivery_note")
                if obj.get("delivery_note") is not None
                else None,
                "attachment": obj.get("attachment")
                if obj.get("attachment") is not None
                else None,
                "accompanying_invoice": obj.get("accompanying_invoice")
                if obj.get("accompanying_invoice") is not None
                else None,
            }
        )
        return _obj
