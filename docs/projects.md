# Projects

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_types_list**](projects.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
[**project_audit_events_list**](projects.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](projects.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](projects.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](projects.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](projects.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](projects.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_requests_list**](projects.md#project_requests_list) | **GET** /projects/{project_name}/requests | List requests in project
[**project_users_create**](projects.md#project_users_create) | **POST** /projects/{project_name}/users | Add user to a project
[**project_users_delete**](projects.md#project_users_delete) | **DELETE** /projects/{project_name}/users/{user_id} | Delete user from a project
[**project_users_get**](projects.md#project_users_get) | **GET** /projects/{project_name}/users/{user_id} | Get user in a project
[**project_users_list**](projects.md#project_users_list) | **GET** /projects/{project_name}/users | List users in a project
[**projects_create**](projects.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](projects.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](projects.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](projects.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](projects.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](projects.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](projects.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**projects_usage_get**](projects.md#projects_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**quotas_list**](projects.md#quotas_list) | **GET** /projects/{project_name}/quotas | List quotas


# **instance_types_list**
> instance_types_list()

List instance types

## Description
Get list of available deployment instance types for a project

### Response Structure
Details of the instance type

- `id`: Unique identifier for the instance type (UUID)
- `name`: Name of the deployment instance type
- `display_name`: Readable name of the deployment instance type
- `memory_allocation`: Integer indicating memory allocation for this instance type (Mi)
- `cpu_allocation`: Float indicating vCPU allocation for this instance type
- `gpu_allocation`: Integer indicating number of GPU cores for this instance type
- `storage_allocation`: Integer indicating the maximum storage that can be used by this instance type (MB)
- `credit_rate`: Credits used per hour for this instance type
- `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type

## Response Examples

```
[
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "name": "512mb",
    "display_name": "512 MB",
    "memory_allocation": 512,
    "cpu_allocation": 0.125,
    "gpu_allocation": 0,
    "storage_allocation": 2048,
    "credit_rate": 0.5,
    "dedicated_node": false
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::instance_types_list(
  
)

# Or provide directly
result <- ubiops::instance_types_list(
  
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
  value = "value",
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
  value = "value",
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

# **project_requests_list**
> project_requests_list(object.type, status=NULL, success=NULL, limit=NULL, offset=NULL, sort=NULL, pipeline=NULL, request.schedule=NULL, start.date=NULL, end.date=NULL, search.id=NULL)

List requests in project

## Description
List the deployment/pipeline requests of the given project

### Required Parameters

- `object_type`: The type of the object. It can be either deployment or pipeline.

### Optional Parameters

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

### Response Structure
A list of dictionaries containing the metadata of the deployment/pipeline requests with the following fields:

- `id`: The UUID of the object
- `deployment`: Name of the deployment the request was made to (Optional: in case it's a deployment request. Else NULL)
- `pipeline`: Name of the pipeline the request was made to (Optional: in case it's a pipeline request. Else NULL)
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment/pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "pipeline": null,
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": null,
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_requests_list(
  object.type,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL
)

# Or provide directly
result <- ubiops::project_requests_list(
  object.type,
  status = NULL, success = NULL, limit = NULL, offset = NULL, sort = NULL, pipeline = NULL, request.schedule = NULL, start.date = NULL, end.date = NULL, search.id = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_users_create**
> project_users_create(data)

Add user to a project

## Description
Add a user to a project. The user making the request must be admin of the organization. The user can later be assigned roles in the project, such as project-admin, project-viewer etc.

### Required Parameters

- `user_id`: UUID of the user

## Request Examples

```
{
  "user_id": "bd3e25a3-f77a-4cb5-92df-a7e614106e95"
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)
- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
}
```

### Example
```R
data <- list(
  user_id = "user_id"
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_users_create(
  data
)

# Or provide directly
result <- ubiops::project_users_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_users_delete**
> project_users_delete(user.id)

Delete user from a project

## Description
Delete a user from a project. The user making the request must be admin of the organization.

**When a user is deleted from a project, all his roles defined in the scope of the project are also deleted.**

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::project_users_delete(
  user.id
)

# Or provide directly
ubiops::project_users_delete(
  user.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_users_get**
> project_users_get(user.id)

Get user in a project

## Description
Get the details of a user in a project. The user making the request must also be a project user.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)
- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_users_get(
  user.id
)

# Or provide directly
result <- ubiops::project_users_get(
  user.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **project_users_list**
> project_users_list(user.type=NULL)

List users in a project

## Description
List users and their details in a project. The user making the request must also be a project user.

### Response Structure
List of users

- `id`: Unique identifier for the user (UUID)
- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name"
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::project_users_list(
  
  user.type = NULL
)

# Or provide directly
result <- ubiops::project_users_list(
  
  user.type = NULL, 
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

### Optional Parameters

- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project. It defaults to False.
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running. It defaults to null, meaning that there are no limits.
- `cors_origins`: List of origins from which the requests are allowed for the project

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
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended
- `cors_origins`: List of origins from which the requests are allowed for the project

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": null,
  "suspended": false,
  "suspended_reason": null,
  "cors_origins": []
}
```

### Example
```R
data <- list(
  name = "name",
  organization_name = "organization_name",
  advanced_permissions = FALSE,  # (optional)
  credits = 0,  # (optional)
  cors_origins = list("value-1", "value-2")  # (optional)
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
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended
- `cors_origins`: List of origins from which the requests are allowed for the project

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null,
  "cors_origins": []
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
> projects_list(organization=NULL)

List projects

## Description
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created

### Optional Parameters
These parameters should be given as query parameters

- `organization`: Name of the organization whose projects should be obtained

## Response Examples

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "advanced_permissions": false,
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "advanced_permissions": false,
    "organization_name": "organization-2"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_list(
  organization = NULL
)

# Or provide directly
result <- ubiops::projects_list(
  organization = NULL, 
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
    - `deployment_version_revision_id`: the UUID of a deployment version revision. It does not have to be given in combination with the deployment and version name.
    - `environment_name`: name of an environment
    - `environment_build_id`: the UUID of an environment build. It does not have to be given in combination with the environment name.
    - `pipeline_name`: name of a pipeline
    - `pipeline_version`: name of a pipeline version. If this field is present in the request, pipeline_name must also be given. The pipeline versions are only meaningful in combination with the pipelines they are defined for.
    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name and pipeline_version must also be given. The pipeline objects are only meaningful in combination with the pipeline versions they are defined in.
    - `deployment_request_id`: the UUID of a deployment request
    - `pipeline_request_id`: the UUID of a pipeline request
    - `webhook_name`: name of a webhook
    - `system`: whether the log was generated by the system or user code (true / false)
    - `level`: the level of the log (info / error)

Any combination of filters may be given in the request. For example, if only a deployment_name is provided, all logs for that deployment are returned. These logs can contain information from all the pipelines that deployment is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.
Either `date` or `id` should be provided, as they both refer to a starting point of the logs. If no `date` or `id` is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date.
- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs.

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500.
- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value.

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned.

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned.

    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).

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
- `deployment_version_revision_id`: The UUID of the deployment version revision
- `environment_name`:  The environment which the log is related to
- `environment_build_id`: The UUID of the environment build
- `pipeline_name`: The pipeline which the log is related to
- `pipeline_version`: The pipeline version which the log is related to
- `pipeline_object_name`: The pipeline object which the log is related to
- `deployment_request_id`:  The deployment request the log is related to
- `pipeline_request_id`:  The pipeline request the log is related to
- `system`:  Whether the log was generated by the system (true / false)
- `level`: The level of the log (info / error)

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
- buckets
- environments

currently defined in the project.

## Response Examples

```
{
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4,
  "buckets": 2,
  "environments": 2
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
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspend`: A boolean to suspend and activate projects. If the project is already suspended by UbiOps, it is not possible to suspend/activate the project.
- `cors_origins`: List of origins from which the requests are allowed for the project

## Request Examples

```
{
  "name": "project-name-example"
}
```


```
{
  "name": "project-name-example",
  "cors_origins": ["https://test.com"]
}
```

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended
- `cors_origins`: List of origins from which the requests are allowed for the project

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null,
  "cors_origins": ["https://test.com"]
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  advanced_permissions = FALSE,  # (optional)
  credits = 0,  # (optional)
  suspend = FALSE,  # (optional)
  cors_origins = list("value-1", "value-2")  # (optional)
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

# **projects_usage_get**
> projects_usage_get(start.date=NULL, end.date=NULL, interval='month')

Get resource usage

## Description
Get credits usage for the project

### Optional Parameters

- `start_date`: Start date for the usage data to be returned. If omitted, results are generated for current subscription period.
- `end_date`: End date for the usage data to be returned. If omitted, results are generated for current subscription period.
- `interval`: Interval for the usage data. It can be 'day' or 'month'. It defaults to 'month'.

If no **start_date** or **end_date** is given, the current subscription period is used, e.g. if the usage details are requested on 01-12-2020 and the subscription started on 20-11-2020, the results will contain data from 20-11-2020 to 20-12-2020.
When **start_date** and **end_date** are given, this month period is used, e.g. if 12-11-2020 is given as start date and 12-12-2020 as end date, the results will contain data from 12-11-2020 to 12-12-2020.

### Response Structure

- `interval`: Interval for the usage data
- `data_project`: A list of dictionaries containing the project usage for the given date range
- `data_deployments`: A list of dictionaries containing the usage of each deployment in the project for the given date range
- `data_deployments_deleted`: A list of dictionaries containing the usage corresponds to deleted deployments in the project for the given date range

## Response Examples
2019-08-01 as start date and 2019-09-01 as end date

```
{
  "interval": "month",
  "data_project": [
    {
      "start_date": "2019-08-01T00:00:00Z",
      "end_date": "2019-09-01T00:00:00Z",
      "value": 500
    }
  ],
  "data_deployments": [
     {
      "deployment_id": "4326da55-06ca-4664-badb-03156355451a",
      "deployment_name": "deployment-1",
      "data": [
        {
          "start_date": "2019-08-01T00:00:00Z",
          "end_date": "2019-09-01T00:00:00Z",
          "value": 300
        }
      ]
    }
  ],
  "data_deleted_deployments": [
    {
      "start_date": "2019-08-01T00:00:00Z",
      "end_date": "2019-09-01T00:00:00Z",
      "value": 200
    }
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::projects_usage_get(
  
  start.date = NULL, end.date = NULL, interval = 'month'
)

# Or provide directly
result <- ubiops::projects_usage_get(
  
  start.date = NULL, end.date = NULL, interval = 'month', 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **quotas_list**
> quotas_list()

List quotas

## Description
List the quotas defined for a project. Project members can see quotas.

### Response Structure

- `resource`: The resource for the quota
- `quota`: Limit of how much the resource can be used in the project

## Response Examples

```
[
  {
    "resource": "memory_standard",
    "quota": 274877906944
  },
  {
    "resource": "cpu_standard",
    "quota": 62
  },
  {
    "resource": "gpu_standard",
    "quota": 0
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::quotas_list(
  
)

# Or provide directly
result <- ubiops::quotas_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


