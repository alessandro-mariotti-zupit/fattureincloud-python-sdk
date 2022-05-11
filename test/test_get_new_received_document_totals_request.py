"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest
import datetime
import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.received_document import ReceivedDocument
from fattureincloud_python_sdk.model.received_document_entity import (
    ReceivedDocumentEntity,
)
from fattureincloud_python_sdk.model.received_document_items_list_item import (
    ReceivedDocumentItemsListItem,
)
from fattureincloud_python_sdk.model.received_document_type import ReceivedDocumentType
from fattureincloud_python_sdk.model.vat_type import VatType

globals()["ReceivedDocument"] = ReceivedDocument
from fattureincloud_python_sdk.model.get_new_received_document_totals_request import (
    GetNewReceivedDocumentTotalsRequest,
)


class TestGetNewReceivedDocumentTotalsRequest(unittest.TestCase):
    """GetNewReceivedDocumentTotalsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetNewReceivedDocumentTotalsRequest(self):
        """Test GetNewReceivedDocumentTotalsRequest"""
        model = GetNewReceivedDocumentTotalsRequest(
            data=ReceivedDocument(
                id=1,
                type=ReceivedDocumentType("expense"),
                entity=ReceivedDocumentEntity(
                    id=1,
                    name="name_example",
                ),
                date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                category="category_example",
                description="description_example",
                amount_net=3.14,
                amount_vat=3.14,
                amount_withholding_tax=3.14,
                amount_other_withholding_tax=3.14,
                amortization=3.14,
                rc_center="rc_center_example",
                invoice_number="invoice_number_example",
                is_marked=True,
                is_detailed=True,
                e_invoice=True,
                tax_deductibility=0.0,
                vat_deductibility=0.0,
                items_list=[
                    ReceivedDocumentItemsListItem(
                        id=1,
                        product_id=1,
                        code="code_example",
                        name="name_example",
                        measure="measure_example",
                        net_price=3.14,
                        category="category_example",
                        qty=3.14,
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
                        stock=3.14,
                    )
                ],
            )
        )
        expected_json = '{"data": {"id": 1, "type": "expense", "entity": {"id": 1, "name": "name_example"}, "date": "2022-01-01", "category": "category_example", "description": "description_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_withholding_tax": 3.14, "amount_other_withholding_tax": 3.14, "amortization": 3.14, "rc_center": "rc_center_example", "invoice_number": "invoice_number_example", "is_marked": true, "is_detailed": true, "e_invoice": true, "tax_deductibility": 0.0, "vat_deductibility": 0.0, "items_list": [{"id": 1, "product_id": 1, "code": "code_example", "name": "name_example", "measure": "measure_example", "net_price": 3.14, "category": "category_example", "qty": 3.14, "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "stock": 3.14}]}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
