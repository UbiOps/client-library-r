# Webhooks

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_tests_create**](webhooks.md#webhook_tests_create) | **POST** /projects/{project_name}/webhooks-tests | Create webhook tests
[**webhook_tests_get**](webhooks.md#webhook_tests_get) | **GET** /projects/{project_name}/webhooks-tests/{test_id} | Get webhook test
[**webhooks_create**](webhooks.md#webhooks_create) | **POST** /projects/{project_name}/webhooks | Create webhooks
[**webhooks_delete**](webhooks.md#webhooks_delete) | **DELETE** /projects/{project_name}/webhooks/{webhook_name} | Delete a webhook
[**webhooks_get**](webhooks.md#webhooks_get) | **GET** /projects/{project_name}/webhooks/{webhook_name} | Get webhook
[**webhooks_list**](webhooks.md#webhooks_list) | **GET** /projects/{project_name}/webhooks | List webhooks
[**webhooks_update**](webhooks.md#webhooks_update) | **PATCH** /projects/{project_name}/webhooks/{webhook_name} | Update a webhook


# **webhook_tests_create**
> webhook_tests_create(data)

Create webhook tests

## Description
Test a webhook

### Required Parameters

- `url`: Callback url to send event payloads to
- `object_type`: Type of object for which the webhook will be tested. It can be either 'deployment' or 'pipeline'.
- `object_name`: Name of deployment or pipeline for which the webhook will be tested
- `event`: Event that triggers the webhook

### Optional Parameters

- `headers`: Request headers to use when calling the webhook
- `version`: Name of deployment/pipeline version for which the webhook will be tested. If not provided, the default version of the deployment/pipeline will be used.
- `timeout`: Timeout in seconds on the call to webhook. It defaults to 10 seconds and the maximum value is 30 seconds.
- `retry`: Boolean value indicating whether the calls to the webhook should be retried if they fail (network timeout or non 2xx or 3xx HTTP response). It defaults to False.
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call. It defaults to False.

## Request Examples

```
{
  "url": "https://callback-url-webhook-1.com",
  "object_type": "deployment",
  "object_name": "deployment-1",
  "event": "deployment_request_finished"
}
```

### Response Structure
Details of the test

- `id`: Unique identifier for the test (UUID)
- `status`: Status of the test. It can be one of the following: 'pending', 'completed' or 'failed'.
- `error_message`: An error message explaining why the test has failed

## Response Examples

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "pending",
  "error_message": null
}
```

### Example
```R
data <- list(
  object_type = "object_type",
  object_name = "object_name",
  version = "version",  # (optional)
  url = "url",
  headers = list(  # (optional)
    list(
      key = "key",
      value = "value",
      protected = FALSE
    )
  ),
  event = "event",
  timeout = 0,  # (optional)
  retry = FALSE,  # (optional)
  include_result = FALSE  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhook_tests_create(
  data
)

# Or provide directly
result <- ubiops::webhook_tests_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhook_tests_get**
> webhook_tests_get(test.id)

Get webhook test

## Description
Retrieve details of a webhook test in a project

### Response Structure
Details of a test

- `id`: Unique identifier for the test (UUID)
- `status`: Status of the test. It can be one of the following: 'pending', 'completed' or 'failed'.
- `error_message`: An error message explaining why the test has failed

## Response Examples

Pending test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "pending",
  "error_message": null
}
```

Completed test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "completed",
  "error_message": null
}
```

Failed test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "failed",
  "error_message": "Connection error"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhook_tests_get(
  test.id
)

# Or provide directly
result <- ubiops::webhook_tests_get(
  test.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhooks_create**
> webhooks_create(data)

Create webhooks

## Description
Create a webhook

### Required Parameters

- `name`: Name of the webhook. It is unique within a project.
- `url`: Callback url to send event payloads to
- `object_type`: Type of object for which the webhook will be created. It can be either 'deployment' or 'pipeline'.
- `object_name`: Name of deployment or pipeline for which the webhook will be created
- `event`: Event that triggers the webhook

### Optional Parameters

- `headers`: Request headers to use when calling the webhook. It defaults to an empty list.
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `version`: Name of deployment/pipeline version for which the webhook will be created. If not provided, the default version of the deployment/pipeline will be used.
- `timeout`: Timeout in seconds on the call to webhook. It defaults to 10 seconds and the maximum value is 30 seconds.
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled. It defaults to True.
- `retry`: Boolean value indicating whether the calls to the webhook should be retried if they fail (network timeout or non 2xx or 3xx HTTP response). It defaults to False.
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call. It defaults to False.

## Request Examples

```
{
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [
    {
      "key": "Authorization",
      "value": "Token 123",
      "protected": true
    }
  ],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "event": "deployment_request_finished"
}
```

### Response Structure
Details of the created webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [
    {
      "key": "Authorization",
      "value": "Token 123",
      "protected": true
  ],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
}
```

### Example
```R
data <- list(
  name = "name",
  object_type = "object_type",
  object_name = "object_name",
  version = "version",  # (optional)
  url = "url",
  headers = list(  # (optional)
    list(
      key = "key",
      value = "value",
      protected = FALSE
    )
  ),
  event = "event",
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  timeout = 0,  # (optional)
  enabled = FALSE,  # (optional)
  retry = FALSE,  # (optional)
  include_result = FALSE  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhooks_create(
  data
)

# Or provide directly
result <- ubiops::webhooks_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhooks_delete**
> webhooks_delete(webhook.name)

Delete a webhook

## Description
Delete a webhook

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::webhooks_delete(
  webhook.name
)

# Or provide directly
ubiops::webhooks_delete(
  webhook.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhooks_get**
> webhooks_get(webhook.name)

Get webhook

## Description
Retrieve details of a webhook in a project

### Response Structure
Details of a webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhooks_get(
  webhook.name
)

# Or provide directly
result <- ubiops::webhooks_get(
  webhook.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhooks_list**
> webhooks_list(labels=NULL, object.type=NULL, event=NULL)

List webhooks

## Description
List the webhooks in a project

### Response Structure
A list of details of the webhooks in the project

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
[
  {
    "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
    "name": "webhook-1",
    "url": "https://callback-url-webhook-1.com",
    "headers": [],
    "object_type": "deployment",
    "object_name": "deployment-1",
    "version": "v1",
    "description": "",
    "labels": {
      "event-type": "request-finished"
    },
    "event": "deployment_request_finished",
    "timeout": 10,
    "enabled": true,
    "retry": false,
    "include_result": false
  },
  {
    "id": "cbfb3944-bbcb-4e18-907a-54d2f792a136",
    "name": "webhook-2",
    "url": "https://callback-url-webook-2.com",
    "headers": [],
    "object_type": "deployment",
    "object_name": "deployment-2",
    "version": null,
    "description": "",
    "labels": {
      "event-type": "request-failed"
    },
    "event": "deployment_request_failed",
    "timeout": 15,
    "enabled": true,
    "retry": false,
    "include_result": false
  },
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhooks_list(
  
  labels = NULL, object.type = NULL, event = NULL
)

# Or provide directly
result <- ubiops::webhooks_list(
  
  labels = NULL, object.type = NULL, event = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **webhooks_update**
> webhooks_update(webhook.name, data)

Update a webhook

## Description
Update a webhook

### Optional Parameters

- `name`: Name for the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook. Use *value* None to not update the values of protected headers.
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Request Examples

```
{
  "name": "new-webhook-name"
}
```

### Response Structure
Details of a webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "new-webhook-name",
  "url": "https://callback-url-webhook-1.com",
  "headers": [],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  url = "url",  # (optional)
  headers = list(  # (optional)
    list(
      key = "key",
      value = "value",
      protected = FALSE
    )
  ),
  event = "event",  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  timeout = 0,  # (optional)
  enabled = FALSE,  # (optional)
  retry = FALSE,  # (optional)
  include_result = FALSE  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhooks_update(
  webhook.name, data
)

# Or provide directly
result <- ubiops::webhooks_update(
  webhook.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


