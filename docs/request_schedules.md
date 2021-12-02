# RequestSchedules

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_schedules_create**](request_schedules.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](request_schedules.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](request_schedules.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](request_schedules.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](request_schedules.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule


# **request_schedules_create**
> request_schedules_create(data)

Create request schedules

## Description
Create a new request schedule with the provided name

### Required Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `object_type`: Type of object for which the request is made. Can be either 'deployment' or 'pipeline'.

- `object_name`: Name of deployment or pipeline for which the request is made

- `schedule`: Schedule in crontab format

### Optional Parameters

- `version`: Name of version for which the request schedule is made. If not provided, default version of the deployment/pipeline will be used.

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.

- `timeout`: Timeout of the request in seconds. The maximum and default values depend on the object (deployment or pipeline) and the type of request (batch or direct).
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 300,
  "enabled": true,
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Response Structure
Details of the created request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request schedule is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false). For pipeline schedules, this variable is true by default. For deployment schedules, the deployment mode is used to determine its value. It is false for express mode and true for batch mode.

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 300,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Example
```R
data <- list(
  name = "name",
  object_type = "object_type",
  object_name = "object_name",
  version = "version",  # (optional)
  schedule = "schedule",
  request_data = list(key = "value"),  # (optional)
  timeout = 0,  # (optional)
  enabled = FALSE,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::request_schedules_create(
  data
)

# Or provide directly
result <- ubiops::request_schedules_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **request_schedules_delete**
> request_schedules_delete(schedule.name)

Delete a request schedule

## Description
Delete the request schedule from the project.

If you want to temporarily disable a request schedule, update the request with `enabled` set to False.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::request_schedules_delete(
  schedule.name
)

# Or provide directly
ubiops::request_schedules_delete(
  schedule.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **request_schedules_get**
> request_schedules_get(schedule.name)

Get details of a request schedule

## Description
Retrieve details of a single request schedule

### Response Structure
Details of a request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false)

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 200,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::request_schedules_get(
  schedule.name
)

# Or provide directly
result <- ubiops::request_schedules_get(
  schedule.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **request_schedules_list**
> request_schedules_list()

List request schedules

## Description
List the request schedules in a project. The user has to have 'requests.list' permission on either 'deployments.versions' or 'pipelines.versions' to list the request schedules.

### Response Structure
A list of details of all request schedules in a project

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made 

- `request_data`: Input data for the request schedule

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false)

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
[
  {
    "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
    "name": "test-request",
    "object_type": "deployment",
    "object_name": "test-deployment",
    "version": "v1",
    "schedule": "0 * 3 * *",
    "request_data": {
      "input_field_1": 2345,
      "input_field_2": 8765
    },
    "batch": false,
    "timeout": 200",
    "enabled": true,
    "creation_date": "2020-09-16T08:06:34.457679Z",
    "description": "Daily request schedule",
    "labels": {
      "type": "daily"
    }
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::request_schedules_list(
  
)

# Or provide directly
result <- ubiops::request_schedules_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **request_schedules_update**
> request_schedules_update(schedule.name, data)

Update a request schedule

## Description
Update a request schedule in a project. Create permissions on the object are necessary for this action.

### Optional Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `schedule`: Schedule in crontab format

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.

- `timeout`: Timeout of the request in seconds. The maximum and default values depend on the object (deployment or pipeline) and the type of request (batch or direct).

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 360,
  "enabled": false
}
```

### Response Structure
Details of the updated request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `batch`: Boolean value indicating whether the requests will be performed as batch requests (true) or as direct requests (false)

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "batch": false,
  "timeout": 360,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  schedule = "schedule",  # (optional)
  request_data = list(key = "value"),  # (optional)
  timeout = 0,  # (optional)
  enabled = FALSE,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::request_schedules_update(
  schedule.name, data
)

# Or provide directly
result <- ubiops::request_schedules_update(
  schedule.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


