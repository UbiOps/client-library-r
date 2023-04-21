# Environments

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_builds_get**](environments.md#environment_builds_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Get build
[**environment_builds_list**](environments.md#environment_builds_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds | List builds
[**environment_builds_update**](environments.md#environment_builds_update) | **PATCH** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Update build
[**environment_revisions_file_download**](environments.md#environment_revisions_file_download) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/download | Download environment file
[**environment_revisions_file_upload**](environments.md#environment_revisions_file_upload) | **POST** /projects/{project_name}/environments/{environment_name}/revisions | Upload environment file
[**environment_revisions_get**](environments.md#environment_revisions_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id} | Get revision
[**environment_revisions_list**](environments.md#environment_revisions_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions | List revisions
[**environment_revisions_rebuild**](environments.md#environment_revisions_rebuild) | **POST** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/rebuild | Rebuild revision
[**environments_create**](environments.md#environments_create) | **POST** /projects/{project_name}/environments | Create environments
[**environments_delete**](environments.md#environments_delete) | **DELETE** /projects/{project_name}/environments/{environment_name} | Delete environment
[**environments_get**](environments.md#environments_get) | **GET** /projects/{project_name}/environments/{environment_name} | Get environment
[**environments_list**](environments.md#environments_list) | **GET** /projects/{project_name}/environments | List environments
[**environments_update**](environments.md#environments_update) | **PATCH** /projects/{project_name}/environments/{environment_name} | Update environment
[**environments_usage**](environments.md#environments_usage) | **GET** /projects/{project_name}/environments/{environment_name}/usage | List usage of environment


# **environment_builds_get**
> environment_builds_get(build.id, environment.name, revision.id)

Get build

## Description
Retrieve details of a build of an environment

### Response Structure
Details of a build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "success",
  "error_message": "",
  "trigger": "Rebuild triggered"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_builds_get(
  build.id, environment.name, revision.id
)

# Or provide directly
result <- ubiops::environment_builds_get(
  build.id, environment.name, revision.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_builds_list**
> environment_builds_list(environment.name, revision.id)

List builds

## Description
List builds of an environment. A build is triggered when a new environment file is uploaded.

### Response Structure
A list of details of the builds

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
[
  {
    "id": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
    "revision": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
    "creation_date": "2023-01-23T12:17:11.863+00:00",
    "status": "failed",
    "error_message": "Could not find the requirements file",
    "trigger": "Environment file upload"
  },
  {
    "id": "038ae310-6629-4887-952d-868b6e533b90",
    "revision": "8760570f-6eda-470b-99af-bde810d418d8",
    "creation_date": "2023-01-29T17:12:43.108+00:00",
    "status": "queued",
    "error_message": "",
    "trigger": "Environment file upload"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_builds_list(
  environment.name, revision.id
)

# Or provide directly
result <- ubiops::environment_builds_list(
  environment.name, revision.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_builds_update**
> environment_builds_update(build.id, environment.name, revision.id, data)

Update build

## Description
Cancel a build of an environment

### Required Parameters

- `status`: Status that the build will be updated to. It can only be cancelled.

## Request Examples

```
{
    "status": "cancelled"
}
```

### Response Structure
Details of the cancelled build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "cancelled",
  "error_message": "",
  "trigger": "Rebuild triggered"
}
```

### Example
```R
data <- list(
  status = "status"
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_builds_update(
  build.id, environment.name, revision.id, data
)

# Or provide directly
result <- ubiops::environment_builds_update(
  build.id, environment.name, revision.id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_revisions_file_download**
> environment_revisions_file_download(environment.name, revision.id)

Download environment file

## Description
Download the file of a revision of an environment

### Response Structure

- `file`: Environment file

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_revisions_file_download(
  environment.name, revision.id
)

# Or provide directly
result <- ubiops::environment_revisions_file_download(
  environment.name, revision.id,
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
output_path <- ubiops::environment_revisions_file_download(
  environment.name, revision.id,
  preload_content=TRUE
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_revisions_file_upload**
> environment_revisions_file_upload(environment.name, file=NULL, source.environment=NULL)

Upload environment file

## Description
Upload a file for an environment. Uploading a file will create a new revision and trigger a build. This file should contain all the dependencies that the environment should have in the zip format.

It is **also possible** to provide a source environment from which the environment file will be copied. This will also create a new revision and trigger a build.

### Optional Parameters

- `file`: Environment file
- `source_environment`: Environment from which the environment file will be copied

Either **file** or **source_environment** must be provided.

### Response Structure

- `success`: Boolean indicating whether the environment file upload/copy succeeded
- `revision`: ID of the created revision for the file upload
- `build`: ID of the build created for the file upload

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_revisions_file_upload(
  environment.name,
  file = NULL, source.environment = NULL
)

# Or provide directly
result <- ubiops::environment_revisions_file_upload(
  environment.name,
  file = NULL, source.environment = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_revisions_get**
> environment_revisions_get(environment.name, revision.id)

Get revision

## Description
Retrieve details of a revision of an environment

### Response Structure
Details of a revision

- `id`: Unique identifier for the revision
- `environment`: Environment to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the environment file. In case the revision is created by a service, the field will have a "UbiOps" value.
- `expired`: A boolean indicating whether the environment file has been deleted for the revision

## Response Examples

```
{
  "id": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
  "version": "python3-8-custom",
  "creation_date": "2023-01-29T17:12:43.108+00:00",
  "created_by": "test@example.com",
  "expired": false
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_revisions_get(
  environment.name, revision.id
)

# Or provide directly
result <- ubiops::environment_revisions_get(
  environment.name, revision.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_revisions_list**
> environment_revisions_list(environment.name)

List revisions

## Description
List revisions of an environment

### Response Structure
A list of details of the revisions

- `id`: Unique identifier for the revision
- `environment`: Environment to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the environment file. In case the revision is created by a service, the field will have a "UbiOps" value.
- `expired`: A boolean indicating whether the environment file has been deleted for the revision

## Response Examples

```
[
  {
    "id": "8760570f-6eda-470b-99af-bde810d418d8",
    "environment": "python3-8-custom",
    "creation_date": "2023-01-23T12:17:11.863+00:00",
    "created_by": "UbiOps",
    "expired": false
  },
  {
    "id": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
    "version": "python3-8-custom",
    "creation_date": "2023-01-29T17:12:43.108+00:00",
    "created_by": "test@example.com",
    "expired": false
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_revisions_list(
  environment.name
)

# Or provide directly
result <- ubiops::environment_revisions_list(
  environment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environment_revisions_rebuild**
> environment_revisions_rebuild(environment.name, revision.id, data=NULL)

Rebuild revision

## Description
Trigger a rebuild for a revision of an environment

### Response Structure
Details of the created build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "queued",
  "error_message": "",
  "trigger": "Rebuild triggered"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environment_revisions_rebuild(
  environment.name, revision.id,
  data = NULL
)

# Or provide directly
result <- ubiops::environment_revisions_rebuild(
  environment.name, revision.id,
  data = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_create**
> environments_create(data)

Create environments

## Description
Create a custom environment

### Required Parameters

- `name`: Name of the environment
- `base_environment`: Base environment name on which this environment is based

### Optional Parameters

- `display_name`: Display name of the environment. If not set, 'name' is used instead.
- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "python3-8-custom",
  "base_environment": "python3.8"
}
```


```
{
  "name": "python3-8-custom-1",
  "display_name": "Custom Python 3.8",
  "base_environment": "python3.8"
}
```

### Response Structure
Details of the created environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-8-custom",
  "display_name": "Custom Python 3.8",
  "base_environment": "python3.8",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T08:32:14.876451Z",
  "description": "Custom environment based on Python 3.8",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false
}
```

### Example
```R
data <- list(
  name = "name",
  display_name = "display_name",  # (optional)
  base_environment = "base_environment",
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environments_create(
  data
)

# Or provide directly
result <- ubiops::environments_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_delete**
> environments_delete(environment.name)

Delete environment

## Description
Delete an environment. The environment cannot be deleted if it is referenced by a deployment version.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::environments_delete(
  environment.name
)

# Or provide directly
ubiops::environments_delete(
  environment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_get**
> environments_get(environment.name)

Get environment

## Description
Retrieve details of an environment

### Response Structure
Details of an environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `active_revision`: UUID of the active revision of the environment
- `active_build`: UUID of the active build of the environment
- `latest_revision`: UUID of the latest revision of the environment
- `latest_build`: UUID of the latest build of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-8-custom",
  "display_name": "Custom Python 3.8",
  "base_environment": "python3.8",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.8",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false,
  "active_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "active_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
  "latest_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "latest_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environments_get(
  environment.name
)

# Or provide directly
result <- ubiops::environments_get(
  environment.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_list**
> environments_list(labels=NULL, environment.type=NULL)

List environments

## Description
Environments can be filtered according to the labels they have by giving labels as a query parameter. Environments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the environment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.
- `environment_type`: Filter on the type of the environment. It can be one of the following: 'base', 'custom' or 'all'. The default value is 'all'.

### Response Structure
A list of details of the environments

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined. It is null for base environments.
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created

## Response Examples

```
[
  {
    "id": "1319895f-467b-4732-9804-7de500099233",
    "name": "python3-8",
    "display_name": "Python 3.8",
    "base_environment": null,
    "project": null,
    "creation_date": "2023-03-01T08:32:14.876451Z",
    "last_updated": "2023-03-01T10:52:23.124784Z",
    "description": "Base environment containing Python 3.8",
    "labels": {},
    "gpu_required": false,
    "status": "active",
    "implicit": false
  },
  {
    "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
    "name": "python3-8-custom",
    "display_name": "Custom Python 3.8",
    "base_environment": "python3.8",
    "project": "project-1",
    "creation_date": "2023-03-02T12:15:43.124751Z",
    "last_updated": "2023-03-03T13:14:23.865421Z",
    "description": "Custom environment based on Python 3.8",
    "labels": {
      "type": "environment"
    },
    "gpu_required": false,
    "status": "active",
    "implicit": false
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environments_list(
  
  labels = NULL, environment.type = NULL
)

# Or provide directly
result <- ubiops::environments_list(
  
  labels = NULL, environment.type = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_update**
> environments_update(environment.name, data)

Update environment

## Description
Update an environment. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `name`: Name of the environment
- `display_name`: Display name of the environment
- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "new-python3-8-custom"
}
```

### Response Structure
Details of the updated environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `active_revision`: UUID of the active revision of the environment
- `active_build`: UUID of the active build of the environment
- `latest_revision`: UUID of the latest revision of the environment
- `latest_build`: UUID of the latest build of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "new-python3-8-custom",
  "display_name": "Custom Python 3.8",
  "base_environment": "python3.8",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.8",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false,
  "active_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "active_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
  "latest_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "latest_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6"
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  display_name = "display_name",  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environments_update(
  environment.name, data
)

# Or provide directly
result <- ubiops::environments_update(
  environment.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **environments_usage**
> environments_usage(environment.name, environment.type=NULL)

List usage of environment

## Description
List the deployment versions used by an environment

### Response Structure
A list of details of the deployment versions

- `id`: Unique identifier for the deployment version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `environment`: Environment of the version
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the version

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "environment": "python3-8",
    "environment_display_name": "Python 3.8",
    "status": "available"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "environment": "python3-8",
    "environment_display_name": "Python 3.8",
    "status": "unavailable"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::environments_usage(
  environment.name,
  environment.type = NULL
)

# Or provide directly
result <- ubiops::environments_usage(
  environment.name,
  environment.type = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


