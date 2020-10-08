# ubiops.CoreApi

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_model_requests_batch_collect**](CoreApi.md#batch_model_requests_batch_collect) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch-collect | Retrieve multiple batch model request results
[**batch_model_requests_batch_delete**](CoreApi.md#batch_model_requests_batch_delete) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch-delete | Delete multiple batch model requests
[**batch_model_requests_create**](CoreApi.md#batch_model_requests_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch | Create batch model requests
[**batch_model_requests_delete**](CoreApi.md#batch_model_requests_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch/{request_id} | Delete batch model requests
[**batch_model_requests_get**](CoreApi.md#batch_model_requests_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch/{request_id} | Get batch model request
[**batch_model_requests_list**](CoreApi.md#batch_model_requests_list) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch | List batch model requests
[**batch_pipeline_request_delete**](CoreApi.md#batch_pipeline_request_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Delete batch pipeline requests
[**batch_pipeline_request_get**](CoreApi.md#batch_pipeline_request_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Get batch pipeline request
[**batch_pipeline_requests_batch_collect**](CoreApi.md#batch_pipeline_requests_batch_collect) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-collect | Retrieve multiple batch pipeline request results
[**batch_pipeline_requests_batch_delete**](CoreApi.md#batch_pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-delete | Delete multiple batch pipeline requests
[**batch_pipeline_requests_create**](CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | Create batch pipeline requests
[**batch_pipeline_requests_list**](CoreApi.md#batch_pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | List batch pipeline requests
[**blobs_create**](CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**configurations_list**](CoreApi.md#configurations_list) | **GET** /config/connectors | List available connector configurations
[**connectors_create**](CoreApi.md#connectors_create) | **POST** /projects/{project_name}/connectors | Create a connector
[**connectors_delete**](CoreApi.md#connectors_delete) | **DELETE** /projects/{project_name}/connectors/{connector_name} | Delete connectors
[**connectors_get**](CoreApi.md#connectors_get) | **GET** /projects/{project_name}/connectors/{connector_name} | Get connectors
[**connectors_list**](CoreApi.md#connectors_list) | **GET** /projects/{project_name}/connectors | List connectors
[**connectors_update**](CoreApi.md#connectors_update) | **PATCH** /projects/{project_name}/connectors/{connector_name} | Update connectors
[**credentials_create**](CoreApi.md#credentials_create) | **POST** /projects/{project_name}/credentials | Create credentials
[**credentials_delete**](CoreApi.md#credentials_delete) | **DELETE** /projects/{project_name}/credentials/{credentials_name} | Delete credentials
[**credentials_get**](CoreApi.md#credentials_get) | **GET** /projects/{project_name}/credentials/{credentials_name} | Get credentials
[**credentials_list**](CoreApi.md#credentials_list) | **GET** /projects/{project_name}/credentials | List credentials
[**credentials_update**](CoreApi.md#credentials_update) | **PATCH** /projects/{project_name}/credentials/{credentials_name} | Update credentials
[**metrics_get**](CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**model_environment_variables_create**](CoreApi.md#model_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/environment-variables | Create model environment variable
[**model_environment_variables_delete**](CoreApi.md#model_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Delete model environment variable
[**model_environment_variables_get**](CoreApi.md#model_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Get model environment variable
[**model_environment_variables_list**](CoreApi.md#model_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/environment-variables | List model environment variables
[**model_environment_variables_update**](CoreApi.md#model_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Update model environment variable
[**model_requests_create**](CoreApi.md#model_requests_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request | Create model requests
[**model_version_environment_variables_create**](CoreApi.md#model_version_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | Create model version environment variable
[**model_version_environment_variables_delete**](CoreApi.md#model_version_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Delete model version environment variable
[**model_version_environment_variables_get**](CoreApi.md#model_version_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Get model version environment variable
[**model_version_environment_variables_list**](CoreApi.md#model_version_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | List model version environment variables
[**model_version_environment_variables_update**](CoreApi.md#model_version_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Update model version environment variable
[**model_versions_create**](CoreApi.md#model_versions_create) | **POST** /projects/{project_name}/models/{model_name}/versions | Create model versions
[**model_versions_delete**](CoreApi.md#model_versions_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version} | Delete model version
[**model_versions_file_download**](CoreApi.md#model_versions_file_download) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/download | Download model files
[**model_versions_file_upload**](CoreApi.md#model_versions_file_upload) | **PUT** /projects/{project_name}/models/{model_name}/versions/{version}/upload | Upload model files
[**model_versions_get**](CoreApi.md#model_versions_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version} | Get model version
[**model_versions_list**](CoreApi.md#model_versions_list) | **GET** /projects/{project_name}/models/{model_name}/versions | List model versions
[**model_versions_update**](CoreApi.md#model_versions_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version} | Update model version
[**models_create**](CoreApi.md#models_create) | **POST** /projects/{project_name}/models | Create a model
[**models_delete**](CoreApi.md#models_delete) | **DELETE** /projects/{project_name}/models/{model_name} | Delete a model
[**models_get**](CoreApi.md#models_get) | **GET** /projects/{project_name}/models/{model_name} | Get details of model
[**models_list**](CoreApi.md#models_list) | **GET** /projects/{project_name}/models | List models in project
[**models_update**](CoreApi.md#models_update) | **PATCH** /projects/{project_name}/models/{model_name} | Update a model
[**organization_subscriptions_list**](CoreApi.md#organization_subscriptions_list) | **GET** /organizations/{organization_name}/subscriptions | List subscriptions for an organization
[**organization_usage_details_get**](CoreApi.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
[**organization_usage_get**](CoreApi.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
[**organization_users_create**](CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](CoreApi.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
[**organizations_update**](CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**permissions_list**](CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
[**pipeline_object_attachments_create**](CoreApi.md#pipeline_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/attachments | Create object attachments
[**pipeline_object_attachments_delete**](CoreApi.md#pipeline_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Delete attachment of a source and destination object
[**pipeline_object_attachments_get**](CoreApi.md#pipeline_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Get an attachment of a source and destination object
[**pipeline_object_attachments_list**](CoreApi.md#pipeline_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments | List object attachments
[**pipeline_object_attachments_source_get**](CoreApi.md#pipeline_object_attachments_source_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/ | List the attachments of a source object
[**pipeline_object_environment_variables_list**](CoreApi.md#pipeline_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_objects_create**](CoreApi.md#pipeline_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/objects | Add an object to a pipeline
[**pipeline_objects_delete**](CoreApi.md#pipeline_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Delete object from pipeline
[**pipeline_objects_get**](CoreApi.md#pipeline_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Get an object in a pipeline
[**pipeline_objects_list**](CoreApi.md#pipeline_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects | List objects in a pipeline
[**pipeline_objects_update**](CoreApi.md#pipeline_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Update an object in a pipeline
[**pipelines_create**](CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete pipeline
[**pipelines_get**](CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get pipeline
[**pipelines_list**](CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_request**](CoreApi.md#pipelines_request) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request | Make a request to a pipeline
[**pipelines_update**](CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update pipeline
[**project_environment_variables_create**](CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_usage_get**](CoreApi.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**projects_create**](CoreApi.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](CoreApi.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](CoreApi.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**role_assignments_create**](CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
[**role_assignments_delete**](CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
[**role_assignments_get**](CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
[**role_assignments_per_user_list**](CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
[**roles_create**](CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**scheduled_requests_create**](CoreApi.md#scheduled_requests_create) | **POST** /projects/{project_name}/schedules | Create scheduled requests
[**scheduled_requests_delete**](CoreApi.md#scheduled_requests_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a scheduled request
[**scheduled_requests_get**](CoreApi.md#scheduled_requests_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a scheduled request
[**scheduled_requests_list**](CoreApi.md#scheduled_requests_list) | **GET** /projects/{project_name}/schedules | List scheduled requests
[**scheduled_requests_update**](CoreApi.md#scheduled_requests_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a scheduled request
[**service_status**](CoreApi.md#service_status) | **GET** /status | Service status
[**service_users_create**](CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**subscriptions_create**](CoreApi.md#subscriptions_create) | **POST** /subscriptions | Create subscriptions
[**subscriptions_delete**](CoreApi.md#subscriptions_delete) | **DELETE** /subscriptions/{subscription_name} | Delete a subscription
[**subscriptions_get**](CoreApi.md#subscriptions_get) | **GET** /subscriptions/{subscription_name} | Get details of a subscription
[**subscriptions_list**](CoreApi.md#subscriptions_list) | **GET** /subscriptions | List subscriptions
[**subscriptions_update**](CoreApi.md#subscriptions_update) | **PATCH** /subscriptions/{subscription_name} | Update details of a subscription
[**user_create**](CoreApi.md#user_create) | **POST** /user | Create a new user
[**user_delete**](CoreApi.md#user_delete) | **DELETE** /user | Delete user
[**user_get**](CoreApi.md#user_get) | **GET** /user | Get user details
[**user_update**](CoreApi.md#user_update) | **PATCH** /user | Update user details


# **batch_model_requests_batch_collect**
> list[BatchModelRequestResultList] batch_model_requests_batch_collect(project_name, model_name, version, data)

Retrieve multiple batch model request results


### Description
Retrieve multiple batch model requests. If one of the given batch model requests does not exist, an error message is given and no request is returned. A maximum of 250 model requests can be retrieved with this method. The model requests are NOT returned in the order they are given in.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure 
A list of dictionaries containing the details of the retrieved model requests with the following fields:
 - `id`: Unique identifier for the model request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the model request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `result`: Model request result value. NULL if the request is 'pending', 'processing' or 'failed'.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_last_updated": "2020-06-29T08:09:10.729+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_last_updated": "2020-03-25T09:37:17.765+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = None # object | 

    try:
        # Retrieve multiple batch model request results
        api_response = api_instance.batch_model_requests_batch_collect(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_batch_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**list[BatchModelRequestResultList]**](BatchModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_model_requests_batch_delete**
> object batch_model_requests_batch_delete(project_name, model_name, version, data)

Delete multiple batch model requests


### Description
Delete multiple batch model requests. If one of the given batch model requests does not exist, an error message is given and no request is deleted. A maximum of 250 model requests can be deleted with this method.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = None # object | 

    try:
        # Delete multiple batch model requests
        api_response = api_instance.batch_model_requests_batch_delete(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | **object**|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_model_requests_create**
> list[BatchModelRequestCreateResponse] batch_model_requests_create(project_name, model_name, version, data)

Create batch model requests


### Description
Request multiple predictions from a model. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the model request collect methods. It is only possible to make a model request if a model file is uploaded for that model version and the model build has succeeded (meaning that the model version is in available state).

If one of the requests is faulty, all requests are denied. The maximum number of requests per bulk call is 250.

### Required Parameters 
A list of dictionaries, where each dictionary contains the input fields of the model as keys. It is also possible to send a single dictionary as input.

#### Request Examples 
```
[
  {
    "model-input-field-1": 5.0,
    "model-input-field-2": "N",
    "model-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "model-input-field-1": 3.0,
    "model-input-field-2": "S",
    "model-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

### Response Structure 
A list of dictionaries containing the details of the created model requests with the following fields:
 - `id`: Unique identifier for the model request, which can be used to collect the result
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `time_created`: Server time that the request was made (current time)

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = [ubiops.ModelRequestCreate()] # list[ModelRequestCreate] | 

    try:
        # Create batch model requests
        api_response = api_instance.batch_model_requests_create(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**list[ModelRequestCreate]**](ModelRequestCreate.md)|  | 

### Return type

[**list[BatchModelRequestCreateResponse]**](BatchModelRequestCreateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_model_requests_delete**
> batch_model_requests_delete(project_name, model_name, request_id, version)

Delete batch model requests


### Description
Delete a batch model request


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

    try:
        # Delete batch model requests
        api_instance.batch_model_requests_delete(project_name, model_name, request_id, version)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_model_requests_get**
> BatchModelRequestResultList batch_model_requests_get(project_name, model_name, request_id, version)

Get batch model request


### Description
Get a batch request for a model. With this method, the result of a batch request may be retrieved.

### Response Structure 
A dictionary containing the details of the model request with the following fields:
 - `id`: Unique identifier for the model request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the model request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `result`: Model request result value. NULL if the request is 'pending', 'processing' or 'failed'.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_last_updated": "2020-03-29T08:09:10.729+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

    try:
        # Get batch model request
        api_response = api_instance.batch_model_requests_get(project_name, model_name, request_id, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**BatchModelRequestResultList**](BatchModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_model_requests_list**
> list[BatchModelRequestListResponse] batch_model_requests_list(project_name, model_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort)

List batch model requests


### Description
List all requests for a model version

### Optional Parameters
The following parameters should be given as Query parameters: 
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'
- `success`: A boolean value that indicates whether the model request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting, can be 'asc' or 'desc'. The default sorting is done in descending order.

### Response Structure 
A list of dictionaries containing the details of the model requests with the following fields:
 - `id`: Unique identifier for the model request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the model request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
status = 'status_example' # str |  (optional)
success = True # bool |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List batch model requests
        api_response = api_instance.batch_model_requests_list(project_name, model_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **status** | **str**|  | [optional] 
 **success** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**list[BatchModelRequestListResponse]**](BatchModelRequestListResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_request_delete**
> batch_pipeline_request_delete(project_name, pipeline_name, pipeline_request_id)

Delete batch pipeline requests


### Description
Delete a batch pipeline request. This action cancels all the model requests in the pipeline.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
pipeline_request_id = 'pipeline_request_id_example' # str | 

    try:
        # Delete batch pipeline requests
        api_instance.batch_pipeline_request_delete(project_name, pipeline_name, pipeline_request_id)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_request_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **pipeline_request_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_request_get**
> BatchPipelineRequestResultList batch_pipeline_request_get(project_name, pipeline_name, pipeline_request_id)

Get batch pipeline request


### Description
Get a batch request for a pipeline. With this method, the result of the batch request may be retrieved.

### Response Structure 
A dictionary containing the details of the pipeline request with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `model_requests`: A list of requests of the models in the pipeline. This field is empty when the request is initialized and is updated when all the model requests in the pipeline are completed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_last_updated": "2020-03-28T20:00:26.613+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "model_requests": [],
  "error_message": null
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
pipeline_request_id = 'pipeline_request_id_example' # str | 

    try:
        # Get batch pipeline request
        api_response = api_instance.batch_pipeline_request_get(project_name, pipeline_name, pipeline_request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_request_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **pipeline_request_id** | **str**|  | 

### Return type

[**BatchPipelineRequestResultList**](BatchPipelineRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_batch_collect**
> list[BatchPipelineRequestResultList] batch_pipeline_requests_batch_collect(project_name, pipeline_name, data)

Retrieve multiple batch pipeline request results


### Description
Retrieve multiple batch pipeline requests. If one of the given batch pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline requests can be retrieved with this method. The pipeline requests are NOT returned in the order they are given in.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure 
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated
 - `request_data`: A dictionary containing the data that was sent when the request was created
 - `model_requests`: A list of requests of the models in the pipeline. This field is empty when the request is initialized and is updated when all the model requests in the pipeline are completed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples 
```
[
    {
      "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
      "status": "pending",
      "success": false,
      "time_created": "2020-063-28T20:00:26.613+00:00",
      "time_last_updated": "2020-03-28T20:00:26.613+00:00",
      "request_data": {
        "input_field": 23.5
      },
      "model_requests": [],
      "error_message": null
    },
    {
      "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
      "status": "pending",
      "success": false,
      "time_created": "2020-063-28T20:00:26.613+00:00",
      "time_last_updated": "2020-03-28T20:00:26.613+00:00",
      "request_data": {
        "input_field": 23.5
      },
      "model_requests": [],
      "error_message": null
    }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = None # object | 

    try:
        # Retrieve multiple batch pipeline request results
        api_response = api_instance.batch_pipeline_requests_batch_collect(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_requests_batch_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**list[BatchPipelineRequestResultList]**](BatchPipelineRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_batch_delete**
> object batch_pipeline_requests_batch_delete(project_name, pipeline_name, data)

Delete multiple batch pipeline requests


### Description
Delete multiple batch pipeline requests. If one of the given batch pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters 
A list of ids for the batch requests

#### Request Examples 
```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = None # object | 

    try:
        # Delete multiple batch pipeline requests
        api_response = api_instance.batch_pipeline_requests_batch_delete(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_requests_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | **object**|  | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_create**
> list[BatchPipelineRequestCreateResponse] batch_pipeline_requests_create(project_name, pipeline_name, data)

Create batch pipeline requests


### Description
Request multiple predictions from a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters 
A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys

#### Request Examples 
```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

### Response Structure 
A list of dictionaries containing the details of the created pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request, which can be used to collect the result
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `time_created`: Server time that the request was made (current time)
 

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = [ubiops.PipelineRequestCreate()] # list[PipelineRequestCreate] | 

    try:
        # Create batch pipeline requests
        api_response = api_instance.batch_pipeline_requests_create(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_requests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**list[PipelineRequestCreate]**](PipelineRequestCreate.md)|  | 

### Return type

[**list[BatchPipelineRequestCreateResponse]**](BatchPipelineRequestCreateResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_pipeline_requests_list**
> list[BatchPipelineRequestListResponse] batch_pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort)

List batch pipeline requests


### Description
List all requests for a pipeline

### Optional Parameters
The following parameters should be given as query parameters: 
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting, can be 'asc' or 'desc'. The default sorting is done in descending order.

### Response Structure 
A list of dictionaries containing the details of the pipeline requests with the following fields:
 - `id`: Unique identifier for the pipeline request
 - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
 - `success`: A boolean value that indicates whether the pipeline request was successful
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated

#### Response Examples 
```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_last_updated": "2020-03-28T20:00:26.613+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
status = 'status_example' # str |  (optional)
success = True # bool |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)

    try:
        # List batch pipeline requests
        api_response = api_instance.batch_pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_pipeline_requests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **status** | **str**|  | [optional] 
 **success** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**list[BatchPipelineRequestListResponse]**](BatchPipelineRequestListResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_create**
> BlobList blobs_create(project_name, file, blob_ttl=blob_ttl)

Upload a blob


### Description 
Upload a blob to a project. The returned blob_id may be passed in a model or pipeline request as input.

The uploaded blob file can be retrieved by passing the blob_id as well. 

### Optional Parameters 
These parameters should be given in the header.
- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds (default = 259200 seconds, 3 days)

### Response Structure 
The details of the uploaded blob
- `id`: Unique identifier for the blob (UUID)
- `creation_date`: Time the blob was created
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

#### Response Examples
```
{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 259200
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
file = '/path/to/file' # file | 
blob_ttl = 56 # int |  (optional)

    try:
        # Upload a blob
        api_response = api_instance.blobs_create(project_name, file, blob_ttl=blob_ttl)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->blobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **file** | **file**|  | 
 **blob_ttl** | **int**|  | [optional] 

### Return type

[**BlobList**](BlobList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_delete**
> blobs_delete(project_name, blob_id)

Delete a blob


### Description 
Delete a blob from a project


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
blob_id = 'blob_id_example' # str | 

    try:
        # Delete a blob
        api_instance.blobs_delete(project_name, blob_id)
    except ApiException as e:
        print("Exception when calling CoreApi->blobs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **blob_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_get**
> BlobUpload blobs_get(project_name, blob_id)

Get a blob


### Description 
Download a blob file in a project

### Response Structure 
- `file`: Blob file


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
blob_id = 'blob_id_example' # str | 

    try:
        # Get a blob
        api_response = api_instance.blobs_get(project_name, blob_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->blobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **blob_id** | **str**|  | 

### Return type

[**BlobUpload**](BlobUpload.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blobs_list**
> list[BlobList] blobs_list(project_name, range=range, creation_date=creation_date)

List blobs


### Description 
List all blobs in a project

### Optional Parameters 
These parameters should be given as GET parameters.
- `range`: Number of blobs to be returned. It may be a positive or a negative value. If it is positive, blobs uploaded starting from the creation_date towards the present time are returned. Otherwise, blobs uploaded towards the past are returned. The default value is -50. 
- `creation_date`: Get the blobs uploaded starting from this date. If it is not provided, the uploaded blobs are returned according to the *range* parameter. It should be provided in year-month-day hour:minute:second format.

### Response Structure
A list of details of the blobs in the project
 - `id`: Unique identifier for the blob (UUID)
 - `creation_date`: Time the blob was created
 - `filename`: Original filename of the blob
 - `size`: Size of the uploaded blob in bytes
 - `ttl`: Time to live of the blob in seconds

#### Response Examples
```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-13T14:39:50.149+00:00",
    "filename": "original-filename.jpg",
    "size": 562,
    "ttl": 12338
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T08:35:18.796+00:00",
    "filename": "original-filename2.jpg",
    "size": 3439,
    "ttl": 259200
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
range = 56 # int |  (optional)
creation_date = 'creation_date_example' # str |  (optional)

    try:
        # List blobs
        api_response = api_instance.blobs_list(project_name, range=range, creation_date=creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->blobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **range** | **int**|  | [optional] 
 **creation_date** | **str**|  | [optional] 

### Return type

[**list[BlobList]**](BlobList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_list**
> list[ConfigurationList] configurations_list()

List available connector configurations


### Description
Get the details of available connectors. The configuration parameters for both the connectors and their corresponding credentials are returned with the required names and data types. These parameters must be provided when creating credentials and connectors.
If a new connector is supported, the necessary configuration parameters can be accessed with this method.

### Response Structure
Details of the available connectors and their credentials
- `connector`: Name of the connector
- `connector_type`: Type of the connector. It can be either structured or blob depending on what type of data is supported by the connector.
- `connector_configuration`: A dictionary with the following keys:
    - `parameter`: Name of the parameter necessary for the connector configuration
    - `name`: Descriptive name of the parameter
    - `description`: A description of the parameter
    - `input_field`: The HTML input field type for the UI
    - `default`: The default value for the parameter
    - `protected`: A boolean field to indicate if the parameter should be kept as hidden.
    - `regex`: The regex that is used to validate the parameter
- `credentials_configuration`: A dictionary with the following keys:
    - `parameter`: Name of the parameter necessary for the credentials configuration
    - `name`: Descriptive name of the parameter
    - `description`: A description of the parameter
    - `input_field`: The HTML input field type for the UI
    - `default`: The default value for the parameter
    - `protected`: A boolean field to indicate if the parameter should be kept as hidden.
    - `regex`: The regex that is used to validate the parameter


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # List available connector configurations
        api_response = api_instance.configurations_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->configurations_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigurationList]**](ConfigurationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_create**
> ConnectorList connectors_create(project_name, data)

Create a connector


### Description
Create a connector by defining its necessary configuration parameters. Connectors use a reference to credentials which will be used in authentication.

The type of a connector can be either a blob or structured. This input type is inferred from the given *type* field. For example, an aws_s3 connector is of type blob while a postgresql connector is structured.
For the **blob** type connectors, a default field is created with the name *blob* and data type *blob*. When blob connectors are attached in a pipeline, this field must be used in the mapping. It is not possible to define other fields for blob connectors.

### Required Parameters
- `name`: Name of the connector. It is unique within a project.
- `type`: Type of the connector. It should be one of the supported connectors such as aws_s3, postgresql and gcp_cloud_storage. The full list of supported connectors can be obtained from */config/connectors* endpoint.
- `credentials`: Name of referenced credentials
- `configuration`: A dictionary which should contain the fields necessary for the given type

### Optional Parameters
- `input_fields`: A list of connector fields with name and data_type. For example, for postgresql type of connector, these fields correspond to the columns of a table. In case of blob connectors, the input_fields should be omitted or given as an empty list. For structured connectors, they must be provided.

#### Request Examples
A postgresql connector
```
{
  "name": "postgresql-connector",
  "type": "postgresql",
  "credentials": "postgresql-credentials",
  "configuration": {
    "database": "database-1",
    "schema": "public",
    "table": "table-1"
  },
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
     {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```

### Response Structure 
Details of the created connector 
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to the type field. It can be either structured or blob.
- `project`: Project name in which the connector is created
- `credentials`: Name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type
- `status`: The state of the connector. It is initialized as pending_verification.
- `error_message`: The error message which explains why the connector has failed verification. It is empty if the connector is available.
- `creation_date`: The date when the connector was created
- `last_updated`: The date when the connector was last updated

#### Response Examples
```
{
  "id": "e0342249-853c-4879-bd08-5cd1af572d7e",
  "name": "postgresql-connector",
  "type": "postgresql",
  "input_type": "structured",
  "status": "pending_verification",
  "error_message": "",
  "project": "project-1",
  "credentials": "postgresql-credentials",
  "configuration": {
    "database": "database-1",
    "schema": "public",
    "table": "table-1"
  },
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
     {
      "name": "field-2",
      "data_type": "double"
    }
  ],
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.ConnectorCreate() # ConnectorCreate | 

    try:
        # Create a connector
        api_response = api_instance.connectors_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->connectors_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ConnectorCreate**](ConnectorCreate.md)|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_delete**
> connectors_delete(project_name, connector_name)

Delete connectors

Delete a connector in a project

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 

    try:
        # Delete connectors
        api_instance.connectors_delete(project_name, connector_name)
    except ApiException as e:
        print("Exception when calling CoreApi->connectors_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_get**
> ConnectorList connectors_get(project_name, connector_name)

Get connectors


### Description
Get the details of a single connector

### Response Structure
Details of the connector
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to the type field. It can be either structured or blob.
- `project`: Project name in which the connector is defined
- `credentials`: Name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type
- `status`: The state of the connector. It can be pending_verification, failed_verification or available.
- `error_message`: The error message which explains why the connector has failed verification. It is empty if the connector is available.
- `creation_date`: The date when the connector was created
- `last_updated`: The date when the connector was last updated

#### Response Examples 
```
{
  "id": "662c326c-a560-4322-8ed3-1229224257c43",
  "name": "s3-connector",
  "type": "aws_s3",
  "input_type": "blob",
  "status": "available",
  "error_message": "",
  "project": "project-1",
  "credentials": "s3-credentials",
  "configuration": {
    "bucket": "bucket-name",
    "path_prefix": "blob"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 

    try:
        # Get connectors
        api_response = api_instance.connectors_get(project_name, connector_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->connectors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_list**
> list[ConnectorList] connectors_list(project_name)

List connectors


### Description
List the connectors in a project

### Response Structure
A list of details of the connectors in the project
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to type field. It can be either structured or blob.
- `project`: Project name in which the connector is defined
- `credentials`: Name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type
- `status`: The state of the connector. It can be pending_verification, failed_verification or available.
- `error_message`: The error message which explains why the connector has failed verification. It is empty if the connector is available.
- `creation_date`: The date when the connector was created
- `last_updated`: The date when the connector was last updated

#### Response Examples
```
[
  {
    "id": "662c326c-a560-4322-8ed3-1229224257c43",
    "name": "s3-connector",
    "type": "aws_s3",
    "input_type": "blob",
    "status": "available",
    "error_message": "",
    "project": "project-1",
    "credentials": "s3-credentials",
    "configuration": {
      "bucket": "bucket-name",
      "path_prefix": "blob"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  },
  {
    "id": "e0342249-853c-4879-bd08-5cd1af572d7e",
    "name": "postgresql-connector",
    "type": "postgresql",
    "input_type": "structured",
    "status": "available",
    "error_message": "",
    "project": "project-1",
    "credentials": "postgresql-credentials",
    "configuration": {
      "database": "database-1",
      "schema": "public",
      "table": "table-1"
    },
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List connectors
        api_response = api_instance.connectors_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->connectors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ConnectorList]**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_update**
> ConnectorList connectors_update(project_name, connector_name, data)

Update connectors


### Description
Update a connector in a project. When updating, all necessary fields are validated again. It is not possible to update the **type** of a connector.

### Optional Parameters
- `name`: New name for the connector
- `credentials`: A new credentials name to be referenced
- `configuration`: A new dictionary with new values for credentials configuration. This dictionary may contain a subset of the necessary parameters for the credentials type. Only the given parameters are updated and the rest is kept at their old values.
- `input_fields`: The old fields are changed with the new ones. If one or more old fields wanted to be kept for the connector, they must be provided again.

#### Request Examples
```	
{
  "name": "new-connector-name"
}
```

```
{
  "configuration": {
    "bucket": "new-bucket-name",
    "path_prefix": "new-blob"
  }
}
```

```
{
  "credentials": "new-credentials-name"
}
```

```
{
  "input_fields": [
    {
      "name": "new-connector-field-1",
      "data_type": "double"
    },
    {
      "name": "new-connector-field-2",
      "data_type": "array_int"
    }
  ]
}
```

### Response Structure
Details of the updated connector
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to the type field. It can be either structured or blob.
- `project`: Project name in which the connector is defined
- `credentials`: Name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type
- `status`: The state of the connector. If the configuration parameters are updated, the connector is verified again.
- `error_message`: The error message which explains why the connector has failed verification. It is empty if the connector is available.
- `creation_date`: The date when the connector was created
- `last_updated`: The date when the connector was last updated

#### Response Examples
```	
{
  "id": "662c326c-a560-4322-8ed3-1229224257c43",
  "name": "new-s3-connector",
  "type": "aws_s3",
  "input_type": "blob",
  "status": "available",
  "error_message": "",
  "project": "project-1",
  "credentials": "s3-credentials",
  "configuration": {
    "bucket": "new-bucket-name",
    "path_prefix": "blob"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 
data = ubiops.ConnectorUpdate() # ConnectorUpdate | 

    try:
        # Update connectors
        api_response = api_instance.connectors_update(project_name, connector_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->connectors_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 
 **data** | [**ConnectorUpdate**](ConnectorUpdate.md)|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_create**
> CredentialsList credentials_create(project_name, data)

Create credentials


### Description 
Create a new credentials by defining its necessary configuration parameterss

### Required Parameters 
- `name`: Name of the credentials. It is unique within a project.
- `type`: Type of the credentials. It should be one of the supported connectors such as aws_s3, postgresql and gcp_cloud_storage.
- `configuration`: A dictionary which should contain the fields necessary for the given type

#### Request Examples 
```
{
  "name": "s3-credentials",
  "type": "aws_s3",
  "configuration": {
    "access_key": "access_key",
    "secret_key": "secret_key",
    "region": "eu-central-1"
  }
}
```

### Response Structure 
Details of the created credentials
 - `id`: Unique identifier for the credentials (UUID)
 - `name`: Name of the credentials
 - `project`: Project name in which the credentials is created
 - `type`: Type of the credentials
 - `reference_count`: The number of connectors using this credentials. It is initialised as 0 when it is created.
 - `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
 - `status`: The state of the credentials. It is initialized as pending_verification.
 - `error_message`: The error message which explains why the credentials has failed verification. It is empty if the credentials is available.
 - `creation_date`: The date when the credentials was created
 - `last_updated`: The date when the credentials was last updated

#### Response Examples 
```
{
  "id": "da4da757-373c-4cab-948e-90ff4ab2e9c3",
  "name": "s3-credentials",
  "project": "project-1",
  "type": "aws_s3",
  "status": "pending_verification",
  "error_message": "",
  "reference_count": 0,
  "configuration": {
    "access_key": null,
    "secret_key": null,
    "region": "eu-central-1"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.CredentialsCreate() # CredentialsCreate | 

    try:
        # Create credentials
        api_response = api_instance.credentials_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->credentials_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**CredentialsCreate**](CredentialsCreate.md)|  | 

### Return type

[**CredentialsList**](CredentialsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_delete**
> credentials_delete(project_name, credentials_name)

Delete credentials

 
### Description 
Delete a credentials. If there is a reference to the credentials from a connector, it is **not possible to delete** the credentials. The reference should be removed first.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 

    try:
        # Delete credentials
        api_instance.credentials_delete(project_name, credentials_name)
    except ApiException as e:
        print("Exception when calling CoreApi->credentials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_get**
> CredentialsListWithConfig credentials_get(project_name, credentials_name)

Get credentials


### Description 
Get the details of a single credentials

### Response Structure 
Details of the credentials
- `id`: Unique identifier for the credentials (UUID)
- `name`: Name of the credentials
- `project`: Project name in which the credentials is defineds
- `type`: Type of the credentials
- `reference_count`: The number of connectors using the credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `status`: The state of the credentials. It can be pending_verification, failed_verification or available.
- `error_message`: The error message which explains why the credentials has failed verification. It is empty if the credentials is available.
- `creation_date`: The date when the credentials was created
- `last_updated`: The date when the credentials was last updated

#### Response Examples 
```
{ 
  "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
  "name": "postgresql-credentials",
  "project": "project-1",
  "type": "postgresql",
  "status": "available",
  "error_message": "",
  "reference_count": 2,
  "configuration": {
    "username": "user",
    "password": null,
    "host": "host",
    "port": "1234"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 

    try:
        # Get credentials
        api_response = api_instance.credentials_get(project_name, credentials_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 

### Return type

[**CredentialsListWithConfig**](CredentialsListWithConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_list**
> list[CredentialsList] credentials_list(project_name)

List credentials

 
### Description
List all the sets of credentials in a project

### Response Structure 
A list of details of the credentials in the project
- `id`: Unique identifier for the credentials (UUID)
- `name`: Name of the credentials
- `project`: Project name in which the credentials is defined
- `type`: Type of the credentials
- `reference_count`: The number of connectors using the credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `status`: The state of the credentials. It can be pending_verification, failed_verification or available.
- `error_message`: The error message which explains why the credentials has failed verification. It is empty if the credentials is available.
- `creation_date`: The date when the credentials was created
- `last_updated`: The date when the credentials was last updated

#### Response Examples 
```
[
  {
    "id": "da4da757-373c-4cab-948e-90ff4ab2e9c3",
    "name": "s3-credentials",
    "project": "project-1",
    "type": "aws_s3",
    "status": "available",
    "error_message": "",
    "reference_count": 1,
    "configuration": {
      "access_key": null,
      "secret_key": null,
      "region": "eu-central-1"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  },
  {
    "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
    "name": "postgresql-credentials",
    "project": "project-1",
    "type": "postgresql",
    "status": "available",
    "error_message": "",
    "reference_count": 2,
    "configuration": {
      "username": "user",
      "password": null,
      "host": "host",
      "port": "1234"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List credentials
        api_response = api_instance.credentials_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->credentials_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[CredentialsList]**](CredentialsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_update**
> CredentialsListWithConfig credentials_update(project_name, credentials_name, data)

Update credentials

 
### Description
Update a credentials. It is not possible to update the type of a credentials. All necessary fields are validated again.

### Optional Parameters 
- `name`: New name for the credentials
- `configuration`: A new dictionary with new values for credentials configuration. This dictionary may contain a subset of the necessary parameters for the credentials type. Only the given parameters are updated and the rest is kept at their old values.

#### Request Examples 
```
{
  "name": "new-credentials-name"
}
```

```
{
  "configuration": {
    "username": "new_user",
    "password": "new_secret_password",
    "host": "new_host",
    "port": "1234"
  }
}
```

### Response Structure 
Details of the updated credentials
- `id`: Unique identifier for the credentials (UUID)
- `name`: Name of the credentials
- `project`: Project name in which the credentials is defined
- `type`: Type of the credentials
- `reference_count`: The number of connectors using the credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `status`: The state of the credentials. If the configuration parameters are updated, the connector is verified again. If there is a connector referencing this credentials, it is also verified again with the updated configuration.
- `error_message`: The error message which explains why the credentials has failed verification. It is empty if the credentials is available.
- `creation_date`: The date when the credentials was created
- `last_updated`: The date when the credentials was last updated

#### Response Examples 
```
{ 
  "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
  "name": "postgresql-credentials",
  "project": "project-1",
  "type": "postgresql",
  "status": "pending_verification",
  "error_message": "",
  "reference_count": 2,
  "configuration": {
    "username": "new_user",
    "password": null,
    "host": "new_host",
    "port": "1234"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 
data = ubiops.CredentialsUpdate() # CredentialsUpdate | 

    try:
        # Update credentials
        api_response = api_instance.credentials_update(project_name, credentials_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->credentials_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 
 **data** | [**CredentialsUpdate**](CredentialsUpdate.md)|  | 

### Return type

[**CredentialsListWithConfig**](CredentialsListWithConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_get**
> list[Metrics] metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)

Get metrics


### Description 
Get metrics for the project or a specified object. The following metrics are available:

Metrics on pipeline level: 
 - `requests`: Number of requests made to the object
 - `input_volume`: Volume of incoming data in bytes
 - `object_requests`: Number of requests made to objects in the pipeline
 
Metrics on model version level: 
 - `requests`: Number of requests made to the object
 - `input_volume`: Volume of incoming data in bytes
 - `output_volume`: Volume of outgoing data in bytes
 - `outputs`: Number of outgoing data items 
 - `compute`: Time in seconds for a model request to complete
 - `instances`: Number of active model instances
 - `gb_seconds`: Usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds the models are running
 - `active_time`: Time in seconds that the model is active
 
Metrics on connector level: 
 - `requests`: Number of requests made to the object
 - `volume`: Volume of incoming data in bytes

### Required Parameters 
- `start_time`: Starting time for the metric values to be returned. It should be provided in datetime isoformat.
- `end_time`: Ending time for the metric values to be returned. It should be provided in datetime isoformat.
- `object_type`: The type of the object for which the metrics are requested. It can be either `model_version`, `connector` or `pipeline`.

### Optional Parameters 
- `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
- `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.

### Response Structure 
- `start_time`: Timestamp denoting the start of the period over which the metric was measured
- `end_time`: Timestamp denoting the end of the period over which the metric was measured
- `value`: Aggregated metric value for the given interval

#### Response Examples
With interval as minute, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 12:03:00
```
[
  {
    "start_time": "2019-11-13T12:00:00+00:00",
    "end_time": "2019-11-13T12:01:00+00:00",
    "value": 100
  },
  {
    "start_time": "2019-11-13T12:01:00+00:00",
    "end_time": "2019-11-13T12:02:00+00:00",
    "value": 134
  },
  {
    "start_time": "2019-11-13T12:02:00+00:00",
    "end_time": "2019-11-13T12:03:00+00:00",
    "value": 112
  }
]

```

With interval as hour, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 14:00:00
```
[
  {
   "start_time": "2019-11-13T12:00:00+00:00",
   "end_time": "2019-11-13T13:00:00+00:00",
   "value": 92
  },
  {
    "start_time": "2019-11-13T13:00:00+00:00",
    "end_time": "2019-11-13T14:00:00+00:00",
    "value": 120
  },
  {
    "start_time": "2019-11-13T14:00:00+00:00",
    "end_time": "2019-11-13T15:00:00+00:00",
    "value": 0
  }
]
```
 
With interval as day, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-14 12:00:00
```
[
  {
   "start_time": "2019-11-13T00:00:00+00:00",
   "end_time": "2019-11-14T00:00:00+00:00",
   "value": 528
  },
  {
    "start_time": "2019-11-14T00:00:00+00:00",
    "end_time": "2019-11-15T00:00:00+00:00",
    "value": 342
  }
]
```
 
With interval as month, start_time as 2019-11-13 12:00:00 and end_time as 2019-12-13 12:00:00
```
[
  {
   "start_time": "2019-11-01T00:00:00+00:00",
   "end_time": "2019-12-01T00:00:00+00:00",
   "value": 1983
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
metric = 'metric_example' # str | 
start_time = 'start_time_example' # str | 
end_time = 'end_time_example' # str | 
object_type = 'object_type_example' # str | 
interval = 'interval_example' # str |  (optional)
object_id = 'object_id_example' # str |  (optional)

    try:
        # Get metrics
        api_response = api_instance.metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **metric** | **str**|  | 
 **start_time** | **str**|  | 
 **end_time** | **str**|  | 
 **object_type** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **object_id** | **str**|  | [optional] 

### Return type

[**list[Metrics]**](Metrics.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_create**
> EnvironmentVariableList model_environment_variables_create(project_name, model_name, data)

Create model environment variable


### Description
Create an environment variable for the model. This variable will be inherited by all versions of this model. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "model_variable_a",
  "value": "some_value",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "model_variable_a",
"value": "some_value",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Create model environment variable
        api_response = api_instance.model_environment_variables_create(project_name, model_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_delete**
> model_environment_variables_delete(project_name, id, model_name)

Delete model environment variable


### Description
Delete an environment variable of the model


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # Delete model environment variable
        api_instance.model_environment_variables_delete(project_name, id, model_name)
    except ApiException as e:
        print("Exception when calling CoreApi->model_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_get**
> EnvironmentVariableList model_environment_variables_get(project_name, id, model_name)

Get model environment variable


### Description
Retrieve details of a model environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # Get model environment variable
        api_response = api_instance.model_environment_variables_get(project_name, id, model_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_list**
> list[InheritedEnvironmentVariableList] model_environment_variables_list(project_name, model_name)

List model environment variables


### Description
List the environment variables defined for the model. Includes environment variables defined at project level.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project` or empty if the variable was defined for the model directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be empty if the variable was defined for the model directly

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "",
    "inheritance_name": ""
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # List model environment variables
        api_response = api_instance.model_environment_variables_list(project_name, model_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_update**
> EnvironmentVariableList model_environment_variables_update(project_name, id, model_name, data)

Update model environment variable


### Description
Update an environment variable for the model. This cannot be used to update inherited variables; to change an inherited variable for a specific model you can create a variable with the same name for the model.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "model_variable_a",
  "value": "some new value",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "model_variable_a",
  "value": "some new value",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Update model environment variable
        api_response = api_instance.model_environment_variables_update(project_name, id, model_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_create**
> ModelRequestList model_requests_create(project_name, model_name, version, data, timeout=timeout)

Create model requests


### Description 
Request a prediction from a model. Model requests are made for a specific version of a model. It is only possible to make a model request if a model file is uploaded for that model version and the model build has succeeded (meaning that the model version is in available state).
In case of a **blob** field, the uuid of a previously uploaded blob must be provided.

### Required Parameters
A dictionary which contains the input fields of the model as keys

### Optional Parameters
These parameters should be given as GET parameters
- `timeout`: Timeout for the model request in seconds. The maximum allowed value is 3600 and the default value is 300.

#### Request Examples
```
{
  "model-input-field-1": 5.0,
  "model-input-field-2": "N",
  "model-input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

```
{
  "input-field-1": 5.0,
  "blob-input-field": "f52ff875-4980-4d71-9798-a469ef8cece2"
}
```

### Response Structure 
Details of the created model request
- `request_id`: Unique identifier for the model request
- `success`: A boolean value that indicates whether the model request was successful
- `result`: Model request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

#### Response Examples
A failed model request
```
{
  "request_id": "edcf07b5-ae15-46e6-ba29-daeed53eaa61",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful model request
```
{
  "request_id": "b98a6d68-3173-409a-9e6e-a56804045a9c",
  "success": true,
  "result": {
    "model-output-field-1": "2.1369",
    "model-output-field-2": "5.5832",
  },
  "error_message": None
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.ModelRequestCreate() # ModelRequestCreate | 
timeout = 56 # int |  (optional)

    try:
        # Create model requests
        api_response = api_instance.model_requests_create(project_name, model_name, version, data, timeout=timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_requests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**ModelRequestCreate**](ModelRequestCreate.md)|  | 
 **timeout** | **int**|  | [optional] 

### Return type

[**ModelRequestList**](ModelRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_create**
> EnvironmentVariableList model_version_environment_variables_create(project_name, model_name, version, data)

Create model version environment variable


### Description
Create an environment variable for the model version. Variables inherited from the project or model can be shadowed by creating a variable with the same name.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "version_variable",
  "value": "another one",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "version_variable",
  "value": "another one",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Create model version environment variable
        api_response = api_instance.model_version_environment_variables_create(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_version_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_delete**
> model_version_environment_variables_delete(project_name, id, model_name, version)

Delete model version environment variable


### Description
Delete an environment variable of the model version


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # Delete model version environment variable
        api_instance.model_version_environment_variables_delete(project_name, id, model_name, version)
    except ApiException as e:
        print("Exception when calling CoreApi->model_version_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_get**
> EnvironmentVariableList model_version_environment_variables_get(project_name, id, model_name, version)

Get model version environment variable


### Description
Retrieve details of a model version environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # Get model version environment variable
        api_response = api_instance.model_version_environment_variables_get(project_name, id, model_name, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_version_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_list**
> list[InheritedEnvironmentVariableList] model_version_environment_variables_list(project_name, model_name, version)

List model version environment variables


### Description
List the environment variables defined for the model version. Includes environment variables defined at project level and model level.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `model`, or empty if the variable was defined for the model version directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be empty if the variable was defined for the model version directly

#### Response Examples 
```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": "",
    "inheritance_name": ""
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "model",
    "inheritance_name": "model_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # List model version environment variables
        api_response = api_instance.model_version_environment_variables_list(project_name, model_name, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_version_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_update**
> EnvironmentVariableList model_version_environment_variables_update(project_name, id, model_name, version, data)

Update model version environment variable


### Description
Update an environment variable for the model version. This cannot be used to update inherited variables; to change an inherited variable for a specific version you can create a variable with the same name for the version.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "version_variable",
  "value": "yet another one",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "version_variable",
  "value": "yet another one",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Update model version environment variable
        api_response = api_instance.model_version_environment_variables_update(project_name, id, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_version_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_create**
> ModelVersionList model_versions_create(project_name, model_name, data)

Create model versions


### Description 
Create a version for a model

### Required Parameters 
- `version`: Name of the version of the model

### Optional Parameters 
- `language`: Language in which the model version is provided. It can be python3.5, python3.6, python3.7 or python3.8. The default value is python3.7
- `memory_allocation`: Reserved memory for the version in MB. This value determines the memory allocated to the model version: it should to be enough to encompass the model file and all requirements that need to be installed. The default value is 2048. The minimum and maximum values are 256 and 32768 respectively.
- `maximum_instances`: Upper bound of number of model versions running. The default value is 5, the maximum value is 20. *Indicator of resource capacity:* if many model requests need to be handled in a short time, this number can be set higher to avoid long waiting times.
- `minimum_instances`: Lower bound of number of model versions running. The default value is 0. Set this value greater than 0 to always have a always running model version.
- `maximum_idle_time`: Maximum time in seconds a model version stays idle before it is stopped. The default value is 300, the minimum value is 10 and the maximum value is 3600. A high value means that the model version stays active longer. Sending requests to a running model version means that it will be already initialized and thus take a shorter timer. 

- `description`: Description for the model version

If the time that a request takes does not matter, keep the default values.

#### Request Examples 
```
{
  "version": "version-1",
  "language": "python3.6"
}
```
 
```
{
  "version": "version-1",
  "language": "python3.5",
  "memory_allocation": 512
}
```
 
```
{
  "version": "version-1",
  "maximum_instances": 4,
  "minimum_instances": 1
}
```

### Response Structure 
Details of the created version
- `id`: Unique identifier for the model (UUID)
- `model`: Model name to which the version is associated
- `version`: Version name
- `language`: Language in which the model version is provided
- `memory_allocation`: Reserved memory for the version in MB  
- `maximum_instances`: Upper bound of number of model versions running
- `minimum_instances`: Lower bound of number of model versions running
- `maximum_idle_time`: Maximum time in seconds a model version stays idle before it is stopped
- `description`: Description of the model version
- `status`: The state of the model version. It is set to *initialised* state on creation.
- `error_message`: The error message which explains why the model version has failed building or deployment. It is empty if the model version is available.
- `creation_date`: The date when the model version was created
- `last_updated`: The date when the model version was last updated
- `file_last_updated`: The date when a model file was last uploaded

#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.5",
  "description": "",
  "status": "initialised",
  "error_message": "",
  "memory_allocation": 512,
  "maximum_instances": 5,
  "minimum_instances": 0,
  "maximum_idle_time": 10,
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z",
  "file_last_updated": "2020-05-12T16:23:15.456812Z",
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = ubiops.ModelVersionCreate() # ModelVersionCreate | 

    try:
        # Create model versions
        api_response = api_instance.model_versions_create(project_name, model_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**ModelVersionCreate**](ModelVersionCreate.md)|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_delete**
> model_versions_delete(project_name, model_name, version)

Delete model version

 
### Description 
Delete a model version. If the model version is referenced from a pipeline, it cannot be deleted, it must be removed from the pipeline first.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # Delete model version
        api_instance.model_versions_delete(project_name, model_name, version)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_file_download**
> ModelVersionFileUpload model_versions_file_download(project_name, model_name, version)

Download model files


### Description 
Download the model file of a model version of a model

### Response Structure 
 - `file`: Model file of the version


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # Download model files
        api_response = api_instance.model_versions_file_download(project_name, model_name, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_file_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelVersionFileUpload**](ModelVersionFileUpload.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_file_upload**
> Success model_versions_file_upload(project_name, model_name, version, file)

Upload model files


### Description 
Upload a file for a model version. This file should contain the model that will be run. It should be provided as a zip and a template can be found on https://github.com/UbiOps/model-template. The file is saved under a directory in the storage specified in the settings.

### Required Parameters
- `file`: Model file

### Response Structure
- `success`: Boolean indicating whether the model file upload succeeded or not



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
file = '/path/to/file' # file | 

    try:
        # Upload model files
        api_response = api_instance.model_versions_file_upload(project_name, model_name, version, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**Success**](Success.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_get**
> ModelVersionList model_versions_get(project_name, model_name, version)

Get model version


### Description 
Retrieve details of a model version of a model in a project

### Response Structure 
Details of a version
- `id`: Unique identifier for the model (UUID)
- `model`: Model name to which the version is associated
- `version`: Version name
- `language`: Language in which the model version is provided
- `memory_allocation`: Reserved memory for the version in MB 
- `maximum_instances`: Upper bound of number of model pods running in parallel
- `minimum_instances`: Lower bound of number of model pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a model version stays idle before it is stopped
- `description`: Description of the model version
- `status`: The state of the model version
- `error_message`: The error message which explains why the model version has failed building or deployment. It is empty if the model version is available.
- `creation_date`: The date when the model version was created
- `last_updated`: The date when the model version was last updated
- `file_last_updated`: The date when a model file was last uploaded

#### Response Examples
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "memory_allocation": 512,
  "language": "python3.7",
  "description": "",
  "status": "active",
  "error_message": "",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "file_last_updated": "2020-06-23T11:17:28.128652Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

    try:
        # Get model version
        api_response = api_instance.model_versions_get(project_name, model_name, version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_list**
> list[ModelVersionList] model_versions_list(project_name, model_name)

List model versions


### Description 
List all the versions of a model in a project

### Response Structure 
A list of details of the versions
- `id`: Unique identifier for the model (UUID)
- `model`: Model name to which the version is associated
- `version`: Version name
- `language`: Language in which the model version is provided
- `memory_allocation`: Reserved memory usage for the version in MB
- `maximum_instances`: Upper bound of number of model versions running
- `minimum_instances`: Lower bound of number of model versions running
- `maximum_idle_time`: Maximum time in seconds a model version stays idle before it is stopped
- `description`: Description of the model version
- `status`: The state of the model version
- `error_message`: The error message which explains why the model version has failed building or deployment. It is empty if the model version is available.
- `creation_date`: The date when the model version was created
- `last_updated`: The date when the model version was last updated
- `file_last_updated`: The date when a model file was last uploaded

#### Response Examples
```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "model": "model-1",
    "version": "version-1",
    "language": "python3.5",
    "description": "",
    "status": "active",
    "error_message": "",
    "memory_allocation": 512,
    "maximum_instances": 4,
    "minimum_instances": 1,
    "maximum_idle_time": 10,
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "file_last_updated": "2020-06-19T10:52:23.124784Z"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "model": "model-1",
    "version": "version-2",
    "language": "python3.6",
    "description": "",
    "status": "active",
    "error_message": "",
    "memory_allocation": 256,
    "maximum_instances": 5,
    "minimum_instances": 0,
    "maximum_idle_time": 10,
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "file_last_updated": "2020-06-23T11:17:28.128652Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # List model versions
        api_response = api_instance.model_versions_list(project_name, model_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**list[ModelVersionList]**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_update**
> ModelVersionList model_versions_update(project_name, model_name, version, data)

Update model version


### Description 
Update a model version of a model in a project. Updating the language field will cause the model to be build again. All necessary fields are validated again.

### Optional Parameters 
- `version`: New name for the version
- `language`: New language for the version
- `memory_allocation`: New reserved memory for the version in MB
- `maximum_instances`: New upper bound of number of model versions running
- `minimum_instances`: New lower bound of number of model versions running
- `maximum_idle_time`: New maximum time in seconds a model version stays idle before it is stopped
- `description`: New description for the version

#### Request Examples 
```
{
  "version": "new-version"
}
```
 
```
{
  "memory_allocation": 512,
  "maximum_instances": 4,
  "minimum_instances": 1
}
```

### Response Structure 
Details of the updated version
- `id`: Unique identifier for the model (UUID)
- `model`: Model name to which the version is associated
- `version`: Version name
- `language`: Language in which the model version is provided
- `memory_allocation`: Reserved memory for the version in MB
- `maximum_instances`: Upper bound of number of model versions running
- `minimum_instances`: Lower bound of number of model versions running
- `maximum_idle_time`: Maximum time in seconds a model version stays idle before it is stopped
- `description`: Description of the model version
- `status`: The state of the model version
- `error_message`: The error message which explains why the model version has failed building or deployment. It is empty if the model version is available.
- `creation_date`: The date when the model version was created
- `last_updated`: The date when the model version was last updated
- `file_last_updated`: The date when a model file was last uploaded

#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.5",
  "description": "",
  "status": "active",
  "error_message": "",
  "memory_allocation": 512,
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-23T18:04:76.123754Z",
  "file_last_updated": "2020-06-23T11:17:28.128652Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = ubiops.ModelVersionCreate() # ModelVersionCreate | 

    try:
        # Update model version
        api_response = api_instance.model_versions_update(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->model_versions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**ModelVersionCreate**](ModelVersionCreate.md)|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create**
> ModelList models_create(project_name, data)

Create a model


### Description 
Create a model by defining the input/output type and input/output fields. In case of **plain** type of input or output, input and output fields should not be given or passed as an empty list.

Possible data types for the input and output fields are:
- **int**: integer
- **string**: string
- **double**: double precision floating point
- **bool**: boolean value (False/True)
- **timestamp**: timestamp
- **array_int**: an array of integers
- **array_double**: an array of double precision floating points
- **array_string**: an array of strings
- **blob**: a blob field. This type of field can be used to pass blobs to the model. In model and pipeline requests, the uuid of a previously uploaded blob must be provided for this field.

### Required Parameters 
- `name`: Name of the model. It is unique within a project.
- `input_type`: Type of the input of the model. It can be either structured or plain.
- `output_type`: Type of the output of the model. It can be either structured or plain.
- `input_fields`: The list of required model input fields. It must contain the fields: name and data_type. The name of an input field is unique for a model.
- `output_fields`: The list of required model output fields. It must contain the fields: name and data_type. The name of an output field is unique for a model.

### Optional Parameters
- `description`: Description of the model

#### Request Examples
A model with structured input and output type
```
{
  "name": "model-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```
 
A model with plain input type
```
{
  "name": "model-1",
  "description": "Model one"
  "input_type": "plain",
  "output_type": "structured",
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```
 
A model with plain input and output type
```
{
  "name": "model-1",
  "input_type": "plain",
  "output_type": "plain"
}
```

### Response Structure 
Details of the created model
- `id`: Unique identifier for the model (UUID)
- `name`: Name of the model
- `project`: Project name in which the model is created
- `input_type`: Type of the input of the model
- `output_type`: Type of the output of the model
- `input_fields`: The list of model input fields containing name and data_type
- `output_fields`: The list of model output fields containing name and data_type
- `description`: Description of the model
- `creation_date`: The date when the model was created
- `last_updated`: The date when the model was last updated
- `number_of_versions`: Number of versions that this model has

#### Response Examples 
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "model-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-18T08:32:14.876451Z",
  "number_of_versions": 0
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.ModelCreate() # ModelCreate | 

    try:
        # Create a model
        api_response = api_instance.models_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->models_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ModelCreate**](ModelCreate.md)|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_delete**
> models_delete(project_name, model_name)

Delete a model


### Description 
Delete a model. If any of the model versions of the model are referenced in a pipeline, the model cannot be deleted.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # Delete a model
        api_instance.models_delete(project_name, model_name)
    except ApiException as e:
        print("Exception when calling CoreApi->models_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get**
> ModelList models_get(project_name, model_name)

Get details of model


### Description 
Retrieve details of a single model in a project

### Response Structure 
Details of a model
- `id`: Unique identifier for the model (UUID)
- `name`: Name of the model
- `project`: Project name in which the model is defined
- `input_type`: Type of the input of the model
- `output_type`: Type of the output of the model
- `input_fields`: The list of model input fields containing name and data_type
- `output_fields`: The list of model output fields containing name and data_type
- `description`: Description of the model
- `creation_date`: The date when the model was created
- `last_updated`: The date when the model was last updated
- `number_of_versions`: Number of versions that this model has

#### Response Examples 
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "model-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "number_of_versions": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

    try:
        # Get details of model
        api_response = api_instance.models_get(project_name, model_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list**
> list[ModelList] models_list(project_name)

List models in project


### Description 
List all models in a project

### Response Structure 
A list of details of the models in the project
- `id`: Unique identifier for the model (UUID)
- `name`: Name of the model
- `project`: Project name in which the model is defined
- `input_type`: Type of the input of the model
- `output_type`: Type of the output of the model
- `input_fields`: The list of model input fields containing name and data_type. It is empty in case of plain input type models.
- `output_fields`: The list of model output fields containing name and data_type. It is empty in case of plain output type models.
- `description`: Description of the model
- `creation_date`: The date when the model was created
- `last_updated`: The date when the model was last updated
- `number_of_versions`: Number of versions that this model has

#### Response Examples 
```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "model-1",
    "project": "project-1",
    "description": "Temperature model",
    "input_type": "structured",
    "output_type": "structured",
    "input_fields": [
      {
        "name": "input-field-1",
        "data_type": "int"
      },
      {
        "name": "input-field-2",
        "data_type": "double"
      }
    ],
    "output_fields": [
      {
        "name": "output-field",
        "data_type": "double"
      }
    ],
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "number_of_versions": 1
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "model-2",
    "project": "project-1",
    "description": "Model two",
    "input_type": "structured",
    "output_type": "plain",
    "input_fields": [
      {
        "name": "input-field",
        "data_type": "int"
      }
    ],
    "output_fields": [],
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z",
    "number_of_versions": 2
  },
  {
    "id": "bd3fae9d-aeec-4cf3-8ef0-5f9224d41904",
    "name": "model-3",
    "description": "",
    "project": "project-1",
    "input_type": "plain",
    "output_type": "plain",
    "input_fields": [],
    "output_fields": [],
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "number_of_versions": 1
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List models in project
        api_response = api_instance.models_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->models_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ModelList]**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_update**
> ModelList models_update(project_name, model_name, data)

Update a model


### Description 
Update a model. It is only possible to update the name and description fields.

### Optional Parameters 
- `name`: New name for the model
- `description`: New description for the model

#### Request Examples
```
{
  "name": "new-model-name"
}
```

### Response Structure 
Details of the updated model
- `id`: Unique identifier for the model (UUID)
- `name`: Name of the model
- `project`: Project name in which the model is defined
- `input_type`: Type of the input of the model
- `output_type`: Type of the output of the model
- `input_fields`: The list of model input fields containing name and data_type
- `output_fields`: The list of model output fields containing name and data_type
- `description`: Description of the model
- `creation_date`: The date when the model was created
- `last_updated`: The date when the model was last updated
- `number_of_versions`: Number of versions that this model has

#### Response Examples
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-model-name",
  "project": "project-1",
  "description": "New model description",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ],
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "number_of_versions": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = ubiops.ModelUpdate() # ModelUpdate | 

    try:
        # Update a model
        api_response = api_instance.models_update(project_name, model_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->models_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**ModelUpdate**](ModelUpdate.md)|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_subscriptions_list**
> list[OrganizationSubscriptionList] organization_subscriptions_list(organization_name)

List subscriptions for an organization


### Description
List the history of subscriptions of an organization. The user making the request must be admin of the organization.

### Response Structure
A list of details of the subscriptions that the organization has had
- `id`: Unique identifier for the organization (UUID) 

- `subscription`: Name of the subscription 

- `start_date`: Date the subscription started 

- `subscription_agreement_user`: Email of the user who accepted the terms of subscription
- `subscription_update_user`: Email of the user who updated the subscription to the current one

#### Response Examples
```
[
  {
    "id": "56b26bcb-34b6-4c4d-a4aa-9d625e0aa9e2",
    "subscription": "professional",
    "start_date": "2020-07-08",
    "subscription_agreement_user": "test-user@test.com",
    "subscription_update_user": ""test-user-2@test.com"
  },
  {
    "id": "3a27e5f8-b247-4866-a08c-5df136b6034c",
    "subscription": "starter",
    "start_date": "2020-06-01",
    "subscription_agreement_user": "test-user@test.com",
    "subscription_update_user": ""
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 

    try:
        # List subscriptions for an organization
        api_response = api_instance.organization_subscriptions_list(organization_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_subscriptions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**list[OrganizationSubscriptionList]**](OrganizationSubscriptionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_usage_details_get**
> list[UsagePerDay] organization_usage_details_get(organization_name, month=month)

Get resource usage details


### Description 
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per day.

### Optional Parameters 
- `month`: date indicating the month to fetch usage data for, formatted `YYYY-MM`. If omitted defaults to the current month

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (model version, pipeline or connector)
 - `usage`: an array of objects each containing the following:
     - `day`: Timestamp denoting the start of the day
     - `value`: Aggregated metric value for the given unit over the given day

#### Response Examples
```
[
  {
    "object_type": "model_version",
    "metric": "gb_seconds",
    "usage": [
      {
        "day": "2020-07-29T00:00:00Z",
        "value": 4200
      },
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 840
      },
      {
        "day": "2020-07-30T00:00:00Z",
        "value": 960
      }
    ]
  },
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 1098
      },
      {
        "day": "2020-07-06T00:00:00Z",
        "value": 18
      },
      {
        "day": "2020-07-16T00:00:00Z",
        "value": 9
      },
      {
        "day": "2020-07-15T00:00:00Z",
        "value": 117
      },
      {
        "day": "2020-07-08T00:00:00Z",
        "value": 90
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
month = 'month_example' # str |  (optional)

    try:
        # Get resource usage details
        api_response = api_instance.organization_usage_details_get(organization_name, month=month)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_usage_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **month** | **str**|  | [optional] 

### Return type

[**list[UsagePerDay]**](UsagePerDay.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_usage_get**
> list[UsagePerMonth] organization_usage_get(organization_name, start_month=start_month)

Get resource usage


### Description 
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per month.

### Optional Parameters 
- `start_month`: date indicating the start month to fetch usage data from, formatted `YYYY-MM`. If omitted results are generated from one year ago.

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (model version, pipeline or connector)
 - `usage`: an array of objects each containing the following:
     - `month`: Timestamp denoting the start of the month
     - `value`: Aggregated metric value for the given unit over the given month

#### Response Examples
```
[
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "month": "2019-08-01T00:00:00Z",
        "value": 1840
      },
      {
        "month": "2019-09-01T00:00:00Z",
        "value": 400
      },
      {
        "month": "2019-10-01T00:00:00Z",
        "value": 1204
      },
      {
        "month": "2019-11-01T00:00:00Z",
        "value": 1598
      },
      {
        "month": "2019-12-01T00:00:00Z",
        "value": 824
      },
      {
        "month": "2020-01-01T00:00:00Z",
        "value": 2036
      },
      {
        "month": "2020-02-01T00:00:00Z",
        "value": 1438
      },
      {
        "month": "2020-03-01T00:00:00Z",
        "value": 932
      },
      {
        "month": "2020-04-01T00:00:00Z",
        "value": 528
      },
      {
        "month": "2020-05-01T00:00:00Z",
        "value": 1484
      },
      {
        "month": "2020-06-01T00:00:00Z",
        "value": 1942
      },
      {
        "month": "2020-07-01T00:00:00Z",
        "value": 1332
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
start_month = 'start_month_example' # str |  (optional)

    try:
        # Get resource usage
        api_response = api_instance.organization_usage_get(organization_name, start_month=start_month)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_usage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **start_month** | **str**|  | [optional] 

### Return type

[**list[UsagePerMonth]**](UsagePerMonth.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_create**
> OrganizationUserDetail organization_users_create(organization_name, data)

Add a user to an organization


### Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters
- `email`: Email of the user 

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure 
Details of the added user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
data = ubiops.OrganizationUserCreate() # OrganizationUserCreate | 

    try:
        # Add a user to an organization
        api_response = api_instance.organization_users_create(organization_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUserCreate**](OrganizationUserCreate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_delete**
> organization_users_delete(organization_name, user_id)

Delete a user from an organization


### Description 
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        # Delete a user from an organization
        api_instance.organization_users_delete(organization_name, user_id)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_get**
> OrganizationUserDetail organization_users_get(organization_name, user_id)

Get details of a user in an organization


### Description 
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure 
Details of the user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        # Get details of a user in an organization
        api_response = api_instance.organization_users_get(organization_name, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_list**
> list[OrganizationUserDetail] organization_users_list(organization_name)

List the users in an organization


### Description 
List users and their details in an organization

### Response Structure 
List of details of users
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples
```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 

    try:
        # List the users in an organization
        api_response = api_instance.organization_users_list(organization_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**list[OrganizationUserDetail]**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_update**
> OrganizationUserDetail organization_users_update(organization_name, user_id, data)

Update details of a user in an organization


### Description 
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters
- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "admin": true
}
```

### Response Structure
Details of the user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 
data = ubiops.OrganizationUserUpdate() # OrganizationUserUpdate | 

    try:
        # Update details of a user in an organization
        api_response = api_instance.organization_users_update(organization_name, user_id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organization_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**OrganizationUserUpdate**](OrganizationUserUpdate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_create**
> OrganizationList organizations_create(data)

Create organizations


### Description 
Create a new organization. When a user creates an organization, s/he will automatically become an organization admin.

### Required Parameters 
- `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `subscription`: Name of the subscription for the organization
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted

### Optional Parameters 
- `subscription_end_date`: End date of the subscription. The subscription will be cancelled on this date. A 'free' subscription cannot have a custom end_date as this subscription is always valid for a year.

#### Request Examples 
```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true
}
```

```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true,
  "subscription_end_date": "2021-03-25"
}
```

### Response Structure 
Details of the created organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Date and time the organization was created 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    data = ubiops.OrganizationCreate() # OrganizationCreate | 

    try:
        # Create organizations
        api_response = api_instance.organizations_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organizations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OrganizationCreate**](OrganizationCreate.md)|  | 

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> OrganizationDetail organizations_get(organization_name)

Get details of an organization


### Description 
Get the details of an organization

### Response Structure 
Details of the organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Time the organization was created 

- `subscription`: Name of the subscription 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 

    try:
        # Get details of an organization
        api_response = api_instance.organizations_get(organization_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> list[OrganizationList] organizations_list()

List organizations


### Description 
List all organizations where the user making the request is a member

### Response Structure
A list of details of the organizations
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Date and time the organization was created 


#### Response Examples
```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # List organizations
        api_response = api_instance.organizations_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organizations_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrganizationList]**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_resource_usage**
> ResourceUsage organizations_resource_usage(organization_name)

List resource usage of an organization


### Description 
List the total number of resources used by this organization

### Response Structure
A list containing the number of
- projects 

- users 

- models 

- versions 

- connectors 

- pipelines 

currently used by the organization.

#### Response Examples
```
{
  "projects": 5,
  "users": 3,
  "models": 30,
  "versions": 47,
  "connectors": 1,
  "pipelines": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 

    try:
        # List resource usage of an organization
        api_response = api_instance.organizations_resource_usage(organization_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organizations_resource_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**ResourceUsage**](ResourceUsage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> OrganizationDetail organizations_update(organization_name, data)

Update details of an organization


### Description 
Update an organization. The user making the request must be admin of the organization. Users are able to update the name of the organization, but changes to the subscription can only be done by Dutch Analytics.
To delete the end date of the current subscription, give the 'subscription_end_date' parameter with value null.

### Optional Parameters 
- `name`: New organization name
- `subscription`: New subscription
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted upon upgrading the subscription
- `subscription_end_date`: End date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will be cancelled on this date. If the subscription_end_date was previously set, but should be removed, give a null value for 'subscription_end_date'.

#### Request Examples


```
{
  "name": "new-organization-name"
}
```
```
{
  "subscription": "professional",
  "subscription_agreed": true
}
```
```
{
  "subscription_end_date": "2020-08-30",
  "subscription_agreed": true
}
```

### Response Structure 
Details of the organization
- `id`: Unique identifier for the organization (UUID) 

- `name`: Name of the organization 

- `creation_date`: Time the organization was created 

- `subscription`: Name of the subscription 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    organization_name = 'organization_name_example' # str | 
data = ubiops.OrganizationUpdate() # OrganizationUpdate | 

    try:
        # Update details of an organization
        api_response = api_instance.organizations_update(organization_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->organizations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_list**
> list[PermissionList] permissions_list()

List the available permissions


### Description 
List all the available permissions which can be used to create custom roles.

### Response Structure 
A list of available permissions
 - `name`: Name of the permission 



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # List the available permissions
        api_response = api_instance.permissions_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->permissions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PermissionList]**](PermissionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_create**
> Attachments pipeline_object_attachments_create(project_name, pipeline_name, data)

Create object attachments


### Description 
Create an attachment between two pipeline objects. An attachment can only be made between two objects that have already been added to the pipeline. 
The object where the attachment starts is called the source object. The object that is linked is called the destination object. When attaching two objects, one must also define which source object output fields map to which destination object input fields.
All the input fields in the destination object must be provided in the mapping. In contrast, not all source object output fields need to be used in the mapping. It is also possible that one source output field may link to multiple destination input fields.

A *connector* object can only be a destination object.

The *pipeline_start* object can only be a source object.

In case of plain type of objects, the mapping must be omitted or given as an empty list.

When creating attachments for a blob connector, use the *blob* field in the mapping.

### Required Parameters 
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name keys. The source and destination fields should match in data type, e.g. integer source fields can only be mapped to integer type destination fields.

#### Request Examples 
An attachment between a model version and connector
```
{
  "source_name": "model-1-v1",
  "destination_name": "connector-1",
  "mapping": [
    {
      "source_field_name": "model-output-field-1",
      "destination_field_name": "connector-field-1"
    },
    {
      "source_field_name": "model-output-field-2",
      "destination_field_name": "connector-field-2"
    },
    {
      "source_field_name": "model-output-field-3",
      "destination_field_name": "connector-field-3"
    }
  ]
}
```

```
{
  "source_name": "blob-model-v3",
  "destination_name": "s3-connector",
  "mapping": []
}
```
 
An attachment between a pipeline and model version
```
{
  "source_name": "pipeline_start",
  "destination_name": "model-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "model-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "model-input-field-2"
    }
  ]
}
```

### Response Structure 
Details of the created attachment
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
{
  "source_name": "pipeline-1",
  "destination_name": "model-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "model-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "model-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.AttachmentsCreate() # AttachmentsCreate | 

    try:
        # Create object attachments
        api_response = api_instance.pipeline_object_attachments_create(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**AttachmentsCreate**](AttachmentsCreate.md)|  | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_delete**
> pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)

Delete attachment of a source and destination object


### Description 
Delete an attachment in a pipeline. The referenced and original objects of the attachment still exist in the pipeline, only the link between them is deleted.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

    try:
        # Delete attachment of a source and destination object
        api_instance.pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_get**
> AttachmentsList pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)

Get an attachment of a source and destination object


### Description 
Get the details of a single attachment between a source and destination object in a pipeline

### Response Structure 
Details of the attachment
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
{
  "source_name": "model-2-v2",
  "destination_name": "model-3-v1",
  "mapping": [
    {
      "source_field_name": "model-2-output-field-1",
      "destination_field_name": "model-3-input-field-1"
    },
    {
      "source_field_name": "model-2-output-field-2",
      "destination_field_name": "model-3-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

    try:
        # Get an attachment of a source and destination object
        api_response = api_instance.pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**AttachmentsList**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_list**
> list[AttachmentsList] pipeline_object_attachments_list(project_name, pipeline_name)

List object attachments


### Description 
List all attachments in a pipeline

### Response Structure 
A list of details of the attachments in the pipeline
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
[
  {
    "source_name": "pipeline-1",
    "destination_name": "model-2-v2",
    "mapping": [
      {
        "source_field_name": "pipeline-input-field-1",
        "destination_field_name": "model-input-field-1"
      },
      {
        "source_field_name": "pipeline-input-field-2",
        "destination_field_name": "model-input-field-2"
      }
    ]
  },
  {
    "source_name": "model-2-v2",
    "destination_name": "connector-1",
    "mapping": [
      {
        "source_field_name": "model-output-field-1",
        "destination_field_name": "connector-field-1"
      },
      {
        "source_field_name": "model-output-field-2",
        "destination_field_name": "connector-field-2"
      },
      {
        "source_field_name": "model-output-field-3",
        "destination_field_name": "connector-field-3"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # List object attachments
        api_response = api_instance.pipeline_object_attachments_list(project_name, pipeline_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_source_get**
> list[AttachmentsList] pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)

List the attachments of a source object


### Description 
List attachments of a source object in a pipeline

### Response Structure 
A list of details of the attachments of the given source object in the pipeline
- `source_name`: Name of the source pipeline object
- `destination_name`: Name of the destination pipeline object
- `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
[
  {
    "source_name": "model-2-v2",
    "destination_name": "connector-1",
    "mapping": [
      {
        "source_field_name": "model-2-output-field-1",
        "destination_field_name": "connector-field-1"
      },
      {
        "source_field_name": "model-2-output-field-2",
        "destination_field_name": "connector-field-2"
      },
      {
        "source_field_name": "model-2-output-field-3",
        "destination_field_name": "connector-field-3"
      }
    ]
  },
  {
    "source_name": "model-2-v2",
    "destination_name": "model-3-v1",
    "mapping": [
      {
        "source_field_name": "model-2-output-field-1",
        "destination_field_name": "model-3-input-field-1"
      },
      {
        "source_field_name": "model-2-output-field-2",
        "destination_field_name": "model-3-input-field-2"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

    try:
        # List the attachments of a source object
        api_response = api_instance.pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_attachments_source_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_environment_variables_list**
> list[InheritedEnvironmentVariableList] pipeline_object_environment_variables_list(project_name, name, pipeline_name)

List pipeline object environment variables


### Description
List environment variables accessible to objects in the pipeline
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `model`, or `model_version`
- `inheritance_name`: Name of the parent object that this variable is inherited from

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "model",
    "inheritance_name": "model_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # List pipeline object environment variables
        api_response = api_instance.pipeline_object_environment_variables_list(project_name, name, pipeline_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_object_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_create**
> PipelineObjectList pipeline_objects_create(project_name, pipeline_name, data)

Add an object to a pipeline


### Description 
Create a pipeline object, which can either be a connector or model version. The pipeline object that is added is a reference to the real object. In this way, multiple references to the same object may be added to a pipeline.
In case of model reference_type, the reference_name refers to the model name and the version is the version of the model which will be added to the pipeline as an object.

### Required Parameters 
- `name`: Name of the pipeline object. It is unique within a pipeline
- `reference_type`: Type of the object it will reference. It can either be a model or connector
- `reference_name`: Name of the object it will reference

### Optional Parameters 
- `version`: Version name. If model is given in reference_type field, version field must be provided too. If the reference_type is connector, this field should be omitted in the request.

#### Request Examples 
An object referencing a model version
```
{
  "name": "model-1-v1",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-1"
}
```
 
An object referencing a connector
```
{
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```

### Response Structure 
Details of the created pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_type`: Type of the object it will reference
- `reference_name`: Name of the object it will reference
- `version`: Version name in case of model reference_type

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "model-1-v1",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-1"
}
```
 
```
{
  "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineObjectCreate() # PipelineObjectCreate | 

    try:
        # Add an object to a pipeline
        api_response = api_instance.pipeline_objects_create(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_objects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectCreate**](PipelineObjectCreate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_delete**
> pipeline_objects_delete(project_name, name, pipeline_name)

Delete object from pipeline

  
### Description 
Delete a pipeline object. Only the reference in the pipeline is deleted. The original object (model, model version and connector) still exists.
If the object is attached to another object, the attachment is also deleted.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # Delete object from pipeline
        api_instance.pipeline_objects_delete(project_name, name, pipeline_name)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_objects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_get**
> PipelineObjectList pipeline_objects_get(project_name, name, pipeline_name)

Get an object in a pipeline


### Description 
Retrieve the details of a single pipeline object

### Response Structure 
Details of the pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_type`: Type of the object it references
- `reference_name`: Name of the object it references
- `version`: Version name in case of model reference_type

#### Response Examples 
A dictionary containing details of the pipeline object
```
{
  "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # Get an object in a pipeline
        api_response = api_instance.pipeline_objects_get(project_name, name, pipeline_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_objects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_list**
> list[PipelineObjectList] pipeline_objects_list(project_name, pipeline_name)

List objects in a pipeline


### Description 
List all pipeline objects (connectors/models) in a pipeline

### Response Structure 
A list of details of the pipeline objects in the pipeline
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_type`: Type of the object it references
- `reference_name`: Name of the object it references
- `version`: Version name in case of model reference_type

#### Response Examples 
```
A list of pipeline objects
[
  {
    "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
    "name": "model-1-v1",
    "reference_type": "model",
    "reference_name": "model-1",
    "version": "version-1"
  },
  {
    "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
    "name": "s3-connector",
    "reference_type": "connector",
    "reference_name": "s3-connector"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # List objects in a pipeline
        api_response = api_instance.pipeline_objects_list(project_name, pipeline_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_objects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[PipelineObjectList]**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_update**
> PipelineObjectList pipeline_objects_update(project_name, name, pipeline_name, data)

Update an object in a pipeline


### Description 
Update a pipeline object. It is not possible to update the reference_name and reference_type. All necessary fields are validated again.

### Optional Parameters 
- `name`: New name for the pipeline object
- `version`: New version for the pipeline object. Since the input/output fields of different model versions are the same, the version of a model pipeline object can be changed with another version of the same model.

#### Request Examples 
```
{
  "name": "new-pipeline-object-name"
}
```
 
```
{
  "name": "model-1-v2"
  "version": "version-2"
}
```

### Response Structure 
Details of the updated pipeline object
- `id`: Unique identifier for the pipeline object (UUID)
- `name`: Name of the pipeline object
- `reference_type`: Type of the object it references
- `reference_name`: Name of the object it references
- `version`: Version name in case of model reference_type

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "model-1-v2",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-2"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineObjectUpdate() # PipelineObjectUpdate | 

    try:
        # Update an object in a pipeline
        api_response = api_instance.pipeline_objects_update(project_name, name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipeline_objects_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectUpdate**](PipelineObjectUpdate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_create**
> PipelineList pipelines_create(project_name, data)

Create pipelines


### Description 
Create a pipeline in a project. 

The input_fields represent the fields that the input data for pipeline requests should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters 
- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the connector. It can be either structured or plain.
- `input_fields`: A list of fields with name and data_type. In case of plain pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, they must be provided.

### Optional Parameters
- `description`: Description of the pipeline

#### Request Examples 
A structured pipeline
```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```
 
A plain pipeline
```
{
  "name": "pipeline-2",
  "input_type": "plain",
  "description": "my description"
}
```

### Response Structure 
Details of the created pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description`: Description of the pipeline
- `project`: Project name in which the pipeline is created
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "name": "pipeline-1",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ],
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-03-24T09:43:51.791253Z"
}
```
 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.PipelineCreate() # PipelineCreate | 

    try:
        # Create pipelines
        api_response = api_instance.pipelines_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_delete**
> pipelines_delete(project_name, pipeline_name)

Delete pipeline


### Description 
Delete a pipeline. This will also delete all objects and attachments in the pipeline.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # Delete pipeline
        api_instance.pipelines_delete(project_name, pipeline_name)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get**
> PipelineList pipelines_get(project_name, pipeline_name)

Get pipeline


### Description 
Get the details of a single pipeline

### Response Structure 
Details of the pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description` Description of the pipeline
- `project`: Project name in which the pipeline is defined
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

    try:
        # Get pipeline
        api_response = api_instance.pipelines_get(project_name, pipeline_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_list**
> list[PipelineList] pipelines_list(project_name)

List pipelines


### Description 
List all pipelines in a project

### Response Structure 
A list of details of the pipelines in the project
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description of the pipeline
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "name": "pipeline-1",
    "project": "project-1",
    "description": "my description",
    "input_type": "structured",
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
    "name": "pipeline-2",
    "project": "project-1",
    "description": "my description",
    "input_type": "plain",
    "input_fields": [],
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List pipelines
        api_response = api_instance.pipelines_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[PipelineList]**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_request**
> PipelineRequestList pipelines_request(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, model_timeout=model_timeout)

Make a request to a pipeline


### Description 
Make a pipeline request. This method returns all the results of the model requests made within the pipeline.

### Required Parameters 
A dictionary which contains the input fields of the pipeline as keys

### Optional Parameters
These parameters should be given as GET parameters
- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 and the default value is 3600.
- `model_timeout`: Timeout for each model request in the pipeline in seconds.  The maximum allowed value is 3600 and the default value is 300.
Maximum allowed value for both is 3600 seconds and the default value is 300 seconds.

#### Request Examples
```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

### Response Structure 
- `project`: Name of the project in which the request is made
- `pipeline`: Name of the pipeline for which the request is made
- `pipeline_request_id`: Unique identifier for the pipeline request
- `model_requests`: A list of dictionaries containing the results of the model requests made for the model objects in the pipeline. The dictionaries contain the following fields:
    - `request_id`: Unique identifier for the model request
    - `pipeline_object`: Name of the object in the pipeline
    - `success`: A boolean value that indicates whether the model request was successful
    - `request_data`: Input data for the model request
    - `result`: Model request result value. NULL if the request failed.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful. 

#### Response Examples
```
{
  "project": "project-1",
  "pipeline": "pipeline-1",
  "pipeline_request_id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "model_requests": [
    {
      "request_id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "model-object-1",
      "success": true,
      "request_data": {
        "model-1-input-field-1": 5,
        "model-1-input-field-2": 0.4
      },
      "result": {
        "model-1-output-field-1": 0.23,
        "model-1-output-field-2": 10
      },
      "error_message": None 
    },
    {
      "request_id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "model-object-2",
      "success": false,
      "request_data": {
        "model-2-input-field": 10
      },
      "result": None,
      "error_message": "Invalid message format" 
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineRequestCreate() # PipelineRequestCreate | 
pipeline_timeout = 56 # int |  (optional)
model_timeout = 56 # int |  (optional)

    try:
        # Make a request to a pipeline
        api_response = api_instance.pipelines_request(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, model_timeout=model_timeout)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineRequestCreate**](PipelineRequestCreate.md)|  | 
 **pipeline_timeout** | **int**|  | [optional] 
 **model_timeout** | **int**|  | [optional] 

### Return type

[**PipelineRequestList**](PipelineRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_update**
> PipelineList pipelines_update(project_name, pipeline_name, data)

Update pipeline


    
### Description 
Update a pipeline. All necessary fields are validated again.

### Optional Parameters 
- `name`: New name for the pipeline
- `description`: New description for the pipeline
- `input_type`: New type for the pipeline. It is possible to change the type from plain to structured and vice versa.
- `input_fields`: New input fields for the pipeline.

If the type of pipeline is updated to plain, the input fields are deleted. In this case, input_fields should either be omitted or provided as en empty list.
If the type of pipeline is updated to structured, the old fields are deleted, if there existed any. The new fields are created. If one or more old fields need to be kept, they must be provided again.

#### Request Examples 
```
{
  "name": "new-pipeline-name"
}
```

```
{
  "description": "New pipeline description"
}
```

```
{
  "input_type": "plain"
}
```
 
```
{
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ]
}
```

### Response Structure 
Details of the updated pipeline
- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description for the pipeline
- `input_type`: Type of the pipeline
- `input_fields`: A list of pipeline fields with name and data_type
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "new-pipeline-name",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ],
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = ubiops.PipelineCreate() # PipelineCreate | 

    try:
        # Update pipeline
        api_response = api_instance.pipelines_update(project_name, pipeline_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->pipelines_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_create**
> EnvironmentVariableList project_environment_variables_create(project_name, data)

Create project environment variable


### Description
Create an environment variable for the project. This variable will be inherited by all models in this project.

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```

```
{
  "name": "database_password",
  "value": "password",
  "secret": true
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```

```
{
  "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
  "name": "database_password",
  "value": null,
  "secret": true
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Create project environment variable
        api_response = api_instance.project_environment_variables_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->project_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_delete**
> project_environment_variables_delete(project_name, id)

Delete project environment variable


### Description
Delete an environment variable of the project


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

    try:
        # Delete project environment variable
        api_instance.project_environment_variables_delete(project_name, id)
    except ApiException as e:
        print("Exception when calling CoreApi->project_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_get**
> EnvironmentVariableList project_environment_variables_get(project_name, id)

Get project environment variable


### Description
Retrieve details of a project environment variable.

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

    try:
        # Get project environment variable
        api_response = api_instance.project_environment_variables_get(project_name, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->project_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_list**
> list[EnvironmentVariableList] project_environment_variables_list(project_name)

List project environment variables


### Description
List the environment variables defined for the project. These are the variables that are inherited by all models in this project.
 
### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List project environment variables
        api_response = api_instance.project_environment_variables_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->project_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[EnvironmentVariableList]**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_update**
> EnvironmentVariableList project_environment_variables_update(project_name, id, data)

Update project environment variable


### Description
Update an environment variable for the projects

### Required Parameters
- `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore. 
- `value`: The value of the variable as a string. It may be an empty string. 
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets). 

#### Request Examples
```
{
  "name": "database_schema",
  "value": "new+schema",
  "secret": false
}
```

### Response Structure 
A list of variables described by the following fields:
- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "new_schema",
  "secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

    try:
        # Update project environment variable
        api_response = api_instance.project_environment_variables_update(project_name, id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->project_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_usage_get**
> list[UsagePerMonth] project_usage_get(project_name, start_month=start_month)

Get resource usage


### Description 
Get resource usage for the project. This returns a list of metrics that are used for billing, aggregated per month.

### Optional Parameters 
- `start_month`: date indicating the start month to fetch usage data from, formatted `YYYY-MM`. If omitted results are generated from one year ago.

### Response Structure 
 - `metric`: The metric that was measured
 - `object_type`: Type of object the metric was measured for (model version, pipeline or connector)
 - `usage`: an array of objects each containing the following:
     - `month`: Timestamp denoting the start of the month
     - `value`: Aggregated metric value for the given unit over the given month

#### Response Examples
```
[
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "month": "2019-08-01T00:00:00Z",
        "value": 1840
      },
      {
        "month": "2019-09-01T00:00:00Z",
        "value": 400
      },
      {
        "month": "2019-10-01T00:00:00Z",
        "value": 1204
      },
      {
        "month": "2019-11-01T00:00:00Z",
        "value": 1598
      },
      {
        "month": "2019-12-01T00:00:00Z",
        "value": 824
      },
      {
        "month": "2020-01-01T00:00:00Z",
        "value": 2036
      },
      {
        "month": "2020-02-01T00:00:00Z",
        "value": 1438
      },
      {
        "month": "2020-03-01T00:00:00Z",
        "value": 932
      },
      {
        "month": "2020-04-01T00:00:00Z",
        "value": 528
      },
      {
        "month": "2020-05-01T00:00:00Z",
        "value": 1484
      },
      {
        "month": "2020-06-01T00:00:00Z",
        "value": 1942
      },
      {
        "month": "2020-07-01T00:00:00Z",
        "value": 1332
      }
    ]
  }
]

```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
start_month = 'start_month_example' # str |  (optional)

    try:
        # Get resource usage
        api_response = api_instance.project_usage_get(project_name, start_month=start_month)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->project_usage_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **start_month** | **str**|  | [optional] 

### Return type

[**list[UsagePerMonth]**](UsagePerMonth.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create**
> ProjectList projects_create(data)

Create projects


### Description 
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters 
- `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `organization_name`: Name of the organization in which the project is going to be created
 
#### Request Examples 
```
{
  "name": "project-1",
  "organization_name": "organization-1"
}
```

### Response Structure 
Details of the created project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    data = ubiops.ProjectCreate() # ProjectCreate | 

    try:
        # Create projects
        api_response = api_instance.projects_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete**
> projects_delete(project_name)

Delete a project


### Description 
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the models, connectors and pipelines defined in it are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # Delete a project
        api_instance.projects_delete(project_name)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> ProjectList projects_get(project_name)

Get details of a project


### Description 
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure 
Details of a project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # Get details of a project
        api_response = api_instance.projects_get(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> list[ProjectList] projects_list()

List projects


### Description 
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "organization_name": "organization-2"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # List projects
        api_response = api_instance.projects_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectList]**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_log_list**
> list[Logs] projects_log_list(project_name, data)

List logs for a project


### Description 
Retrieve the logs of all objects in a project, including models, pipelines, connectors and requests. Using filters you can filter the logs on the objects and information of your choice. 

### Required Parameters 
- `filters`: A dictionary containing information to filter logs on. It may contain zero or more of the following fields: 

    - `model_name`: name of a model 

    - `model_version`: a version name. If this field is present in the request, model_name must also be given. The versions are only meaningful in combination with the models they are defined for. 

    - `connector_name`: name of a connector 

    - `pipeline_name`: name of a pipeline 

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name must also be given. The pipeline objects are only meaningful in combination with the pipelines they are defined in. 

    - `request_id`: the UUID of a model request 

    - `pipeline_request_id`: the UUID of a pipeline request 

    - `system`: whether the log was generated by the system or user code (true / false) 


Any combination of filters may be given in the request. For example, if only a model_name is provided, all logs for that model are returned. These logs can contain information from all the pipelines that model is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.

### Optional Parameters 
- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date. 

- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500. 
 
- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value. 

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned. 

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned. 
 
    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).
    
If no date or id is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

#### Request Examples 
```
{
  "filters": {
    "model_name": "model-1",
    "model_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z"
}
```

```
{
  "filters": {
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1"
  },
  "id": "41d7a7c5cd025e3501a00000",
  "date_range": -100
}
```
 
```
{
  "filters": {
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1"
  },
  "date_range": 100
}
```

```
{
  "filters": {
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1"
  },
  "date": "2020-01-01T00:00:00.000000Z",
  "date_range": -86400,
  "limit": 5
}
```

### Response Structure 
A list of log details
- `id`: Unique UUID of the log line 

- `log`: Log line text 

- `date`: Time the log line was created
 
The following fields will be returned on response if they are set for the log line:
- `connector_name`:  The connector which the log is related to 

- `model_name`:  The model which the log is related to 

- `model_version`:  The model version which the log is related to 

- `pipeline_name`:  The pipeline which the log is related to 

- `pipeline_object_name`: The pipeline object which the log is related to 

- `request_id`:  The model request the log is related to 

- `pipeline_request_id`:  The pipeline request the log is related to 

- `system`:  Whether the log was generated by the system (true / false)

#### Response Examples 
Logs for a specific model and version
```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "model_name": "model-1",
    "model_version": "v1",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "model_name": "model-1",
    "model_version": "v1",
    "pipeline_name": "pipeline-2",
    "pipeline_object_name": "model-1-v1-object",
    "pipeline_trace_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "[Error] Model call result (failed)"
  }
]
```
 
Logs for a specific pipeline
```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "model_name": "model-2",
    "model_version": "v2",
    "pipeline_name": "pipeline-1",
    "pipeline_object_name": "model-2-v2-object",
    "pipeline_trace_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Model call result (success): 0.2316"
  },
  {
    "id": "5dcad12ba76a2c6e4331f193",
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1",
    "pipeline_object_name": "s3-connector-object",
    "pipeline_trace_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "Could not connect to database: connection timed out"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.LogsCreate() # LogsCreate | 

    try:
        # List logs for a project
        api_response = api_instance.projects_log_list(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**LogsCreate**](LogsCreate.md)|  | 

### Return type

[**list[Logs]**](Logs.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_resource_usage**
> ProjectResourceUsage projects_resource_usage(project_name)

List resource usage of a project


### Description 
List the total number of resources used in a project

### Response Structure
A list containing the number of
- models 

- versions 

- connectors 

- pipelines 

currently defined in the project.

#### Response Examples
```
{
  "models": 30,
  "versions": 47,
  "connectors": 1,
  "pipelines": 2
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List resource usage of a project
        api_response = api_instance.projects_resource_usage(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_resource_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**ProjectResourceUsage**](ProjectResourceUsage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update**
> ProjectList projects_update(project_name, data)

Update a project


### Description 
Update the name of a single project. The user making the request must have appropriate permissions.

### Optional Parameters 
- `name`: New project name

#### Request Examples 
```
{
  "name": "project-name-example"
}
```

### Response Structure 
Details of a project
- `id`: Unique identifier for the project (UUID) 

- `name`: Name of the project 

- `creation_date`: Time the project was created 

- `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.ProjectUpdate() # ProjectUpdate | 

    try:
        # Update a project
        api_response = api_instance.projects_update(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->projects_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_create**
> RoleAssignmentList role_assignments_create(project_name, data)

Assign a role to a user in a project


### Description 
Assign a role to a user in the scope of a project. This role can be assigned on either project level or on object level, which can be a model, credentials, connector or pipeline.
The user making the request must have appropriate permissions.

### Required Parameters 
- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role to be assigned to the user 


### Optional Parameters
- `object_name`: Name of the object for which the role will be assigned 

- `object_type`: Type of the object for which the role will be assigned. It can be project, model, credentials, connector or pipeline.

**object_name and object_type must be provided together. If neither of them is provided, the role is set on project level.**

#### Request Examples
Setting the role model-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-admin"
}
```

Setting the role model-viewer on model-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```

### Response Structure 
Details of the created role assignment
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.

#### Response Examples
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-admin",
  "object_name": "project-1",
  "object_type": "project"
}
```

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.RoleAssignmentCreate() # RoleAssignmentCreate | 

    try:
        # Assign a role to a user in a project
        api_response = api_instance.role_assignments_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->role_assignments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleAssignmentCreate**](RoleAssignmentCreate.md)|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_delete**
> role_assignments_delete(project_name, id)

Delete a role from a user with the given role assignment id


### Description 
Delete a role of a user. The user making the request must have appropriate permissions. It is possible for a user to delete their own role if they have permissions to do so.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

    try:
        # Delete a role from a user with the given role assignment id
        api_instance.role_assignments_delete(project_name, id)
    except ApiException as e:
        print("Exception when calling CoreApi->role_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_get**
> RoleAssignmentList role_assignments_get(project_name, id)

Get details of a role assignment


### Description 
Get the details of a role assignment of a user. The user making the request must have appropriate permissions.

### Response Structure 
Details of the role assignment
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

    try:
        # Get details of a role assignment
        api_response = api_instance.role_assignments_get(project_name, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->role_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_per_user_list**
> list[RoleAssignmentList] role_assignments_per_user_list(project_name, user_id)

List the roles assigned to a specific user in a project


### Description 
List the roles assigned to a user in the scope of a project. 

### Response Structure
- `id`: Unique identifier for the role assignment (UUID) 

- `user_id`: Unique identifier for the user (UUID) 

- `role`: Name of the role assigned to the user 

- `object_name`: Name of the object for which the role is assigned 

- `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "model-viewer",
    "object_name": "model-1",
    "object_type": "model"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "connector-admin",
    "object_name": "connector-1",
    "object_type": "connector"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        # List the roles assigned to a specific user in a project
        api_response = api_instance.role_assignments_per_user_list(project_name, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->role_assignments_per_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**list[RoleAssignmentList]**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_create**
> RoleDetailList roles_create(project_name, data)

Create a custom role scoped in a project


### Description 
Create a custom role in the scope of a project. This role is not accessible from other projects. 
The user making the request must have appropriate permissions.

### Required Parameters 
- `name`: Name of the role which will be created. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `permissions`: A list of permissions which the role will contain. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "custom-model-editor-role",
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```

### Response Structure 
Details of the created role
- `id`: Unique identifier for the created role (UUID) 

- `name`: Name of the created role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-model-editor-role",
  "default": false,
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.RoleCreate() # RoleCreate | 

    try:
        # Create a custom role scoped in a project
        api_response = api_instance.roles_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleCreate**](RoleCreate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_delete**
> roles_delete(project_name, role_name)

Delete a role from a project


### Description 
Delete a role from a project. The user making the request must have appropriate permissions.
**Default roles cannot be deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

    try:
        # Delete a role from a project
        api_instance.roles_delete(project_name, role_name)
    except ApiException as e:
        print("Exception when calling CoreApi->roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_get**
> RoleDetailList roles_get(project_name, role_name)

Get details of a role


### Description 
Get the details of a role. The user making the request must have appropriate permissions.

### Response Structure
Details of the role
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-model-editor-role",
  "default": false,
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

    try:
        # Get details of a role
        api_response = api_instance.roles_get(project_name, role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_list**
> list[RoleList] roles_list(project_name)

List the available roles in a project


### Description 
List the roles available in the scope of a project. Information on which permissions each role contains, can be obtained with a call to get details of a single role.

### Response Structure
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the role 

- `default`: A boolean value that indicates whether the role is a default role or not 


#### Response Examples
```
[
  {
    "id": "34e53855-9b50-47bc-b516-6cb971b1949c",
    "name": "project-admin",
    "default": true
  },
  {
    "id": "00132911-b5dd-4017-b399-85f3ffd2a7c3",
    "name": "project-editor",
    "default": true
  },
  {
    "id": "bf0d5823-8062-40f6-bbd2-21bc732f3c3b",
    "name": "project-viewer",
    "default": true
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List the available roles in a project
        api_response = api_instance.roles_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[RoleList]**](RoleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_update**
> RoleDetailList roles_update(project_name, role_name, data)

Update a role in a project


### Description 
Update a role in a project. The user making the request must have appropriate permissions.
**Default roles cannot be updated.**

### Optional Parameters 
- `name`: New name for the role. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `permissions`: A new list of permissions which the role will contain. The previous permissions will be replaced with the given ones. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "new-model-editor-role",
  "permissions": [
    "models.list",
    "models.get"
  ]
}
```

### Response Structure 
Details of the updated role
- `id`: Unique identifier for the role (UUID) 

- `name`: Name of the updated role 

- `default`: A boolean value that indicates whether the role is a default role or not 

- `permissions`: A list of permissions which the role contains

#### Response Examples
```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "new-model-editor-role",
  "default": false,
  "permissions": [
    "models.list",
    "models.get"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 
data = ubiops.RoleUpdate() # RoleUpdate | 

    try:
        # Update a role in a project
        api_response = api_instance.roles_update(project_name, role_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 
 **data** | [**RoleUpdate**](RoleUpdate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_requests_create**
> ScheduleList scheduled_requests_create(project_name, data)

Create scheduled requests


### Description 
Create a new scheduled request with the provided name

### Required Parameters 
- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `object_type`: Type of object for which the request is made. Can be either 'model' or 'pipeline'. 

- `object_name`: Name of model or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 


### Optional Parameters
- `version`: Name of version if type of object is 'model' 

- `request_data`: Input data for the scheduled request. For structured models/pipelines, it must be a dictionary. 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds. This field is not used for batch requests. 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled. Default is 'True'. 


#### Request Examples 
```
{
  "name": "test-request",
  "object_type": "model",
  "object_name": "test-model",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 300,
  "enabled": true
}
```

### Response Structure 
Details of the created scheduled request
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of model or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'model' 

- `request_data`: Input data for the scheduled request 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled 

- `creation_date`: The date when the scheduled request was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "model",
  "object_name": "test-model",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 300,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.ScheduleCreate() # ScheduleCreate | 

    try:
        # Create scheduled requests
        api_response = api_instance.scheduled_requests_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->scheduled_requests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ScheduleCreate**](ScheduleCreate.md)|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_requests_delete**
> scheduled_requests_delete(project_name, schedule_name)

Delete a scheduled request


### Description 
Delete the scheduled request from the project. 

If you want to temporarily disable a scheduled request, update the request with `enabled` set to False.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 

    try:
        # Delete a scheduled request
        api_instance.scheduled_requests_delete(project_name, schedule_name)
    except ApiException as e:
        print("Exception when calling CoreApi->scheduled_requests_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_requests_get**
> ScheduleList scheduled_requests_get(project_name, schedule_name)

Get details of a scheduled request


### Description 
Retrieve details of a single scheduled request

### Response Structure 
Details of a scheduled request
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of model or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'model' 

- `request_data`: Input data for the scheduled request 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled 

- `creation_date`: The date when the scheduled request was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "model",
  "object_name": "test-model",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 200,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 

    try:
        # Get details of a scheduled request
        api_response = api_instance.scheduled_requests_get(project_name, schedule_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->scheduled_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_requests_list**
> list[ScheduleList] scheduled_requests_list(project_name)

List scheduled requests


### Description 
List the scheduled requests in a project. The user has to have 'requests.list' permission on either 'models.versions' or 'pipelines' to list the scheduled requests.

### Response Structure 
A list of details of all scheduled requests in a project
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of model or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'model' 

- `request_data`: Input data for the scheduled request 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled 

- `creation_date`: The date when the scheduled request was created

#### Response Examples 
```
[
    {
      "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
      "name": "test-request",
      "object_type": "model",
      "object_name": "test-model",
      "version": "v1",
      "schedule": "0 * 3 * *",
      "request_data": {
        "input_field_1": 2345,
        "input_field_2": 8765
      },
      "batch": false,
      "timeout": 200",
      "enabled": true,
      "creation_date": "2020-09-16T08:06:34.457679Z"
    }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List scheduled requests
        api_response = api_instance.scheduled_requests_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->scheduled_requests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ScheduleList]**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_requests_update**
> ScheduleList scheduled_requests_update(project_name, schedule_name, data)

Update a scheduled request


### Description 
Update a scheduled request in a project. Create permissions on the object are necessary for this action.

### Optional Parameters
- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

- `schedule`: Schedule in crontab format 

- `request_data`: Input data for the scheduled request. For structured models/pipelines, it must be a dictionary. 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled. Default is 'True'. 


#### Request Examples 
```
{
  "name": "test-request",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": true,
  "timeout": 360,
  "enabled": false
}
```

### Response Structure 
Details of the updated scheduled request
- `name`: Name of the request 

- `object_type`: Type of object for which the request is made 

- `object_name`: Name of model or pipeline for which the request is made 
 
- `schedule`: Schedule in crontab format 

- `version`: Name of version if type of object is 'model' 

- `request_data`: Input data for the scheduled request 

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false) 

- `timeout`: Timeout in seconds 

- `enabled`: Boolean value indicating whether the scheduled request is enabled or disabled 

- `creation_date`: The date when the scheduled request was created

#### Response Examples 
```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "model",
  "object_name": "test-model",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 360,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
schedule_name = 'schedule_name_example' # str | 
data = ubiops.ScheduleUpdate() # ScheduleUpdate | 

    try:
        # Update a scheduled request
        api_response = api_instance.scheduled_requests_update(project_name, schedule_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->scheduled_requests_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **schedule_name** | **str**|  | 
 **data** | [**ScheduleUpdate**](ScheduleUpdate.md)|  | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_status**
> Status service_status()

Service status


### Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure
- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

#### Response Examples
```	
{
  "status": "ok"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # Service status
        api_response = api_instance.service_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_create**
> ServiceUserDetail service_users_create(project_name, data)

Create a new service user


### Description 
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. 

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 
```
{
  "name": "service-user-1"
}
```

### Response Structure 
Details of the created service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `token`: The API token for the created service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
data = ubiops.ServiceUserCreate() # ServiceUserCreate | 

    try:
        # Create a new service user
        api_response = api_instance.service_users_create(project_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserDetail**](ServiceUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_delete**
> service_users_delete(project_name, service_user_id)

Delete service user


### Description 
Delete a service user from a project


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

    try:
        # Delete service user
        api_instance.service_users_delete(project_name, service_user_id)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_get**
> ServiceUserList service_users_get(project_name, service_user_id)

Retrieve details of a service user


### Description 
Retrieve details of a service user

### Response Structure 
Details of the service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

    try:
        # Retrieve details of a service user
        api_response = api_instance.service_users_get(project_name, service_user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_list**
> list[ServiceUserList] service_users_list(project_name)

List service users


### Description 
List service users defined in a project

### Response Structure 
List of details of the service users:
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user 

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 

    try:
        # List service users
        api_response = api_instance.service_users_list(project_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ServiceUserList]**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_token**
> ServiceUserTokenList service_users_token(project_name, service_user_id, data)

Reset the token of a service user


### Description 
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

### Response Structure 
Details of the new token for the service user
- `token`: The new API token for the service user

#### Response Examples
```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = None # object | 

    try:
        # Reset the token of a service user
        api_response = api_instance.service_users_token(project_name, service_user_id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**ServiceUserTokenList**](ServiceUserTokenList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_update**
> ServiceUserList service_users_update(project_name, service_user_id, data)

Update service user details

 
### Description
Update the name of a service user

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 

```
{
  "name": "new-service-user-name",
}
```

### Response Structure 
Details of the updated service user
- `id`: Unique identifier for the service user (UUID) 

- `email`: Email of the service user  

- `name`: Name of the service user 

- `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = ubiops.ServiceUserCreate() # ServiceUserCreate | 

    try:
        # Update service user details
        api_response = api_instance.service_users_update(project_name, service_user_id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->service_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_create**
> SubscriptionDetail subscriptions_create(data)

Create subscriptions


### Description 
Create a new subscription

### Required Parameters 
- `name`: Name of the subscription
- `max_projects`: Maximum number of allowed projects to be created with this subscription
- `max_users`: Maximum number of allowed users to be created with this subscription
- `logs_retention_days`: Number of days for which the logs for each projects will be saved
- `gb_seconds`: Maximum usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds they are running
- `resources`: Maximum number of allowed resources (connectors, pipelines and model versions) to be created with this subscription
- `hidden`: A boolean indication whether the subscription is public or private

### Optional Parameters
- `agreement`: Link to subscription agreement document 
- `terms_conditions`: Link to UbiOps SaaS Terms & Conditions document 

#### Request Examples 
```
{
  "name": "custom-subscription",
  "max_projects": 2,
  "max_users": 3,
  "logs_retention_days": 28,
  "gb_seconds": 20000,
  "resources": 20,
  "hidden": True
}
```

### Response Structure 
Details of the created subscription
- `id`: Unique identifier for the subscription (UUID) 
- `name`: Name of the subscription 
- `max_projects`: Maximum number of allowed projects to be created with this subscription 
- `max_users`: Maximum number of allowed users to be created with this subscription 
- `agreement`: Link to subscription agreement document 
- `terms_conditions`: Link to UbiOps SaaS Terms & Conditions document 
- `gb_seconds`: Maximum usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds they are running
- `resources`: Maximum number of allowed resources (connectors, pipelines and model versions) to be created with this subscription 

#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "custom-subscription",
  "max_projects": 2,
  "max_users": 3,
  "agreement": "",
  "terms_conditions": "",
  "gb_seconds": 10000,
  "resources": 15
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    data = ubiops.SubscriptionCreate() # SubscriptionCreate | 

    try:
        # Create subscriptions
        api_response = api_instance.subscriptions_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->subscriptions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubscriptionCreate**](SubscriptionCreate.md)|  | 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_delete**
> subscriptions_delete(subscription_name)

Delete a subscription


### Description 
Delete a subscription. It's not possible to delete a subscription if it is used by any organization.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    subscription_name = 'subscription_name_example' # str | 

    try:
        # Delete a subscription
        api_instance.subscriptions_delete(subscription_name)
    except ApiException as e:
        print("Exception when calling CoreApi->subscriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get**
> SubscriptionDetail subscriptions_get(subscription_name)

Get details of a subscription


### Description 
Get the details of a subscription

### Response Structure 
Details of the subscription
- `id`: Unique identifier for the subscription (UUID) 
- `name`: Name of the subscription 
- `max_projects`: Maximum number of allowed projects to be created with this subscription 
- `max_users`: Maximum number of allowed users to be created with this subscription 
- `agreement`: Link to subscription agreement document 
- `terms_conditions`: Link to UbiOps SaaS Terms & Conditions document 
- `gb_seconds`: Maximum usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds they are running
- `resources`: Maximum number of allowed resources (connectors, pipelines and model versions) to be created with this subscription 

#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "custom-subscription",
  "max_projects": 2,
  "max_users": 3,
  "agreement": "",
  "terms_conditions": "",
  "gb_seconds": 10000,
  "resources": 15
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    subscription_name = 'subscription_name_example' # str | 

    try:
        # Get details of a subscription
        api_response = api_instance.subscriptions_get(subscription_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_name** | **str**|  | 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_list**
> list[SubscriptionList] subscriptions_list()

List subscriptions


### Description 
List available subscriptions for organizations

### Response Structure
A list of details of the subscriptions
- `id`: Unique identifier for the subscription (UUID) 

- `name`: Name of the subscription 


#### Response Examples 
```
[
  {
    "id": "f35e94e2-820d-4ad2-a2c6-9e2668e1442b",
    "name": "free"
  },
  {
    "id": "888384be-b4b8-4728-918b-079c85879a5b",
    "name": "starter"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # List subscriptions
        api_response = api_instance.subscriptions_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->subscriptions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionList]**](SubscriptionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_update**
> SubscriptionDetail subscriptions_update(subscription_name, data)

Update details of a subscription


### Description 
Update a subscription

### Optional Parameters 
- `name`: New subscription name
- `max_projects`: Maximum number of allowed projects to be created with this subscription 
- `max_users`: Maximum number of allowed users to be created with this subscription 
- `agreement`: Link to subscription agreement document 
- `terms_conditions`: Link to UbiOps SaaS Terms & Conditions document 
- `gb_seconds`: Maximum usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds they are running
- `resources`: Maximum number of allowed resources (connectors, pipelines and model versions) to be created with this subscription 

#### Request Examples
```
{
  "max_projects": 4,
  "max_users": 5
}
```

```
{
  "name": "new-subscription-name"
}
```

### Response Structure 
Details of the subscription
- `id`: Unique identifier for the subscription (UUID) 
- `name`: Name of the subscription 
- `max_projects`: Maximum number of allowed projects to be created with this subscription 
- `max_users`: Maximum number of allowed users to be created with this subscription 
- `agreement`: Link to subscription agreement document 
- `terms_conditions`: Link to UbiOps SaaS Terms & Conditions document 
- `gb_seconds`: Maximum usage of GB seconds, calculated by multiplying the model memory sizes in GB by the number of seconds they are running
- `resources`: Maximum number of allowed resources (connectors, pipelines and model versions) to be created with this subscription 

#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "new-subscription-name",
  "max_projects": 4,
  "max_users": 5,
  "agreement": "",
  "terms_conditions": "",
  "gb_seconds": 10000,
  "resources": 20
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    subscription_name = 'subscription_name_example' # str | 
data = ubiops.SubscriptionUpdate() # SubscriptionUpdate | 

    try:
        # Update details of a subscription
        api_response = api_instance.subscriptions_update(subscription_name, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->subscriptions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_name** | **str**|  | 
 **data** | [**SubscriptionUpdate**](SubscriptionUpdate.md)|  | 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> UserPendingDetail user_create(data)

Create a new user


### Description 
Create a new user with the given details - email, password, name and surname. After creation, an email is send to the email address to activate the acount.
A user is required to accept the terms and conditions. The password needs to be at least 8 characters long.


### Required Parameters
- `email`: Email of the user. This is a unique field. 

- `password`: Password of the user 

- `terms_conditions`: Boolean field. Pass True to accept terms and conditions. 


### Optional Parameters
- `name`: Name of the user 

- `surname`: Surname of the user

#### Request Examples 
```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
  "terms_conditions": true
}
```

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "terms_conditions": true
}
```

### Response Structure 
Details of the created user
 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

#### Response Examples 
```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    data = ubiops.UserPendingCreate() # UserPendingCreate | 

    try:
        # Create a new user
        api_response = api_instance.user_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserPendingCreate**](UserPendingCreate.md)|  | 

### Return type

[**UserPendingDetail**](UserPendingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete()

Delete user


### Description 
Delete the user that makes the request


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # Delete user
        api_instance.user_delete()
    except ApiException as e:
        print("Exception when calling CoreApi->user_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> UserDetail user_get()

Get user details


### Description 
Get the details of the user that makes the request

### Response Structure 
Details of the user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `registration_date`: Date when the user was registered

#### Response Examples 
```
{
  "id": "4740a13a-70ae-4b7a-a461-8231eb2c0594",
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname",
  "registration_date": "2020-01-10 10:06:25.632+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    
    try:
        # Get user details
        api_response = api_instance.user_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> UserDetail user_update(data)

Update user details

 
### Description
Update the details of the user making the request - name, surname, email and password.

When updating the password, the parameter `previous_password` with the value of the previous password is also required.
The password needs to meet the following requirements:
- At least 8 characters long
- At least one capital and one lowercase letter
- At least one number
- At least one of the following symbols: !#$%&')(*+,./:;"<=>?[@]^_`{|}~-" 

### Optional Parameters
- `email`: Email of the user 

- `password`: Password of the user 

    - `previous_password`: Previous password of the user (This field is only required when updating the password) 

- `name`: Name of the user 

- `surname`: Surname of the user

#### Request Examples 
```
{
  "email": "new_test@example.com"
}
```

```
{
  "password": "new-secret-password",
  "previous_password": "previous-secret-password"
}
```

```
{
  "name": "New user name",
  "surname": "New user surname"
}
```

### Response Structure 
Details of the created user
- `id`: Unique identifier for the user (UUID) 

- `email`: Email of the user 

- `name`: Name of the user 

- `surname`: Surname of the user 

- `registration_date`: Date when the user was registered

#### Response Examples 
```
{
  "id": "4740a13a-70ae-4b7a-a461-8231eb2c0594",
  "email": "new_test@example.com",
  "type": "user",
  "name": "New user name",
  "surname": "New user surname",
  "registration_date": "2020-01-10 10:06:25.632+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import ubiops
from ubiops.rest import ApiException
from pprint import pprint
configuration = ubiops.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
with ubiops.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ubiops.CoreApi(api_client)
    data = ubiops.UserUpdate() # UserUpdate | 

    try:
        # Update user details
        api_response = api_instance.user_update(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

