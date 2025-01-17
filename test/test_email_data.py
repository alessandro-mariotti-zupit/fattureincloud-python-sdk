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
from fattureincloud_python_sdk.models.email_data_default_sender_email import (
    EmailDataDefaultSenderEmail,
)
from fattureincloud_python_sdk.models.sender_email import SenderEmail

globals()["EmailDataDefaultSenderEmail"] = EmailDataDefaultSenderEmail
globals()["SenderEmail"] = SenderEmail
from fattureincloud_python_sdk.models.email_data import EmailData


class TestEmailData(unittest.TestCase):
    """EmailData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmailData(self):
        """Test EmailData"""
        model = EmailData(
            recipient_email="info@mail.com",
            cc_email="default@mail.com",
            subject="important",
            body="you won 13 billion indian rupies",
            document_exists=False,
            delivery_note_exists=False,
            attachment_exists=False,
            accompanying_invoice_exists=False,
            default_attach_pdf=False,
            default_sender_email=EmailDataDefaultSenderEmail(
                id=1, email="ex.email@provider.co"
            ),
            sender_emails_list=[SenderEmail(id=1, email="ex.email@provider.co")],
        )
        expected_json = '{"recipient_email": "info@mail.com", "default_sender_email": {"id": 1, "email": "ex.email@provider.co"}, "sender_emails_list": [{"id": 1, "email": "ex.email@provider.co"}], "cc_email": "default@mail.com", "subject": "important", "body": "you won 13 billion indian rupies", "document_exists": false, "delivery_note_exists": false, "attachment_exists": false, "accompanying_invoice_exists": false, "default_attach_pdf": false}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
