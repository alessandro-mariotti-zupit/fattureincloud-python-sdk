# Permissions



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fic_situation** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_clients** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_suppliers** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_products** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_issued_documents** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_received_documents** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_receipts** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_calendar** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_archive** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_taxes** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_stock** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_cashbook** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_settings** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_emails** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_export** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_import_bankstatements** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_import_clients_suppliers** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_import_issued_documents** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_import_products** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_recurring** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_riba** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**dic_employees** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**dic_settings** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**dic_timesheet** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**fic_issued_documents_detailed** | [**PermissionsFicIssuedDocumentsDetailed**](PermissionsFicIssuedDocumentsDetailed.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.permissions import Permissions

# TODO update the JSON string below
json = "{}"
# create an instance of Permissions from a JSON string
permissions_instance = Permissions.from_json(json)
# print the JSON string representation of the object
print Permissions.to_json()

# convert the object into a dict
permissions_dict = permissions_instance.to_dict()
# create an instance of Permissions from a dict
permissions_form_dict = permissions.from_dict(permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


