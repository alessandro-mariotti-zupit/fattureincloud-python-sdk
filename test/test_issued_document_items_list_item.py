"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.vat_type import VatType
from functions import json_serial
from functions import create_from_json

globals()["VatType"] = VatType
from fattureincloud_python_sdk.models.issued_document_items_list_item import (
    IssuedDocumentItemsListItem,
)


class TestIssuedDocumentItemsListItem(unittest.TestCase):
    """IssuedDocumentItemsListItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssuedDocumentItemsListItem(self):
        """Test IssuedDocumentItemsListItem"""
        model = IssuedDocumentItemsListItem(
            product_id=1234,
            code="239874892374982",
            name="Water bottle",
            description="description_example",
            qty=3.14,
            measure="measure_example",
            net_price=1.23,
            gross_price=1.45,
            vat=VatType(
                id=1,
                value=22.0,
                description="Non imponibile art. 123",
                notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                e_invoice=True,
                ei_type="2",
                ei_description="ei_description_example",
                is_disabled=True,
            ),
            not_taxable=False,
            apply_withholding_taxes=True,
            discount=0.0,
            discount_highlight=False,
            in_dn=True,
            stock=True,
            ei_raw={},
        )
        expected_json = '{"product_id": 1234, "code": "239874892374982", "name": "Water bottle", "description": "description_example", "qty": 3.14, "measure": "measure_example", "net_price": 1.23, "gross_price": 1.45, "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "not_taxable": false, "apply_withholding_taxes": true, "discount": 0.0, "discount_highlight": false, "in_dn": true, "stock": true, "ei_raw": {}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
