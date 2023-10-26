# DeploymentRequests

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_deployment_requests_create**](deployment_requests.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
[**batch_deployment_version_requests_create**](deployment_requests.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
[**deployment_requests_batch_delete**](deployment_requests.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
[**deployment_requests_batch_get**](deployment_requests.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
[**deployment_requests_create**](deployment_requests.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
[**deployment_requests_delete**](deployment_requests.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
[**deployment_requests_get**](deployment_requests.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
[**deployment_requests_list**](deployment_requests.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
[**deployment_requests_update**](deployment_requests.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
[**deployment_version_requests_batch_delete**](deployment_requests.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
[**deployment_version_requests_batch_get**](deployment_requests.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
[**deployment_version_requests_create**](deployment_requests.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
[**deployment_version_requests_delete**](deployment_requests.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
[**deployment_version_requests_get**](deployment_requests.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
[**deployment_version_requests_list**](deployment_requests.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
[**deployment_version_requests_update**](deployment_requests.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request


# **batch_deployment_requests_create**
> batch_deployment_requests_create(deployment.name, data, timeout=NULL, notification.group=NULL)

Create a batch deployment request

## Description
Request multiple predictions from the default version of a deployment. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods.

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example
```R
data <- list( list(input_field_1 = "input_value_1", input_field_2 = "input_value_2") )

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::batch_deployment_requests_create(
  deployment.name, data,
  timeout = NULL, notification.group = NULL
)

# Or provide directly
result <- ubiops::batch_deployment_requests_create(
  deployment.name, data,
  timeout = NULL, notification.group = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **batch_deployment_version_requests_create**
> batch_deployment_version_requests_create(deployment.name, version, data, timeout=NULL, notification.group=NULL)

Create a batch deployment version request

## Description
Request multiple predictions from a deployment version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example
```R
data <- list( list(input_field_1 = "input_value_1", input_field_2 = "input_value_2") )

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::batch_deployment_version_requests_create(
  deployment.name, version, data,
  timeout = NULL, notification.group = NULL
)

# Or provide directly
result <- ubiops::batch_deployment_version_requests_create(
  deployment.name, version, data,
  timeout = NULL, notification.group = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_batch_delete**
> deployment_requests_batch_delete(deployment.name, data)

Delete multiple deployment requests

## Description
Delete multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example
```R
data <- list("request_id_1", "request_id_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_batch_delete(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployment_requests_batch_delete(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_batch_get**
> deployment_requests_batch_get(deployment.name, data)

Retrieve multiple deployment requests

## Description
Retrieve multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null
  }
]
```

### Example
```R
data <- list("request_id_1", "request_id_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_batch_get(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployment_requests_batch_get(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_create**
> deployment_requests_create(deployment.name, data, timeout=NULL)

Create a direct deployment request

## Description
Request a prediction from a deployment. Deployment requests are made for the default version of a deployment.
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `success`: A boolean value that indicates whether the deployment request was successful
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": null
}
```

### Example
```R
data <- list(input_field_1 = "input_value_1", input_field_2 = "input_value_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_create(
  deployment.name, data,
  timeout = NULL
)

# Or provide directly
result <- ubiops::deployment_requests_create(
  deployment.name, data,
  timeout = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_delete**
> deployment_requests_delete(deployment.name, request.id)

Delete a deployment request

## Description
Delete a deployment request for the default version of a deployment

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployment_requests_delete(
  deployment.name, request.id
)

# Or provide directly
ubiops::deployment_requests_delete(
  deployment.name, request.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_get**
> deployment_requests_get(deployment.name, request.id, metadata.only=NULL)

Get a deployment request

## Description
Get a request of the default version of a deployment. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `origin`: A dictionary containing the information on where the request originated from. It contains:
   - the deployment (and version) names if the request is directly made to the deployment
   - the pipeline (and version) names if the request is part of a pipeline request
   - the request schedule name if the request is created via a request schedule

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "origin": {
    "deployment": "deployment-1",
    "deployment_version": "v1"
  }
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_get(
  deployment.name, request.id,
  metadata.only = NULL
)

# Or provide directly
result <- ubiops::deployment_requests_get(
  deployment.name, request.id,
  metadata.only = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_list**
> deployment_requests_list(deployment.name, status=NULL, success=NULL, limit=NULL, offset=NULL, sort=NULL, pipeline=NULL, request.schedule=NULL, start.date=NULL, end.date=NULL, search.id=NULL)

List deployment requests

## Description
List all requests for the default version of a deployment

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `request_schedule`: The name of a request schedule that created requests
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

With start_date="2020-03-28T20:00:26+00:00" and end_date="2020-03-28T22:00:26+00:00":

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": false,
    "time_created": "2020-03-28T20:00:43.613+00:00",
    "time_started": "2020-03-28T20:00:50.276+00:00",
    "time_completed": "2020-03-28T20:00:55.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T21:12:45.613+00:00",
    "time_started": "2020-03-28T21:13:00.276+00:00",
    "time_completed": "2020-03-28T21:13:05.241+00:00"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_list(
  deployment.name,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL
)

# Or provide directly
result <- ubiops::deployment_requests_list(
  deployment.name,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_requests_update**
> deployment_requests_update(deployment.name, request.id, data)

Update a deployment request

## Description
Update a deployment request for the default version of a deployment. It is possible to **cancel** a request by giving `cancelled` in the status field.

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples


```
{
"status": "cancelled"
}
```

### Example
```R
data <- list(
  status = "status",  # (optional)
  notification_group = "notification_group"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_update(
  deployment.name, request.id, data
)

# Or provide directly
result <- ubiops::deployment_requests_update(
  deployment.name, request.id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_batch_delete**
> deployment_version_requests_batch_delete(deployment.name, version, data)

Delete multiple deployment version requests

## Description
Delete multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example
```R
data <- list("request_id_1", "request_id_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_batch_delete(
  deployment.name, version, data
)

# Or provide directly
result <- ubiops::deployment_version_requests_batch_delete(
  deployment.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_batch_get**
> deployment_version_requests_batch_get(deployment.name, version, data)

Retrieve multiple deployment version requests

## Description
Retrieve multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `retries`: Number of times that the request has been retried

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null,
    "retries": 0
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null,
    "retries": 1
  }
]
```

### Example
```R
data <- list("request_id_1", "request_id_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_batch_get(
  deployment.name, version, data
)

# Or provide directly
result <- ubiops::deployment_version_requests_batch_get(
  deployment.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_create**
> deployment_version_requests_create(deployment.name, version, data, timeout=NULL)

Create a direct deployment version request

## Description
Request a prediction from a deployment version. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment version
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `success`: A boolean value that indicates whether the deployment request was successful
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": None
}
```

### Example
```R
data <- list(input_field_1 = "input_value_1", input_field_2 = "input_value_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_create(
  deployment.name, version, data,
  timeout = NULL
)

# Or provide directly
result <- ubiops::deployment_version_requests_create(
  deployment.name, version, data,
  timeout = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_delete**
> deployment_version_requests_delete(deployment.name, request.id, version)

Delete a deployment version request

## Description
Delete a deployment request for a deployment version

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployment_version_requests_delete(
  deployment.name, request.id, version
)

# Or provide directly
ubiops::deployment_version_requests_delete(
  deployment.name, request.id, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_get**
> deployment_version_requests_get(deployment.name, request.id, version, metadata.only=NULL)

Get a deployment version request

## Description
Get a request for a deployment version. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `retries`: Number of times that the request has been retried

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "retries": 0
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_get(
  deployment.name, request.id, version,
  metadata.only = NULL
)

# Or provide directly
result <- ubiops::deployment_version_requests_get(
  deployment.name, request.id, version,
  metadata.only = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_list**
> deployment_version_requests_list(deployment.name, version, status=NULL, success=NULL, limit=NULL, offset=NULL, sort=NULL, pipeline=NULL, request.schedule=NULL, start.date=NULL, end.date=NULL, search.id=NULL)

List deployment version requests

## Description
List all requests for a deployment version

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `request_schedule`: The name of a request schedule that created requests
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

With start_date="2020-03-28T20:00:26+00:00" and end_date="2020-03-28T22:00:26+00:00":

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": false,
    "time_created": "2020-03-28T20:00:43.613+00:00",
    "time_started": "2020-03-28T20:00:50.276+00:00",
    "time_completed": "2020-03-28T20:00:55.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T21:12:45.613+00:00",
    "time_started": "2020-03-28T21:13:00.276+00:00",
    "time_completed": "2020-03-28T21:13:05.241+00:00"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_list(
  deployment.name, version,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL
)

# Or provide directly
result <- ubiops::deployment_version_requests_list(
  deployment.name, version,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_requests_update**
> deployment_version_requests_update(deployment.name, request.id, version, data)

Update a deployment version request

## Description
Update a deployment request for a deployment version. It is possible to **cancel** a request by giving `cancelled` in the status field.

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples


```
{
"status": "cancelled"
}
```

### Example
```R
data <- list(
  status = "status",  # (optional)
  notification_group = "notification_group"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_requests_update(
  deployment.name, request.id, version, data
)

# Or provide directly
result <- ubiops::deployment_version_requests_update(
  deployment.name, request.id, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


