# osis_organisation_sdk.EntitesApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/organisation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entities**](EntitesApi.md#get_entities) | **GET** /{organisation_code}/entites/ | 
[**get_entity**](EntitesApi.md#get_entity) | **GET** /{organisation_code}/entites/{uuid} | 
[**get_entity_addresses**](EntitesApi.md#get_entity_addresses) | **GET** /{organisation_code}/entites/{uuid}/addresses | 


# **get_entities**
> PaginatedEntites get_entities(organisation_code)



Return all the entities of the specified organisation

### Example

* Api Key Authentication (Token):
```python
import time
import osis_organisation_sdk
from osis_organisation_sdk.api import entites_api
from osis_organisation_sdk.model.paginated_entites import PaginatedEntites
from osis_organisation_sdk.model.error import Error
from osis_organisation_sdk.model.entite_type_enum import EntiteTypeEnum
from osis_organisation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/organisation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_organisation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/organisation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_organisation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entites_api.EntitesApi(api_client)
    organisation_code = "UCL" # str | 
    entity_type = [
        EntiteTypeEnum("SECTOR"),
    ] # [EntiteTypeEnum] |  (optional)
    search = "search_example" # str |  (optional)
    year = 2020 # int |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    limit = 25 # int | Limit of paginated results (optional)
    offset = 25 # int | Offset of paginated results (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_entities(organisation_code)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_entities(organisation_code, entity_type=entity_type, search=search, year=year, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_code** | **str**|  |
 **entity_type** | [**[EntiteTypeEnum]**](EntiteTypeEnum.md)|  | [optional]
 **search** | **str**|  | [optional]
 **year** | **int**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**PaginatedEntites**](PaginatedEntites.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> Entite get_entity(organisation_code, uuid)



Return the detail of the entity

### Example

* Api Key Authentication (Token):
```python
import time
import osis_organisation_sdk
from osis_organisation_sdk.api import entites_api
from osis_organisation_sdk.model.error import Error
from osis_organisation_sdk.model.entite import Entite
from osis_organisation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/organisation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_organisation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/organisation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_organisation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entites_api.EntitesApi(api_client)
    organisation_code = "UCL" # str | 
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_entity(organisation_code, uuid)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_entity(organisation_code, uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_code** | **str**|  |
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Entite**](Entite.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_addresses**
> [Address] get_entity_addresses(organisation_code, uuid)



Return all the addresses of the entity specified by its uuid

### Example

* Api Key Authentication (Token):
```python
import time
import osis_organisation_sdk
from osis_organisation_sdk.api import entites_api
from osis_organisation_sdk.model.address import Address
from osis_organisation_sdk.model.error import Error
from osis_organisation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/organisation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_organisation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/organisation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_organisation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entites_api.EntitesApi(api_client)
    organisation_code = "UCL" # str | 
    uuid = "uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    limit = 25 # int | Limit of paginated results (optional)
    offset = 25 # int | Offset of paginated results (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_entity_addresses(organisation_code, uuid)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entity_addresses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_entity_addresses(organisation_code, uuid, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entity_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_code** | **str**|  |
 **uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**[Address]**](Address.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

