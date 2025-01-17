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
from fattureincloud_python_sdk.models.issued_document_extra_data import (
    IssuedDocumentExtraData,
)


class TestIssuedDocumentExtraData(unittest.TestCase):
    """IssuedDocumentExtraData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssuedDocumentExtraData(self):
        """Test IssuedDocumentExtraData"""
        model = IssuedDocumentExtraData(
            show_sofort_button=True,
            multifatture_sent=1,
            ts_communication=True,
            ts_flag_tipo_spesa=3.14,
            ts_pagamento_tracciato=True,
            ts_tipo_spesa="ts_tipo_spesa_example",
            ts_opposizione=True,
            ts_status=1,
            ts_file_id="ts_file_id_example",
            ts_sent_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
            ts_full_amount=True,
            imported_by="imported_by_example",
            ts_single_sending=True,
        )
        expected_json = '{"show_sofort_button": true, "multifatture_sent": 1, "ts_communication": true, "ts_flag_tipo_spesa": 3.14, "ts_pagamento_tracciato": true, "ts_tipo_spesa": "ts_tipo_spesa_example", "ts_opposizione": true, "ts_status": 1, "ts_file_id": "ts_file_id_example", "ts_sent_date": "2022-01-01", "ts_full_amount": true, "imported_by": "imported_by_example", "ts_single_sending": true}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
