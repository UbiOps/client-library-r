# Projects

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_get**](projects.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**project_audit_events_list**](projects.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](projects.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](projects.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](projects.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](projects.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](projects.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_usage_get**](projects.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**projects_create**](projects.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](projects.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](projects.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](projects.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](projects.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](projects.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](projects.md#projects_update) | **PATCH** /projects/{project_name} | Update a project


# **metrics_get**
> metrics_get(metric, start.time, end.time, object.type, interval=NULL, object.id=NULL)

Get metrics

## Description
Get metrics for the project or a specified object. The following metrics are available:

Metrics on pipeline version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `request_duration`: Time in seconds for a pipeline request to complete
- `input_volume`: Volume of incoming data in bytes
- `object_requests`: Number of requests made to objects in the pipeline version
- `object_failed_requests`: Number of failed requests made to deployments in a pipeline

Metrics on deployment version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `input_volume`: Volume of incoming data in bytes
- `output_volume`: Volume of outgoing data in bytes
- `outputs`: Number of outgoing data items
- `compute`: Time in seconds for a request to complete
- `memory_average`: Average memory used during a request
- `memory_peak`: Peak memory used during a request
- `instances`: Number of active deployment instances
- `gb_seconds`: Usage of GB seconds, calculated by multiplying the deployment memory sizes in GB by the number of seconds the deployments are running
- `active_time`: Time in seconds that the deployment is active

### Required Parameters

- `start_time`: Starting time for the metric values to be returned. It should be provided in datetime isoformat.
- `end_time`: Ending time for the metric values to be returned. It should be provided in datetime isoformat.
- `object_type`: The type of the object for which the metrics are requested. It can be either `deployment_version` or `pipeline_version`.

### Optional Parameters

- `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
- `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.

### Response Structure

- `start_time`: Timestamp denoting the start of the period over which the metric was measured
- `end_time`: Timestamp denoting the end of the period over which the metric was measured
- `value`: Aggregated metric value for the given interval

## Response Examples
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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::metrics_get(
  metric, start.time, end.time, object.type,
  interval = NULL, object.id = NULL
)

# Or provide directly
result <- ubiops::metrics_get(
  metric, start.time, end.time, object.type,
  interval = NULL, object.id = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_audit_events_list**
> project_audit_events_list(action=NULL, limit=NULL, offset=NULL)

List audit events in a project

## Description
List all audit events in a project including all objects

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events in the project

- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

## Response Examples

```
[
  {
    "id": "54c1ea23-5773-4821-8fd7-1b577cc301bc",
    "date": "2020-05-23T11:53:02.873+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created project test-project",
    "object_type": "project",
    "object_name": "test-project"
  },
  {
    "id": "764e254c-7402-4445-ac79-009d08b21caa",
    "date": "2020-05-23T11:57:20.072+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_audit_events_list(
  
  action = NULL, limit = NULL, offset = NULL
)

# Or provide directly
result <- ubiops::project_audit_events_list(
  
  action = NULL, limit = NULL, offset = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_environment_variables_create**
> project_environment_variables_create(data)

Create project environment variable

## Description
Create an environment variable for the project. This variable will be inherited by all deployments in this project.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

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

## Response Examples

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
```R
data <- list(
  name = "name",
  value = "value",  # (optional)
  secret = FALSE
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_environment_variables_create(
  data
)

# Or provide directly
result <- ubiops::project_environment_variables_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_environment_variables_delete**
> project_environment_variables_delete(id)

Delete project environment variable

## Description
Delete an environment variable of the project

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::project_environment_variables_delete(
  id
)

# Or provide directly
ubiops::project_environment_variables_delete(
  id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_environment_variables_get**
> project_environment_variables_get(id)

Get project environment variable

## Description
Retrieve details of a project environment variable.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_environment_variables_get(
  id
)

# Or provide directly
result <- ubiops::project_environment_variables_get(
  id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_environment_variables_list**
> project_environment_variables_list()

List project environment variables

## Description
List the environment variables defined for the project. These are the variables that are inherited by all deployments in this project.


### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_environment_variables_list(
  
)

# Or provide directly
result <- ubiops::project_environment_variables_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_environment_variables_update**
> project_environment_variables_update(id, data)

Update project environment variable

## Description
Update an environment variable for the projects

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string.
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

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

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "new_schema",
  "secret": false
}
```

### Example
```R
data <- list(
  name = "name",
  value = "value",  # (optional)
  secret = FALSE
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_environment_variables_update(
  id, data
)

# Or provide directly
result <- ubiops::project_environment_variables_update(
  id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_usage_get**
> project_usage_get(start.month=NULL)

Get resource usage

## Description
Get resource usage for the project. This returns a list of metrics that are used for billing, aggregated per month.

### Optional Parameters

- `start_month`: date indicating the start month to fetch usage data from, formatted `YYYY-MM`. If omitted results are generated from one year ago.

### Response Structure

- `metric`: The metric that was measured
- `object_type`: Type of object the metric was measured for (version or pipeline)
- `usage`: an array of objects each containing the following:
     - `month`: Timestamp denoting the start of the month
     - `value`: Aggregated metric value for the given unit over the given month

## Response Examples

```
[
  {
    "object_type": "pipeline_version",
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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_usage_get(
  
  start.month = NULL
)

# Or provide directly
result <- ubiops::project_usage_get(
  
  start.month = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_create**
> projects_create(data)

Create projects

## Description
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters

- `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `organization_name`: Name of the organization in which the project is going to be created


## Request Examples

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

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```

### Example
```R
data <- list(
  name = "name",
  organization_name = "organization_name"
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_create(
  data
)

# Or provide directly
result <- ubiops::projects_create(
  data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_delete**
> projects_delete()

Delete a project

## Description
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the deployments and pipelines defined in it are also deleted.**

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::projects_delete(
  
)

# Or provide directly
ubiops::projects_delete(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_get**
> projects_get()

Get details of a project

## Description
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)

- `name`: Name of the project

- `creation_date`: Time the project was created

- `organization_name`: Name of the organization in which the project is created

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_get(
  
)

# Or provide directly
result <- ubiops::projects_get(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_list**
> projects_list()

List projects

## Description
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects

- `id`: Unique identifier for the project (UUID)

- `name`: Name of the project

- `creation_date`: Time the project was created

- `organization_name`: Name of the organization in which the project is created

## Response Examples

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
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_list()

# Or provide directly
result <- ubiops::projects_list(
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_log_list**
> projects_log_list(data=NULL)

List logs for a project

## Description
Retrieve the logs of all objects in a project, including deployments, pipelines and requests. Using filters you can filter the logs on the objects and information of your choice.

### Optional Parameters

- `filters`: A dictionary containing information to filter logs on. It may contain zero or more of the following fields:

    - `deployment_name`: name of a deployment

    - `deployment_version`: name of a deployment version. If this field is present in the request, deployment_name must also be given. The deployment versions are only meaningful in combination with the deployments they are defined for.

    - `build_id`: the UUID of a build. It does not have to be given in combination with the version and deployment name.

    - `pipeline_name`: name of a pipeline

    - `pipeline_version`: name of a pipeline version. If this field is present in the request, pipeline_name must also be given. The pipeline versions are only meaningful in combination with the pipelines they are defined for.

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name and pipeline_version must also be given. The pipeline objects are only meaningful in combination with the pipeline versions they are defined in.

    - `deployment_request_id`: the UUID of a deployment request

    - `pipeline_request_id`: the UUID of a pipeline request

    - `system`: whether the log was generated by the system or user code (true / false)


Any combination of filters may be given in the request. For example, if only a deployment_name is provided, all logs for that deployment are returned. These logs can contain information from all the pipelines that deployment is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.

- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date.

- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500.

- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value.

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned.

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned.

    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).
   
If no date or id is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

## Request Examples

```
{
  "filters": {
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z"
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1"
  },
  "id": "41d7a7c5cd025e3501a00000",
  "date_range": -100
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
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
- `deployment_name`:  The deployment which the log is related to

- `deployment_version`:  The deployment version which the log is related to

- `build_id`: The UUID of the build

- `pipeline_name`: The pipeline which the log is related to

- `pipeline_version`: The pipeline version which the log is related to

- `pipeline_object_name`: The pipeline object which the log is related to

- `deployment_request_id`:  The deployment request the log is related to

- `pipeline_request_id`:  The pipeline request the log is related to

- `system`:  Whether the log was generated by the system (true / false)

## Response Examples
Logs for a specific deployment and version

```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "deployment_request_id": "ee63f938-ba81-438e-8482-9ac76037895f",
    "pipeline_name": "pipeline-2",
    "pipeline_version": "v2",
    "pipeline_object_name": "deployment-1-v1-object",
    "pipeline_request_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "[Error] Deployment call result (failed)"
  }
]
```

Logs for a specific pipeline

```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "deployment_name": "deployment-2",
    "deployment_version": "v2",
    "deployment_request_id": "6ee941d3-9905-49f5-95b4-cd9c4c23bb03",
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "pipeline_object_name": "deployment-2-v2-object",
    "pipeline_request_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Deployment call result (success): 0.2316"
  }
]
```

### Example
```R
data <- list(
  filters = list(key = "value"),  # (optional)
  date_range = 0,  # (optional)
  date = "date",  # (optional)
  id = "id",  # (optional)
  limit = 0  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_log_list(
  
  data = NULL
)

# Or provide directly
result <- ubiops::projects_log_list(
  
  data = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_resource_usage**
> projects_resource_usage()

List resource usage of a project

## Description
List the total number of resources used in a project

### Response Structure
A list containing the number of

- deployments

- deployment_versions

- pipelines

- pipeline_versions

currently defined in the project.

## Response Examples

```
{
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_resource_usage(
  
)

# Or provide directly
result <- ubiops::projects_resource_usage(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **projects_update**
> projects_update(data)

Update a project

## Description
Update the name of a single project. The user making the request must have appropriate permissions.

### Optional Parameters

- `name`: New project name

## Request Examples

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

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```

### Example
```R
data <- list(
  name = "name"
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_update(
  data
)

# Or provide directly
result <- ubiops::projects_update(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

