# swagger_client.AdminApi

All URIs are relative to *https://virtserver.swaggerhub.com/AutoRoll/AutoRolll/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin**](AdminApi.md#create_admin) | **POST** /admin | Create admin
[**create_admins_with_list_input**](AdminApi.md#create_admins_with_list_input) | **POST** /admin/createWithList | Creates list of adminS with given input array
[**delete_admin**](AdminApi.md#delete_admin) | **DELETE** /admin/{username} | Delete user
[**get_admin_by_name**](AdminApi.md#get_admin_by_name) | **GET** /admin/{username} | Get admin by username
[**login_admin**](AdminApi.md#login_admin) | **GET** /admin/login | Logs admin into the system
[**logout_admin**](AdminApi.md#logout_admin) | **GET** /admin/logout | Logs out current logged in admin session
[**update_admin**](AdminApi.md#update_admin) | **PUT** /admin/{username} | Updated admin

# **create_admin**
> create_admin(body)

Create admin

This can only be done by the logged in admin.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.Admin() # Admin | Created admin object

try:
    # Create admin
    api_instance.create_admin(body)
except ApiException as e:
    print("Exception when calling AdminApi->create_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Admin**](Admin.md)| Created admin object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_admins_with_list_input**
> create_admins_with_list_input(body)

Creates list of adminS with given input array

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = [swagger_client.Admin()] # list[Admin] | List of admin object

try:
    # Creates list of adminS with given input array
    api_instance.create_admins_with_list_input(body)
except ApiException as e:
    print("Exception when calling AdminApi->create_admins_with_list_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Admin]**](Admin.md)| List of admin object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin**
> delete_admin(username)

Delete user

This can only be done by the logged in admin.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
username = 'username_example' # str | The name that needs to be deleted

try:
    # Delete user
    api_instance.delete_admin(username)
except ApiException as e:
    print("Exception when calling AdminApi->delete_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_by_name**
> Admin get_admin_by_name(username)

Get admin by username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
username = 'username_example' # str | The name that needs to be fetched. Use user1 for testing.

try:
    # Get admin by username
    api_response = api_instance.get_admin_by_name(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_admin_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be fetched. Use user1 for testing. | 

### Return type

[**Admin**](Admin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_admin**
> str login_admin(username, password)

Logs admin into the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
username = 'username_example' # str | The admin name for login
password = 'password_example' # str | The password for login in clear text

try:
    # Logs admin into the system
    api_response = api_instance.login_admin(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->login_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The admin name for login | 
 **password** | **str**| The password for login in clear text | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_admin**
> logout_admin()

Logs out current logged in admin session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()

try:
    # Logs out current logged in admin session
    api_instance.logout_admin()
except ApiException as e:
    print("Exception when calling AdminApi->logout_admin: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin**
> update_admin(body, username)

Updated admin

This can only be done by the logged in admin.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
body = swagger_client.Admin() # Admin | Updated admin object
username = 'username_example' # str | name that need to be updated

try:
    # Updated admin
    api_instance.update_admin(body, username)
except ApiException as e:
    print("Exception when calling AdminApi->update_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Admin**](Admin.md)| Updated admin object | 
 **username** | **str**| name that need to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

