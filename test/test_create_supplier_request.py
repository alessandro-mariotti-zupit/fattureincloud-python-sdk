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

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.supplier import Supplier
from fattureincloud_python_sdk.models.supplier_type import SupplierType

globals()["Supplier"] = Supplier
from fattureincloud_python_sdk.models.create_supplier_request import (
    CreateSupplierRequest,
)


class TestCreateSupplierRequest(unittest.TestCase):
    """CreateSupplierRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateSupplierRequest(self):
        """Test CreateSupplierRequest"""
        model = CreateSupplierRequest(
            data=Supplier(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=SupplierType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            )
        )
        expected_json = '{"data": {"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
