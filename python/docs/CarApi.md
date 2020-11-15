# swagger_client.CarApi

All URIs are relative to *https://virtserver.swaggerhub.com/AutoRoll/AutoRolll/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_car**](CarApi.md#add_car) | **POST** /car | Add a new car to the store
[**delete_car**](CarApi.md#delete_car) | **DELETE** /car/{carId} | Deletes a car
[**find_cars_by_status**](CarApi.md#find_cars_by_status) | **GET** /car/findByStatus | Finds cars by status
[**get_car_by_id**](CarApi.md#get_car_by_id) | **GET** /car/{carId} | Find car by ID
[**update_car**](CarApi.md#update_car) | **PUT** /car | Update an existing car
[**update_car_with_form**](CarApi.md#update_car_with_form) | **POST** /car/{carId} | Updates a car in the store with form data
[**upload_file**](CarApi.md#upload_file) | **POST** /car/{carId}/uploadImage | uploads an image

# **add_car**
> add_car(body)

Add a new car to the store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
body = swagger_client.Car() # Car | Car object that needs to be added to the store

try:
    # Add a new car to the store
    api_instance.add_car(body)
except ApiException as e:
    print("Exception when calling CarApi->add_car: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Car**](Car.md)| Car object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_car**
> delete_car(car_id, api_key=api_key)

Deletes a car

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
car_id = 789 # int | Car id to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a car
    api_instance.delete_car(car_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling CarApi->delete_car: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| Car id to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_cars_by_status**
> list[Car] find_cars_by_status(status)

Finds cars by status

Multiple status values can be provided with comma separated strings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
status = ['status_example'] # list[str] | Status values that need to be considered for filter

try:
    # Finds cars by status
    api_response = api_instance.find_cars_by_status(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->find_cars_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Status values that need to be considered for filter | 

### Return type

[**list[Car]**](Car.md)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_by_id**
> Car get_car_by_id(car_id)

Find car by ID

Returns a single car

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
car_id = 789 # int | ID of car to return

try:
    # Find car by ID
    api_response = api_instance.get_car_by_id(car_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->get_car_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of car to return | 

### Return type

[**Car**](Car.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_car**
> update_car(body)

Update an existing car

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
body = swagger_client.Car() # Car | Car object that needs to be added to the store

try:
    # Update an existing car
    api_instance.update_car(body)
except ApiException as e:
    print("Exception when calling CarApi->update_car: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Car**](Car.md)| Car object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_car_with_form**
> update_car_with_form(car_id, name=name, status=status)

Updates a car in the store with form data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
car_id = 789 # int | ID of car that needs to be updated
name = 'name_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    # Updates a car in the store with form data
    api_instance.update_car_with_form(car_id, name=name, status=status)
except ApiException as e:
    print("Exception when calling CarApi->update_car_with_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of car that needs to be updated | 
 **name** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ApiResponse upload_file(car_id, body=body)

uploads an image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: carstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.CarApi(swagger_client.ApiClient(configuration))
car_id = 789 # int | ID of car to update
body = swagger_client.Object() # Object |  (optional)

try:
    # uploads an image
    api_response = api_instance.upload_file(car_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| ID of car to update | 
 **body** | **Object**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[carstore_auth](../README.md#carstore_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

