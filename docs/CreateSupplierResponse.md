# CreateSupplierResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_supplier_response import CreateSupplierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupplierResponse from a JSON string
create_supplier_response_instance = CreateSupplierResponse.from_json(json)
# print the JSON string representation of the object
print CreateSupplierResponse.to_json()

# convert the object into a dict
create_supplier_response_dict = create_supplier_response_instance.to_dict()
# create an instance of CreateSupplierResponse from a dict
create_supplier_response_form_dict = create_supplier_response.from_dict(create_supplier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


