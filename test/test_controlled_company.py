"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
from multiprocessing import connection
import sys
import unittest

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.company_type import CompanyType

globals()["CompanyType"] = CompanyType
from fattureincloud_python_sdk.models.controlled_company import ControlledCompany


class TestControlledCompany(unittest.TestCase):
    """ControlledCompany unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testControlledCompany(self):
        """Test ControlledCompany"""
        model = ControlledCompany(
            id=1,
            name="mario srl",
            type=CompanyType("company"),
            access_token="zpaiefapfjaojf56546456456",
            connection_id=2.0,
            tax_code="0123456789",
        )
        expected_json = '{"id": 1, "name": "mario srl", "type": "company", "access_token": "zpaiefapfjaojf56546456456", "connection_id": 2.0, "tax_code": "0123456789"}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
