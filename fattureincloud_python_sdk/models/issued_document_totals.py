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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat


class IssuedDocumentTotals(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    amount_net: Optional[StrictFloat] = Field(None, description="Total net amount.")
    amount_rivalsa: Optional[StrictFloat] = Field(None, description="Rivalsa amount.")
    amount_net_with_rivalsa: Optional[StrictFloat] = Field(
        None, description="Net amount with rivalsa."
    )
    amount_cassa: Optional[StrictFloat] = Field(None, description="Cassa amount.")
    taxable_amount: Optional[StrictFloat] = Field(None, description="Taxable amount.")
    not_taxable_amount: Optional[StrictFloat] = Field(
        None, description="Not taxable amount."
    )
    amount_vat: Optional[StrictFloat] = Field(None, description="Total vat amount.")
    amount_gross: Optional[StrictFloat] = Field(
        None, description="Total grosas amount."
    )
    taxable_amount_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Taxable withholding tax amount."
    )
    amount_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Withholding tax amount."
    )
    taxable_amount_other_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Other withholding tax taxable amount."
    )
    amount_other_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Other withholding tax amount."
    )
    stamp_duty: Optional[StrictFloat] = Field(
        None, description="Stamp duty value [0 if not present]."
    )
    amount_due: Optional[StrictFloat] = Field(None, description="Total amount due.")
    is_enasarco_maximal_exceeded: Optional[StrictBool] = None
    payments_sum: Optional[StrictFloat] = Field(None, description="Payments sum.")
    vat_list: Optional[Dict[str, Dict[str, Any]]] = None
    __properties = [
        "amount_net",
        "amount_rivalsa",
        "amount_net_with_rivalsa",
        "amount_cassa",
        "taxable_amount",
        "not_taxable_amount",
        "amount_vat",
        "amount_gross",
        "taxable_amount_withholding_tax",
        "amount_withholding_tax",
        "taxable_amount_other_withholding_tax",
        "amount_other_withholding_tax",
        "stamp_duty",
        "amount_due",
        "is_enasarco_maximal_exceeded",
        "payments_sum",
        "vat_list",
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
    def from_json(cls, json_str: str) -> IssuedDocumentTotals:
        """Create an instance of IssuedDocumentTotals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in vat_list (dict)
        _field_dict = {}
        if self.vat_list:
            for _key in self.vat_list:
                if self.vat_list[_key]:
                    _field_dict[_key] = self.vat_list[_key].to_dict()
            _dict["vat_list"] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssuedDocumentTotals:
        """Create an instance of IssuedDocumentTotals from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssuedDocumentTotals.parse_obj(obj)

        _obj = IssuedDocumentTotals.parse_obj(
            {
                "amount_net": float(obj.get("amount_net"))
                if obj.get("amount_net") is not None
                else None,
                "amount_rivalsa": float(obj.get("amount_rivalsa"))
                if obj.get("amount_rivalsa") is not None
                else None,
                "amount_net_with_rivalsa": float(obj.get("amount_net_with_rivalsa"))
                if obj.get("amount_net_with_rivalsa") is not None
                else None,
                "amount_cassa": float(obj.get("amount_cassa"))
                if obj.get("amount_cassa") is not None
                else None,
                "taxable_amount": float(obj.get("taxable_amount"))
                if obj.get("taxable_amount") is not None
                else None,
                "not_taxable_amount": float(obj.get("not_taxable_amount"))
                if obj.get("not_taxable_amount") is not None
                else None,
                "amount_vat": float(obj.get("amount_vat"))
                if obj.get("amount_vat") is not None
                else None,
                "amount_gross": float(obj.get("amount_gross"))
                if obj.get("amount_gross") is not None
                else None,
                "taxable_amount_withholding_tax": float(
                    obj.get("taxable_amount_withholding_tax")
                )
                if obj.get("taxable_amount_withholding_tax") is not None
                else None,
                "amount_withholding_tax": float(obj.get("amount_withholding_tax"))
                if obj.get("amount_withholding_tax") is not None
                else None,
                "taxable_amount_other_withholding_tax": float(
                    obj.get("taxable_amount_other_withholding_tax")
                )
                if obj.get("taxable_amount_other_withholding_tax") is not None
                else None,
                "amount_other_withholding_tax": float(
                    obj.get("amount_other_withholding_tax")
                )
                if obj.get("amount_other_withholding_tax") is not None
                else None,
                "stamp_duty": float(obj.get("stamp_duty"))
                if obj.get("stamp_duty") is not None
                else None,
                "amount_due": float(obj.get("amount_due"))
                if obj.get("amount_due") is not None
                else None,
                "is_enasarco_maximal_exceeded": obj.get("is_enasarco_maximal_exceeded")
                if obj.get("is_enasarco_maximal_exceeded") is not None
                else None,
                "payments_sum": float(obj.get("payments_sum"))
                if obj.get("payments_sum") is not None
                else None,
                "vat_list": dict(
                    (_k, Dict[str, VatItem].from_dict(_v))
                    for _k, _v in obj.get("vat_list").items()
                )
                if obj.get("vat_list") is not None
                else None,
            }
        )
        return _obj
