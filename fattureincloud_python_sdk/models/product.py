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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.vat_type import VatType


class Product(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Unique identifier.")
    name: Optional[StrictStr] = Field(None, description="Product name.")
    code: Optional[StrictStr] = Field(None, description="Product code.")
    net_price: Optional[StrictFloat] = Field(
        None,
        description="Net sale price (used if use_gross_price is false, otherwise it's competed automatically).",
    )
    gross_price: Optional[StrictFloat] = Field(
        None,
        description="Gross sale price (used if use_gross_price is false, otherwise it's competed automatically).",
    )
    use_gross_price: Optional[StrictBool] = Field(
        None, description="Determine which price to use for calculations."
    )
    default_vat: Optional[VatType] = None
    net_cost: Optional[StrictFloat] = Field(
        None, description="Net cost of the product (used for received documents)."
    )
    measure: Optional[StrictStr] = Field(None, description="Unit of measure.")
    description: Optional[StrictStr] = Field(None, description="Product description.")
    category: Optional[StrictStr] = Field(None, description="Product category.")
    notes: Optional[StrictStr] = Field(None, description="Extra notes.")
    in_stock: Optional[StrictBool] = Field(
        None, description="Determine if the product is in stock."
    )
    stock_initial: Optional[StrictFloat] = Field(
        None, description="Product initial stock."
    )
    stock_current: Optional[StrictFloat] = Field(
        None, description="[Read Only] Product current stock."
    )
    average_cost: Optional[StrictFloat] = Field(
        None, description="Product average cost."
    )
    average_price: Optional[StrictFloat] = Field(
        None, description="Product average price."
    )
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties = [
        "id",
        "name",
        "code",
        "net_price",
        "gross_price",
        "use_gross_price",
        "default_vat",
        "net_cost",
        "measure",
        "description",
        "category",
        "notes",
        "in_stock",
        "stock_initial",
        "stock_current",
        "average_cost",
        "average_price",
        "created_at",
        "updated_at",
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
    def from_json(cls, json_str: str) -> Product:
        """Create an instance of Product from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "stock_current",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of default_vat
        if self.default_vat:
            _dict["default_vat"] = self.default_vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Product:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Product.parse_obj(obj)

        _obj = Product.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "code": obj.get("code") if obj.get("code") is not None else None,
                "net_price": float(obj.get("net_price"))
                if obj.get("net_price") is not None
                else None,
                "gross_price": float(obj.get("gross_price"))
                if obj.get("gross_price") is not None
                else None,
                "use_gross_price": obj.get("use_gross_price")
                if obj.get("use_gross_price") is not None
                else None,
                "default_vat": VatType.from_dict(obj.get("default_vat"))
                if obj.get("default_vat") is not None
                else None,
                "net_cost": float(obj.get("net_cost"))
                if obj.get("net_cost") is not None
                else None,
                "measure": obj.get("measure")
                if obj.get("measure") is not None
                else None,
                "description": obj.get("description")
                if obj.get("description") is not None
                else None,
                "category": obj.get("category")
                if obj.get("category") is not None
                else None,
                "notes": obj.get("notes") if obj.get("notes") is not None else None,
                "in_stock": obj.get("in_stock")
                if obj.get("in_stock") is not None
                else None,
                "stock_initial": float(obj.get("stock_initial"))
                if obj.get("stock_initial") is not None
                else None,
                "stock_current": float(obj.get("stock_current"))
                if obj.get("stock_current") is not None
                else None,
                "average_cost": float(obj.get("average_cost"))
                if obj.get("average_cost") is not None
                else None,
                "average_price": float(obj.get("average_price"))
                if obj.get("average_price") is not None
                else None,
                "created_at": obj.get("created_at")
                if obj.get("created_at") is not None
                else None,
                "updated_at": obj.get("updated_at")
                if obj.get("updated_at") is not None
                else None,
            }
        )
        return _obj
