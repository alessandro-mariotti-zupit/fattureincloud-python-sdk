# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt

from typing import Optional

from fattureincloud_python_sdk.models.get_e_invoice_rejection_reason_response import (
    GetEInvoiceRejectionReasonResponse,
)
from fattureincloud_python_sdk.models.send_e_invoice_request import SendEInvoiceRequest
from fattureincloud_python_sdk.models.send_e_invoice_response import (
    SendEInvoiceResponse,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response import (
    VerifyEInvoiceXmlResponse,
)

from fattureincloud_python_sdk.api_client import ApiClient
from fattureincloud_python_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class IssuedEInvoicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_e_invoice_rejection_reason(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        **kwargs
    ) -> GetEInvoiceRejectionReasonResponse:  # noqa: E501
        """Get e-invoice rejection reason  # noqa: E501

        Get e-invoice rejection reason  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_rejection_reason(company_id, document_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetEInvoiceRejectionReasonResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.get_e_invoice_rejection_reason_with_http_info(
            company_id, document_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_e_invoice_rejection_reason_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        **kwargs
    ):  # noqa: E501
        """Get e-invoice rejection reason  # noqa: E501

        Get e-invoice rejection reason  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_rejection_reason_with_http_info(company_id, document_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetEInvoiceRejectionReasonResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "document_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_e_invoice_rejection_reason" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]
        if _params["document_id"]:
            _path_params["document_id"] = _params["document_id"]

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "GetEInvoiceRejectionReasonResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/issued_documents/{document_id}/e_invoice/error_reason",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_e_invoice_xml(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        include_attachment: Annotated[
            Optional[StrictBool],
            Field(description="Include the attachment to the XML e-invoice."),
        ] = None,
        **kwargs
    ) -> str:  # noqa: E501
        """Get e-invoice XML  # noqa: E501

        Downloads the e-invoice in XML format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_xml(company_id, document_id, include_attachment, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param include_attachment: Include the attachment to the XML e-invoice.
        :type include_attachment: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs["_return_http_data_only"] = True
        return self.get_e_invoice_xml_with_http_info(
            company_id, document_id, include_attachment, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_e_invoice_xml_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        include_attachment: Annotated[
            Optional[StrictBool],
            Field(description="Include the attachment to the XML e-invoice."),
        ] = None,
        **kwargs
    ):  # noqa: E501
        """Get e-invoice XML  # noqa: E501

        Downloads the e-invoice in XML format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_e_invoice_xml_with_http_info(company_id, document_id, include_attachment, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param include_attachment: Include the attachment to the XML e-invoice.
        :type include_attachment: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "document_id", "include_attachment"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_e_invoice_xml" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]
        if _params["document_id"]:
            _path_params["document_id"] = _params["document_id"]

        # process the query parameters
        _query_params = []
        if _params.get("include_attachment") is not None:  # noqa: E501
            _query_params.append(("include_attachment", _params["include_attachment"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["text/xml"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "str",
            "401": None,
            "404": None,
        }

        return self.api_client.call_api(
            "/c/{company_id}/issued_documents/{document_id}/e_invoice/xml",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def send_e_invoice(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        send_e_invoice_request: Optional[SendEInvoiceRequest] = None,
        **kwargs
    ) -> SendEInvoiceResponse:  # noqa: E501
        """Send the e-invoice  # noqa: E501

        Sends the e-invoice to SDI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_e_invoice(company_id, document_id, send_e_invoice_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param send_e_invoice_request:
        :type send_e_invoice_request: SendEInvoiceRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SendEInvoiceResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.send_e_invoice_with_http_info(
            company_id, document_id, send_e_invoice_request, **kwargs
        )  # noqa: E501

    @validate_arguments
    def send_e_invoice_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        send_e_invoice_request: Optional[SendEInvoiceRequest] = None,
        **kwargs
    ):  # noqa: E501
        """Send the e-invoice  # noqa: E501

        Sends the e-invoice to SDI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_e_invoice_with_http_info(company_id, document_id, send_e_invoice_request, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param send_e_invoice_request:
        :type send_e_invoice_request: SendEInvoiceRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SendEInvoiceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "document_id", "send_e_invoice_request"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_e_invoice" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]
        if _params["document_id"]:
            _path_params["document_id"] = _params["document_id"]

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params["send_e_invoice_request"]:
            _body_params = _params["send_e_invoice_request"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "SendEInvoiceResponse",
            "401": None,
            "404": None,
        }

        return self.api_client.call_api(
            "/c/{company_id}/issued_documents/{document_id}/e_invoice/send",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def verify_e_invoice_xml(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        **kwargs
    ) -> VerifyEInvoiceXmlResponse:  # noqa: E501
        """Verify e-invoice XML  # noqa: E501

        Verifies the e-invoice XML format. Checks if all of the mandatory fields are filled and compliant to the right format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_e_invoice_xml(company_id, document_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VerifyEInvoiceXmlResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.verify_e_invoice_xml_with_http_info(
            company_id, document_id, **kwargs
        )  # noqa: E501

    @validate_arguments
    def verify_e_invoice_xml_with_http_info(
        self,
        company_id: Annotated[
            StrictInt, Field(..., description="The ID of the company.")
        ],
        document_id: Annotated[
            StrictInt, Field(..., description="The ID of the document.")
        ],
        **kwargs
    ):  # noqa: E501
        """Verify e-invoice XML  # noqa: E501

        Verifies the e-invoice XML format. Checks if all of the mandatory fields are filled and compliant to the right format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_e_invoice_xml_with_http_info(company_id, document_id, async_req=True)
        >>> result = thread.get()

        :param company_id: The ID of the company. (required)
        :type company_id: int
        :param document_id: The ID of the document. (required)
        :type document_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VerifyEInvoiceXmlResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["company_id", "document_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_e_invoice_xml" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["company_id"]:
            _path_params["company_id"] = _params["company_id"]
        if _params["document_id"]:
            _path_params["document_id"] = _params["document_id"]

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["OAuth2AuthenticationCodeFlow"]  # noqa: E501

        _response_types_map = {
            "200": "VerifyEInvoiceXmlResponse",
            "401": None,
            "404": None,
            "422": "VerifyEInvoiceXmlErrorResponse",
        }

        return self.api_client.call_api(
            "/c/{company_id}/issued_documents/{document_id}/e_invoice/xml_verify",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
