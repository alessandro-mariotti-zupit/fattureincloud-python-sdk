# fattureincloud_python_sdk.IssuedEInvoicesApi

All URIs are relative to *https://api-v2.fattureincloud.it*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_e_invoice_rejection_reason**](IssuedEInvoicesApi.md#get_e_invoice_rejection_reason) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/error_reason | Get e-invoice rejection reason
[**get_e_invoice_xml**](IssuedEInvoicesApi.md#get_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml | Get e-invoice XML
[**send_e_invoice**](IssuedEInvoicesApi.md#send_e_invoice) | **POST** /c/{company_id}/issued_documents/{document_id}/e_invoice/send | Send the e-invoice
[**verify_e_invoice_xml**](IssuedEInvoicesApi.md#verify_e_invoice_xml) | **GET** /c/{company_id}/issued_documents/{document_id}/e_invoice/xml_verify | Verify e-invoice XML


# **get_e_invoice_rejection_reason**
> GetEInvoiceRejectionReasonResponse get_e_invoice_rejection_reason(company_id, document_id)

Get e-invoice rejection reason

Get e-invoice rejection reason

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
from __future__ import print_function
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-v2.fattureincloud.it
# See configuration.py for a list of all supported configuration parameters.
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Get e-invoice rejection reason
        api_response = api_instance.get_e_invoice_rejection_reason(company_id, document_id)
        print("The response of IssuedEInvoicesApi->get_e_invoice_rejection_reason:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedEInvoicesApi->get_e_invoice_rejection_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 

### Return type

[**GetEInvoiceRejectionReasonResponse**](GetEInvoiceRejectionReasonResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_e_invoice_xml**
> str get_e_invoice_xml(company_id, document_id, include_attachment=include_attachment)

Get e-invoice XML

Downloads the e-invoice in XML format.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
from __future__ import print_function
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-v2.fattureincloud.it
# See configuration.py for a list of all supported configuration parameters.
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    include_attachment = True # bool | Include the attachment to the XML e-invoice. (optional)

    try:
        # Get e-invoice XML
        api_response = api_instance.get_e_invoice_xml(company_id, document_id, include_attachment=include_attachment)
        print("The response of IssuedEInvoicesApi->get_e_invoice_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedEInvoicesApi->get_e_invoice_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 
 **include_attachment** | **bool**| Include the attachment to the XML e-invoice. | [optional] 

### Return type

**str**

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_e_invoice**
> SendEInvoiceResponse send_e_invoice(company_id, document_id, send_e_invoice_request=send_e_invoice_request)

Send the e-invoice

Sends the e-invoice to SDI.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
from __future__ import print_function
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-v2.fattureincloud.it
# See configuration.py for a list of all supported configuration parameters.
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.
    send_e_invoice_request = {"data":{"withholding_tax_causal":"causale"}} # SendEInvoiceRequest |  (optional)

    try:
        # Send the e-invoice
        api_response = api_instance.send_e_invoice(company_id, document_id, send_e_invoice_request=send_e_invoice_request)
        print("The response of IssuedEInvoicesApi->send_e_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedEInvoicesApi->send_e_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 
 **send_e_invoice_request** | [**SendEInvoiceRequest**](SendEInvoiceRequest.md)|  | [optional] 

### Return type

[**SendEInvoiceResponse**](SendEInvoiceResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_e_invoice_xml**
> VerifyEInvoiceXmlResponse verify_e_invoice_xml(company_id, document_id)

Verify e-invoice XML

Verifies the e-invoice XML format. Checks if all of the mandatory fields are filled and compliant to the right format.

### Example

* OAuth Authentication (OAuth2AuthenticationCodeFlow):
```python
from __future__ import print_function
import time
import os
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-v2.fattureincloud.it
# See configuration.py for a list of all supported configuration parameters.
configuration = fattureincloud_python_sdk.Configuration(
    host = "https://api-v2.fattureincloud.it"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with fattureincloud_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fattureincloud_python_sdk.IssuedEInvoicesApi(api_client)
    company_id = 12345 # int | The ID of the company.
    document_id = 56 # int | The ID of the document.

    try:
        # Verify e-invoice XML
        api_response = api_instance.verify_e_invoice_xml(company_id, document_id)
        print("The response of IssuedEInvoicesApi->verify_e_invoice_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuedEInvoicesApi->verify_e_invoice_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company. | 
 **document_id** | **int**| The ID of the document. | 

### Return type

[**VerifyEInvoiceXmlResponse**](VerifyEInvoiceXmlResponse.md)

### Authorization

[OAuth2AuthenticationCodeFlow](../README.md#OAuth2AuthenticationCodeFlow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

