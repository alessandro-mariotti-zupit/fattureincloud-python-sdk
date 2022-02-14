"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""

import datetime
import functions
import unittest
import unittest.mock
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import RESTResponse
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.api.cashbook_api import CashbookApi
from fattureincloud_python_sdk.model import create_cashbook_entry_response
from fattureincloud_python_sdk.model.cashbook_entry_document import CashbookEntryDocument
from fattureincloud_python_sdk.model.cashbook_entry import CashbookEntry
from fattureincloud_python_sdk.model.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.model.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.model.create_cashbook_entry_response import CreateCashbookEntryResponse
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.get_cashbook_entry_response import GetCashbookEntryResponse
from fattureincloud_python_sdk.model import get_cashbook_entry_response
from fattureincloud_python_sdk.model.cashbook_entry import CashbookEntry
from fattureincloud_python_sdk.model.list_cashbook_entries_response import ListCashbookEntriesResponse
from fattureincloud_python_sdk.model import list_cashbook_entries_response
from fattureincloud_python_sdk.model.modify_cashbook_entry_response import ModifyCashbookEntryResponse  # noqa: E501


class TestCashbookApi(unittest.TestCase):
    """CashbookApi unit test stubs"""

    def setUp(self):
        self.api = CashbookApi()

    def tearDown(self):
        pass

    def test_create_cashbook_entry(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "path": "/path", "type": "doc"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreateCashbookEntryResponse( data=CashbookEntry( id="2", date=datetime.datetime.strptime("2022-02-02", '%Y-%m-%d').date(), description="description", kind=CashbookEntryKind("cashbook"), type=CashbookEntryType("in"), entity_name="name", document=CashbookEntryDocument( id=1, path="/path", type="doc" ), amount_in=10.0, payment_account_in=PaymentAccount( id=1, name="banca" ) ) )
        actual = self.api.create_cashbook_entry(2)
        actual.data.id = "2"
        assert actual == expected

    def test_delete_cashbook_entry(self):
        resp = {
            'status': 200,
            'data': b'{}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.DELETE = unittest.mock.MagicMock(return_value = mock_resp)
        actual = self.api.delete_cashbook_entry(2, 12345)
        assert actual == None

    def test_get_cashbook_entry(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "path": "/path", "type": "doc"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetCashbookEntryResponse( data=CashbookEntry( id="2", date=datetime.datetime.strptime("2022-02-02", '%Y-%m-%d').date(), description="description", kind=CashbookEntryKind("cashbook"), type=CashbookEntryType("in"), entity_name="name", document=CashbookEntryDocument( id=1, path="/path", type="doc" ), amount_in=10.0, payment_account_in=PaymentAccount( id=1, name="banca" ) ) )
        actual = self.api.get_cashbook_entry(2, 12345)
        actual.data.id = "2"
        assert actual == expected

    def test_list_cashbook_entries(self):
        resp = {
            'status': 200,
            'data': b'{"data": [{"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "path": "/path", "type": "doc"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ListCashbookEntriesResponse( data=[ CashbookEntry( id="2", date=datetime.datetime.strptime("2022-02-02", '%Y-%m-%d').date(), description="description", kind=CashbookEntryKind("cashbook"), type=CashbookEntryType("in"), entity_name="name", document=CashbookEntryDocument( id=1, path="/path", type="doc" ), amount_in=10.0, payment_account_in=PaymentAccount( id=1, name="banca" ), ) ], current_page=10, first_page_url="http://url.com", last_page=10, last_page_url="http://url.com", next_page_url="http://url.com", path="http://url.com", per_page=10, prev_page_url="http://url.com", to=10, total=10 )
        actual = self.api.list_cashbook_entries(2, "2020-10-10", "2022-10-10")
        actual.data[0].id = "2"
        assert actual == expected

    def test_modify_cashbook_entry(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "path": "/path", "type": "doc"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyCashbookEntryResponse( data=CashbookEntry( id="2", date=datetime.datetime.strptime("2022-02-02", '%Y-%m-%d').date(), description="description", kind=CashbookEntryKind("cashbook"), type=CashbookEntryType("in"), entity_name="name", document=CashbookEntryDocument( id=1, path="/path", type="doc" ), amount_in=10.0, payment_account_in=PaymentAccount( id=1, name="banca" ) ) )
        actual = self.api.modify_cashbook_entry(2, 12345)
        actual.data.id = "2"
        assert actual == expected


if __name__ == '__main__':
    unittest.main()