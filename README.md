# osis-organisation-sdk
A set of API endpoints that allow you to get information about organizations

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_organisation_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_organisation_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_organisation_sdk
from pprint import pprint
from osis_organisation_sdk.api import entites_api
from osis_organisation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_organisation_sdk.model.entite_type_enum import EntiteTypeEnum
from osis_organisation_sdk.model.error import Error
from osis_organisation_sdk.model.paginated_addresses import PaginatedAddresses
from osis_organisation_sdk.model.paginated_entites import PaginatedEntites
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
year = 2020 # int |  (optional)
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
limit = 25 # int | Limit of paginated results (optional)
offset = 25 # int | Offset of paginated results (optional)

    try:
        api_response = api_instance.get_entities(organisation_code, entity_type=entity_type, year=year, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_organisation_sdk.ApiException as e:
        print("Exception when calling EntitesApi->get_entities: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/organisation*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EntitesApi* | [**get_entities**](docs/EntitesApi.md#get_entities) | **GET** /{organisation_code}/entites/ | 
*EntitesApi* | [**get_entity_addresses**](docs/EntitesApi.md#get_entity_addresses) | **GET** /{organisation_code}/entites/{uuid}/addresses | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [Address](docs/Address.md)
 - [Entite](docs/Entite.md)
 - [EntiteTypeEnum](docs/EntiteTypeEnum.md)
 - [Error](docs/Error.md)
 - [PaginatedAddresses](docs/PaginatedAddresses.md)
 - [PaginatedAddressesAllOf](docs/PaginatedAddressesAllOf.md)
 - [PaginatedEntites](docs/PaginatedEntites.md)
 - [PaginatedEntitesAllOf](docs/PaginatedEntitesAllOf.md)
 - [Paging](docs/Paging.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_organisation_sdk.apis and osis_organisation_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_organisation_sdk.api.default_api import DefaultApi`
- `from osis_organisation_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_organisation_sdk
from osis_organisation_sdk.apis import *
from osis_organisation_sdk.models import *
```
