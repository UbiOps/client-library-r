# Deployments

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**builds_get**](deployments.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
[**builds_list**](deployments.md#builds_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds | List builds
[**deployment_audit_events_list**](deployments.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
[**deployment_environment_variables_copy**](deployments.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
[**deployment_environment_variables_create**](deployments.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
[**deployment_environment_variables_delete**](deployments.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
[**deployment_environment_variables_get**](deployments.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
[**deployment_environment_variables_list**](deployments.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
[**deployment_environment_variables_update**](deployments.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
[**deployment_version_environment_variables_copy**](deployments.md#deployment_version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy deployment version environment variable
[**deployment_version_environment_variables_create**](deployments.md#deployment_version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create deployment version environment variable
[**deployment_version_environment_variables_delete**](deployments.md#deployment_version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete deployment version environment variable
[**deployment_version_environment_variables_get**](deployments.md#deployment_version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get deployment version environment variable
[**deployment_version_environment_variables_list**](deployments.md#deployment_version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List deployment version environment variables
[**deployment_version_environment_variables_update**](deployments.md#deployment_version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update deployment version environment variable
[**deployment_versions_create**](deployments.md#deployment_versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create deployment versions
[**deployment_versions_delete**](deployments.md#deployment_versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete deployment version
[**deployment_versions_get**](deployments.md#deployment_versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get deployment version
[**deployment_versions_list**](deployments.md#deployment_versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List deployment versions
[**deployment_versions_update**](deployments.md#deployment_versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update deployment version
[**deployments_create**](deployments.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create deployments
[**deployments_delete**](deployments.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
[**deployments_get**](deployments.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of a deployment
[**deployments_list**](deployments.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments
[**deployments_update**](deployments.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
[**revisions_file_download**](deployments.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
[**revisions_file_upload**](deployments.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
[**revisions_get**](deployments.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
[**revisions_list**](deployments.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions


# **builds_get**
> builds_get(build.id, deployment.name, version)

Get build

## Description
Retrieve details of a single build of a version

### Response Structure
A dictionary containing details of the build

- `id`: Unique identifier for the build (UUID)
- `revision`: UUID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. Can be 'queued', 'building', 'deploying', 'validating', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
{
  "id": "49d857fd-39ca-48db-9547-0d5d1a91b62d",
  "revision": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
  "creation_date": "2020-12-23T16:15:11.200+00:00",
  "status": "building",
  "error_message": "",
  "trigger": "Deployment file upload"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::builds_get(
  build.id, deployment.name, version
)

# Or provide directly
result <- ubiops::builds_get(
  build.id, deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **builds_list**
> builds_list(deployment.name, version)

List builds

## Description
List all builds associated with a version. A build is triggered when a new deployment file is uploaded.

### Response Structure
A list of details of the builds

- `id`: Unique identifier for the build (UUID)
- `revision`: UUID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. Can be 'queued', 'building', 'deploying', 'validating', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
[
  {
    "id": "49d857fd-39ca-48db-9547-0d5d1a91b62d",
    "revision": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
    "creation_date": "2020-12-23T16:15:11.200+00:00",
    "status": "failed",
    "error_message": "Could not find the deployment file",
    "trigger": "Deployment file upload"
  },
  {
    "id": "baf88570-d884-4bc6-9308-01068b051f5f",
    "revision": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
    "creation_date": "2020-12-23T16:35:13.088+00:00",
    "status": "queued",
    "error_message": "",
    "trigger": "Deployment file upload"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::builds_list(
  deployment.name, version
)

# Or provide directly
result <- ubiops::builds_list(
  deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_audit_events_list**
> deployment_audit_events_list(deployment.name, action=NULL, limit=NULL, offset=NULL)

List audit events for a deployment

## Description
List all audit events for a deployment including versions

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events for a deployment

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
    "id": "25750859-e082-44df-bde9-cd85ca3f869c",
    "date": "2020-10-23T12:03:55.675+00:00",
    "action": "delete",
    "user": "user@example.com",
    "event": "Deleted environment variable ENV_VAR for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  },
  {
    "id": "ce81814d-b00c-4094-a483-814afdb80875",
    "date": "2020-10-23T12:04:28.645+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created version v1 for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "audit-deployment"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_audit_events_list(
  deployment.name,
  action = NULL, limit = NULL, offset = NULL
)

# Or provide directly
result <- ubiops::deployment_audit_events_list(
  deployment.name,
  action = NULL, limit = NULL, offset = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_copy**
> deployment_environment_variables_copy(deployment.name, data)

Copy deployment environment variable

## Description
Copy existing environment variables from a source object to the deployment. Variables of the deployment with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters

- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters

- `source_version`: The version of the deployment from which the variables will be copied

## Request Examples
Copy the environment variables from a deployment

```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a version

```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure
A list of the copied variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "deployment_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```

### Example
```R
data <- list(
  source_deployment = "source_deployment",
  source_version = "source_version"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_environment_variables_copy(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployment_environment_variables_copy(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_create**
> deployment_environment_variables_create(deployment.name, data)

Create deployment environment variable

## Description
Create an environment variable for the deployment. This variable will be inherited by all versions of this deployment. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "deployment_variable_a",
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

## Response Examples

```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "deployment_variable_a",
"value": "some_value",
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
result <- ubiops::deployment_environment_variables_create(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployment_environment_variables_create(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_delete**
> deployment_environment_variables_delete(deployment.name, id)

Delete deployment environment variable

## Description
Delete an environment variable of the deployment

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployment_environment_variables_delete(
  deployment.name, id
)

# Or provide directly
ubiops::deployment_environment_variables_delete(
  deployment.name, id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_get**
> deployment_environment_variables_get(deployment.name, id)

Get deployment environment variable

## Description
Retrieve details of a deployment environment variable. This cannot be used to retrieve details of inherited variables.

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
result <- ubiops::deployment_environment_variables_get(
  deployment.name, id
)

# Or provide directly
result <- ubiops::deployment_environment_variables_get(
  deployment.name, id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_list**
> deployment_environment_variables_list(deployment.name)

List deployment environment variables

## Description
List the environment variables defined for the deployment. Includes environment variables defined at project level.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project` or null if the variable was defined for the deployment directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the deployment directly

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_environment_variables_list(
  deployment.name
)

# Or provide directly
result <- ubiops::deployment_environment_variables_list(
  deployment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_environment_variables_update**
> deployment_environment_variables_update(deployment.name, id, data)

Update deployment environment variable

## Description
Update an environment variable for the deployment. This cannot be used to update inherited variables; to change an inherited variable for a specific deployment you can create a variable with the same name for the deployment.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "deployment_variable_a",
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

## Response Examples

```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "deployment_variable_a",
  "value": "some new value",
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
result <- ubiops::deployment_environment_variables_update(
  deployment.name, id, data
)

# Or provide directly
result <- ubiops::deployment_environment_variables_update(
  deployment.name, id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_copy**
> deployment_version_environment_variables_copy(deployment.name, version, data)

Copy deployment version environment variable

## Description
Copy existing environment variables from a source object to the deployment version. Variables of the deployment version with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters

- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters

- `source_version`: The version of the deployment from which the variables will be copied

## Request Examples
Copy the environment variables from a deployment

```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a deployment version

```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure
A list of the copied variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```

### Example
```R
data <- list(
  source_deployment = "source_deployment",
  source_version = "source_version"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_environment_variables_copy(
  deployment.name, version, data
)

# Or provide directly
result <- ubiops::deployment_version_environment_variables_copy(
  deployment.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_create**
> deployment_version_environment_variables_create(deployment.name, version, data)

Create deployment version environment variable

## Description
Create an environment variable for the deployment version. Variables inherited from the project or deployment can be shadowed by creating a variable with the same name.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "deployment_version_variable",
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

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "deployment_version_variable",
  "value": "another one",
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
result <- ubiops::deployment_version_environment_variables_create(
  deployment.name, version, data
)

# Or provide directly
result <- ubiops::deployment_version_environment_variables_create(
  deployment.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_delete**
> deployment_version_environment_variables_delete(deployment.name, id, version)

Delete deployment version environment variable

## Description
Delete an environment variable of a deployment version

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployment_version_environment_variables_delete(
  deployment.name, id, version
)

# Or provide directly
ubiops::deployment_version_environment_variables_delete(
  deployment.name, id, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_get**
> deployment_version_environment_variables_get(deployment.name, id, version)

Get deployment version environment variable

## Description
Retrieve details of a deployment version environment variable. This cannot be used to retrieve details of inherited variables.

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
result <- ubiops::deployment_version_environment_variables_get(
  deployment.name, id, version
)

# Or provide directly
result <- ubiops::deployment_version_environment_variables_get(
  deployment.name, id, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_list**
> deployment_version_environment_variables_list(deployment.name, version)

List deployment version environment variables

## Description
List the environment variables defined for the deployment version. Includes environment variables defined at project level and deployment level.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or null if the variable was defined for the version directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the version directly

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "deployment_version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
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
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_version_environment_variables_list(
  deployment.name, version
)

# Or provide directly
result <- ubiops::deployment_version_environment_variables_list(
  deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_version_environment_variables_update**
> deployment_version_environment_variables_update(deployment.name, id, version, data)

Update deployment version environment variable

## Description
Update an environment variable for the deployment version. This cannot be used to update inherited variables; to change an inherited variable for a specific version you can create a variable with the same name for the deployment version.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "deployment_version_variable",
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

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "deployment_version_variable",
  "value": "yet another one",
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
result <- ubiops::deployment_version_environment_variables_update(
  deployment.name, id, version, data
)

# Or provide directly
result <- ubiops::deployment_version_environment_variables_update(
  deployment.name, id, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_versions_create**
> deployment_versions_create(deployment.name, data)

Create deployment versions

## Description
Create a version for a deployment. The first version of a deployment is set as default.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version. This field is only used for versions with **batch deployment mode**.

### Required Parameters

- `version`: Name of the version of the deployment

### Optional Parameters

- `language`: Language in which the version is provided. It can be python3.6, python3.7, python3.8, python3.9, python3.6_cuda, python3.7_cuda, python3.8_cuda, python3.9_cuda or r4.0. The default value is python3.7.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB. This value determines the memory allocated to the version: it should be enough to encompass the deployment file and all requirements that need to be installed. The default value is 2048. The minimum and maximum values are 256 and 16384 respectively.
- `instance_type`: Reserved instance type for the version. This value determines the allocation of memory to the version: it should be enough to encompass the deployment file and all requirements that need to be installed. The default value is 2048mb. The minimum and maximum values are 256mb and 16384mb respectively.
- `maximum_instances`: Upper bound of number of versions running. The default value is 5. *Indicator of resource capacity:* if many deployment requests need to be handled in a short time, this number can be set higher to avoid long waiting times.
- `minimum_instances`: Lower bound of number of versions running. The default value is 0. Set this value greater than 0 to always have a always running version.
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped. The default value is 300, the minimum value is 10 (300 for GPU deployments) and the maximum value is 3600. A high value means that the version stays available longer. Sending requests to a running version means that it will be already initialized and thus take a shorter timer.

- `description`: Description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version. It defaults to 604800 seconds (1 week).
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `deployment_mode`: the type of the deployment version. It can be one of the following:
    - *express* - Direct requests can be made to the deployment version.
    - *batch* - Batch requests can be made to the deployment version.

If the time that a request takes does not matter, keep the default values.

## Request Examples

```
{
  "version": "version-1",
  "language": "python3.8"
}
```


```
{
  "version": "version-1",
  "language": "r4.0",
  "instance_type": "512mb"
}
```


```
  "version": "version-1",
  "language": "python3.6_cuda",
  "instance_type": "16384mb_t4",
  "maximum_instances": 1
```

```
{
  "version": "version-1",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "monitoring": "notification-group-1"
}
```

### Response Structure
Details of the created version

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: Active revision of the version. It is initialised as None since there are no deployment files uploaded for the version yet.
- `latest_build`: Latest build of the version. It is initialised as None since no build is triggered for the version yet.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following: *none*, *metadata* or *full*.
- `deployment_mode`: the type of the deployment version

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.8",
  "status": "unavailable",
  "active_revision": null,
  "latest_build": null,
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 5,
  "minimum_instances": 0,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "deployment_mode": "express"
}
```

### Example
```R
data <- list(
  version = "version",
  language = 'python3.7',  # (optional)
  memory_allocation = 0,  # (optional)
  instance_type = "instance_type",  # (optional)
  maximum_instances = 0,  # (optional)
  minimum_instances = 0,  # (optional)
  maximum_idle_time = 0,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  monitoring = "monitoring",  # (optional)
  request_retention_time = 0,  # (optional)
  request_retention_mode = 'full',  # one of: [none, metadata, full]  (optional)
  deployment_mode = 'express',  # one of: [express, batch]  (optional)
  default_notification_group = "default_notification_group"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_versions_create(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployment_versions_create(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_versions_delete**
> deployment_versions_delete(deployment.name, version)

Delete deployment version

## Description
Delete a deployment version. The version cannot be deleted if:
- It is referenced in a pipeline, it must be removed from the pipeline first.
- It is the default version of its deployment and is referenced in a request schedule.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployment_versions_delete(
  deployment.name, version
)

# Or provide directly
ubiops::deployment_versions_delete(
  deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_versions_get**
> deployment_versions_get(deployment.name, version)

Get deployment version

## Description
Retrieve details of a version of a deployment in a project

### Response Structure
Details of a version

- `id`: Unique identifier for the version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of deployment pods running in parallel
- `minimum_instances`: Lower bound of number of deployment pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `last_file_upload`: The date when a deployment file was last uploaded for the version
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `deployment_mode`: the type of the deployment version

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.7",
  "status": "available",
  "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
  "latest_build": "9f7fd6ec-53b7-41c6-949e-09efc2ee2d31",
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "last_file_uploaded": "2020-06-21T09:03:01.875391Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "deployment_mode": "express"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_versions_get(
  deployment.name, version
)

# Or provide directly
result <- ubiops::deployment_versions_get(
  deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_versions_list**
> deployment_versions_list(deployment.name, labels=NULL)

List deployment versions

## Description
Versions can be filtered according to the labels they have by giving labels as a query parameter. Versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the versions

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory usage for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `deployment_mode`: the type of the deployment version

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "description": "",
    "language": "python3.8",
    "status": "available",
    "active_revision": "da27ef7c-aa3f-4963-a815-6ebf1865638e",
    "latest_build": "0f4a94c6-ec4c-4d1e-81d7-8f3e40471f75",
    "memory_allocation": 512,
    "instance_type": "512mb",
    "maximum_instances": 4,
    "minimum_instances": 1,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "monitoring": "notification-group-1",
    "default_notification_group": null,
    "request_retention_time": 604800,
    "request_retention_mode": "full",
    "deployment_mode": "express"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "description": "",
    "language": "r4.0",
    "status": "available",
    "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
    "latest_build": "4534e479-ea2e-4161-876a-1d382191a031",
    "memory_allocation": 256,
    "instance_type": "256mb",
    "maximum_instances": 5,
    "minimum_instances": 0,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-2",
    "default_notification_group": "notification-group-2",
    "request_retention_time": 86400,
    "request_retention_mode": "metadata",
    "deployment_mode": "batch"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_versions_list(
  deployment.name,
  labels = NULL
)

# Or provide directly
result <- ubiops::deployment_versions_list(
  deployment.name,
  labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployment_versions_update**
> deployment_versions_update(deployment.name, version, data)

Update deployment version

## Description
Update a version of a deployment in a project. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version. This field is only used for versions with **batch deployment mode**.

### Optional Parameters

- `version`: New name for the version
- `memory_allocation`: (deprecated) New reserved memory for the version in MiB
- `instance_type`: New instance type for the version
- `maximum_instances`: New upper bound of number of versions running
- `minimum_instances`: New lower bound of number of versions running
- `maximum_idle_time`: New maximum time in seconds a version stays idle before it is stopped
- `description`: New description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored

## Request Examples

```
{
  "version": "new-version"
}
```


```
{
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "monitoring": "notification-group-1"
}
```

### Response Structure
Details of the updated version

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `last_file_upload`: The date when a deployment file was last uploaded for the version
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following: *none*, *metadata* or *full*.
- `deployment_mode`: the type of the deployment version

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.8",
  "status": "available",
  "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
  "latest_build": "0d07337e-96d6-4ce6-8c63-c2f07edd2ce4",
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-23T18:04:76.123754Z",
  "last_file_uploaded": "2020-06-21T09:03:01.875391Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "deployment_mode": "express"
}
```

### Example
```R
data <- list(
  version = "version",  # (optional)
  memory_allocation = 0,  # (optional)
  instance_type = "instance_type",  # (optional)
  maximum_instances = 0,  # (optional)
  minimum_instances = 0,  # (optional)
  maximum_idle_time = 0,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  monitoring = "monitoring",  # (optional)
  request_retention_time = 0,  # (optional)
  request_retention_mode = "request_retention_mode",  # one of: [none, metadata, full]  (optional)
  default_notification_group = "default_notification_group"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_versions_update(
  deployment.name, version, data
)

# Or provide directly
result <- ubiops::deployment_versions_update(
  deployment.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployments_create**
> deployments_create(data)

Create deployments

## Description
Create a deployment by defining the input/output type and input/output fields. In case of **plain** type of input or output, input and output fields should not be given or passed as an empty list.

Possible data types for the input and output fields are:
- **int**: integer
- **string**: string
- **double**: double precision floating point
- **bool**: boolean value (False/True)
- **timestamp**: timestamp
- **array_int**: an array of integers
- **array_double**: an array of double precision floating points
- **array_string**: an array of strings
- **blob**: a blob field. This type of field can be used to pass blobs to the deployment. In deployment and pipeline requests, the uuid of a previously uploaded blob must be provided for this field.

Possible widgets for the input fields are:
- **textbox**: textbox
- **numberbox**: numberbox
- **slider**: slider
- **dropdown**: dropdown
- **switch**: switch
- **button**: upload button
- **drawer**: drawer
- **image_preview**: image upload with preview

Possible widgets for the output fields are:
- **textbox**: textbox
- **button**: download button
- **image_preview**: image preview

### Required Parameters

- `name`: Name of the deployment. It is unique within a project.
- `input_type`: Type of the input of the deployment. It can be either structured or plain.
- `output_type`: Type of the output of the deployment. It can be either structured or plain.
- `input_fields`: The list of required deployment input fields. It must contain the fields: name and data_type, and it may contain the field: widget. The name of an input field is unique for a deployment.
- `output_fields`: The list of required deployment output fields. It must contain the fields: name and data_type, and it may contain the field: widget. The name of an output field is unique for a deployment.

### Optional Parameters

- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples
A deployment with structured input and output type

```
{
  "name": "deployment-1",
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

A deployment with plain input type

```
{
  "name": "deployment-1",
  "description": "Deployment one"
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

A deployment with plain input and output type

```
{
  "name": "deployment-1",
  "input_type": "plain",
  "output_type": "plain"
  "labels": {
    "type": "deployment"
  }
}
```

A deployment with structured input and output type and field widgets
```
{
  "name": "deployment-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {
        "type": "slider",
        "configuration": {"min": 0, "max": 10, "default": 4, "step": 2}
      }
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {
        "type": "numberbox",
        "configuration": {"min": 0, "max": 1, "default": 0.5, "step": 0.1}
      }
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    }
  ]
}
```

### Response Structure
Details of the created deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is created
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type
- `output_fields`: The list of deployment output fields containing name and data_type
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-18T08:32:14.876451Z"
}
```

### Example
```R
data <- list(
  name = "name",
  description = "description",  # (optional)
  input_type = "input_type",  # one of: [structured, plain] 
  output_type = "output_type",  # one of: [structured, plain] 
  input_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",  # one of: [int, string, double, bool, array_int, array_double, array_string, blob] 
      widget = widget  # (optional)
    )
  ),
  output_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",  # one of: [int, string, double, bool, array_int, array_double, array_string, blob] 
      widget = widget  # (optional)
    )
  ),
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployments_create(
  data
)

# Or provide directly
result <- ubiops::deployments_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployments_delete**
> deployments_delete(deployment.name)

Delete a deployment

## Description
Delete a deployment. If any of the versions of the deployment are referenced in a pipeline, the deployment cannot be deleted.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::deployments_delete(
  deployment.name
)

# Or provide directly
ubiops::deployments_delete(
  deployment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployments_get**
> deployments_get(deployment.name)

Get details of a deployment

## Description
Retrieve details of a single deployment in a project

### Response Structure
Details of a deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name, data_type and widget
- `output_fields`: The list of deployment output fields containing name, data_type and widget
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `default_version`: Default version of the deployment.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "default_version": "v1"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployments_get(
  deployment.name
)

# Or provide directly
result <- ubiops::deployments_get(
  deployment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployments_list**
> deployments_list(labels=NULL)

List deployments

## Description
Deployments can be filtered according to the labels they have by giving labels as a query parameter. Deployments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the deployment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the deployments in the project

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type. It is empty in case of plain input type deployments.
- `output_fields`: The list of deployment output fields containing name and data_type. It is empty in case of plain output type deployments.
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated

## Response Examples

```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "deployment-1",
    "project": "project-1",
    "description": "Temperature deployment",
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
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "deployment-2",
    "project": "project-1",
    "description": "Deployment two",
    "input_type": "structured",
    "output_type": "plain",
    "input_fields": [
      {
        "name": "input-field",
        "data_type": "int"
      }
    ],
    "output_fields": [],
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  },
  {
    "id": "bd3fae9d-aeec-4cf3-8ef0-5f9224d41904",
    "name": "deployment-3",
    "description": "",
    "project": "project-1",
    "input_type": "plain",
    "output_type": "plain",
    "input_fields": [],
    "output_fields": [],
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployments_list(
  
  labels = NULL
)

# Or provide directly
result <- ubiops::deployments_list(
  
  labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **deployments_update**
> deployments_update(deployment.name, data)

Update a deployment

## Description
Update a deployment

### Optional Parameters

- `name`: New name for the deployment
- `description`: New description for the deployment
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `default_version`: Name of a version of this deployment which will be assigned as default. Only **available** versions can be assigned as default.
- `input_fields`: New input fields for the deployment
- `output_fields`: New output fields for the deployment

Input and output fields can be updated (name, data type or widget), added or removed. For deployments that are attached in a pipeline or contain any input/output widgets, fields must be updated one at a time so that the updates can be performed while preserving the mapping/widgets.

## Request Examples

```
{
  "name": "new-deployment-name"
}
```

### Response Structure
Details of the updated deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name, data_type and (optional) widget
- `output_fields`: The list of deployment output fields containing name, data_type and (optional) widget
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `default_version`: Default version of the deployment. If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-deployment-name",
  "project": "project-1",
  "description": "New deployment description",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "default_version": "v1"
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  default_version = "default_version",  # (optional)
  description = "description",  # (optional)
  input_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",  # one of: [int, string, double, bool, array_int, array_double, array_string, blob] 
      widget = widget  # (optional)
    )
  ),
  output_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",  # one of: [int, string, double, bool, array_int, array_double, array_string, blob] 
      widget = widget  # (optional)
    )
  ),
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployments_update(
  deployment.name, data
)

# Or provide directly
result <- ubiops::deployments_update(
  deployment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **revisions_file_download**
> revisions_file_download(deployment.name, revision.id, version)

Download deployment file

## Description
Download the deployment file of a revision of a version

### Response Structure

- `file`: Deployment file of the version

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::revisions_file_download(
  deployment.name, revision.id, version
)

# Or provide directly
result <- ubiops::revisions_file_download(
  deployment.name, revision.id, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# Save file manually
file_name <- result$getFileName()

output <- file(file.path(getwd(), file_name), "wb")
readr::write_file(result$getContent(), output)
close(output)

# Or save file directly in temp folder
# by using environment variables or providing directly
Sys.setenv("UBIOPS_TEMP_FOLDER_PATH" = getwd())
output_path <- ubiops::revisions_file_download(
  deployment.name, revision.id, version,
  preload_content=TRUE
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **revisions_file_upload**
> revisions_file_upload(deployment.name, version, file=NULL, source.deployment=NULL, source.version=NULL, template.deployment.id=NULL)

Upload deployment file

## Description
Upload a deployment file for a version. Uploading a deployment file will create a new revision and trigger a build.
This file should contain the deployment that will be run. It should be provided as a zip and a template can be found on https://github.com/UbiOps/deployment-template. The file is saved under a directory in the storage specified in the settings.

It is **also possible** to provide a source version from which the deployment file will be copied. This will also create a new revision and trigger a build.

### Optional Parameters

- `file`: Deployment file
- `source_deployment`: Name of the deployment from which the deployment file will be copied
- `source_version`: Version from which the deployment file will be copied
- `template_deployment_id`: UUID of a template deployment which will be used as the source of the deployment file

Either **file** or **source_deployment** and **source_version** must be provided. source_deployment and source_version must be provided together.

### Response Structure

- `success`: Boolean indicating whether the deployment file upload/copy succeeded or not
- `revision`: UUID of the created revision for the file upload
- `build`: UUID of the build created for the file upload

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::revisions_file_upload(
  deployment.name, version,
  file = NULL, source.deployment = NULL, source.version = NULL, template.deployment.id = NULL
)

# Or provide directly
result <- ubiops::revisions_file_upload(
  deployment.name, version,
  file = NULL, source.deployment = NULL, source.version = NULL, template.deployment.id = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **revisions_get**
> revisions_get(deployment.name, revision.id, version)

Get revision

## Description
Retrieve details of a single revision of a version

### Response Structure
A dictionary containing details of the build

- `id`: Unique identifier for the revision (UUID)
- `version`: Version to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the deployment file. In case the revision is created by a service, the field will have a "UbiOps" value.

## Response Examples

```
{
  "id": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
  "version": "v1",
  "creation_date": "2020-12-23T16:35:13.069+00:00",
  "created_by": "test@example.com"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::revisions_get(
  deployment.name, revision.id, version
)

# Or provide directly
result <- ubiops::revisions_get(
  deployment.name, revision.id, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **revisions_list**
> revisions_list(deployment.name, version)

List revisions

## Description
List all revisions associated with a version. A new revision is created every time a new deployment file is uploaded for a version.

### Response Structure
A list of details of the revisions

- `id`: Unique identifier for the revision (UUID)
- `version`: Version to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the deployment file. In case the revision is created by a service, the field will have a "UbiOps" value.

## Response Examples

```
[
  {
    "id": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
    "version": "v1",
    "creation_date": "2020-12-23T16:15:11.181+00:00",
    "created_by": "UbiOps"
  },
  {
    "id": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
    "version": "v1",
    "creation_date": "2020-12-23T16:35:13.069+00:00",
    "created_by": "test@example.com"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::revisions_list(
  deployment.name, version
)

# Or provide directly
result <- ubiops::revisions_list(
  deployment.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


