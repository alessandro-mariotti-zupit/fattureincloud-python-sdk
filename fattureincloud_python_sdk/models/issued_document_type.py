# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.28
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg


class IssuedDocumentType(str, Enum):
    """
    Issued document type.
    """

    """
    allowed enum values
    """
    INVOICE = "invoice"
    QUOTE = "quote"
    PROFORMA = "proforma"
    RECEIPT = "receipt"
    DELIVERY_NOTE = "delivery_note"
    CREDIT_NOTE = "credit_note"
    ORDER = "order"
    WORK_REPORT = "work_report"
    SUPPLIER_ORDER = "supplier_order"
    SELF_OWN_INVOICE = "self_own_invoice"
    SELF_SUPPLIER_INVOICE = "self_supplier_invoice"
