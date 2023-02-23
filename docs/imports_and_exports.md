# ImportsAndExports

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exports_create**](imports_and_exports.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
[**exports_delete**](imports_and_exports.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
[**exports_download**](imports_and_exports.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
[**exports_get**](imports_and_exports.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
[**exports_list**](imports_and_exports.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
[**imports_create**](imports_and_exports.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
[**imports_delete**](imports_and_exports.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
[**imports_download**](imports_and_exports.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
[**imports_get**](imports_and_exports.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
[**imports_list**](imports_and_exports.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
[**imports_update**](imports_and_exports.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import


# **exports_create**
> exports_create(data)

Create an export

## Description
Create an export by selecting the objects in the export

### Optional Parameters

- `deployments`: Dictionary containing the deployments to export
- `pipelines`: Dictionary containing the pipelines to export
- `environment_variables`: Dictionary containing the project-level environment variables to export

## Request Examples


```
{
  "deployments": {
    "deployment-1": {
      "versions": {
        "version-1": {
          "environment_variables": {
            "VERSION_ENV_VAR_NAME_1": {
              "include_value": true
            },
            "VERSION_ENV_VAR_NAME_2": {
              "include_value": false
            }
          }
        },
        "version-2": {}
      },
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_NAME_1": {
          "include_value": false
        }
      }
    },
    "deployment-2": {
      "versions": {}
    }
  },
  "pipelines": {
    "pipeline-1": {
      "versions": {
        "version-1": {},
        "version-2": {}
      }
    },
    "pipeline-2": {
      "versions": {}
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_NAME_1": {
      "include_value": false
    }
  }
}
```

### Response Structure
Details of the created export

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

### Example
```R
data <- list(
  deployments = list(key = list(key = "value")),  # (optional)
  pipelines = list(key = list(key = "value")),  # (optional)
  environment_variables = list(key = list(key = "value"))  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::exports_create(
  data
)

# Or provide directly
result <- ubiops::exports_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **exports_delete**
> exports_delete(export.id)

Delete an export

## Description
Delete an export from a project

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::exports_delete(
  export.id
)

# Or provide directly
ubiops::exports_delete(
  export.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **exports_download**
> exports_download(export.id)

Download an export

## Description
Download an export in a project

### Response Structure

- `file`: Zip file

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::exports_download(
  export.id
)

# Or provide directly
result <- ubiops::exports_download(
  export.id,
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
output_path <- ubiops::exports_download(
  export.id,
  preload_content=TRUE
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **exports_get**
> exports_get(export.id)

Get an export

## Description
Get the details of an export in a project

### Response Structure

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes
- `deployments`: Dictionary of the deployments in the export
- `pipelines`: Dictionary of the pipelines in the export
- `environment_variables`: Dictionary of the environment variables in the export

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::exports_get(
  export.id
)

# Or provide directly
result <- ubiops::exports_get(
  export.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **exports_list**
> exports_list(status=NULL)

List exports

## Description
List all exports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the export. Can be 'pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the exports in the project

- `id`: Unique identifier for the export (UUID)
- `creation_date`: Time the export was created
- `status`: The status of the export
- `error_message`: The error message in case of a failure
- `size`: Size of the export in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": null
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "completed",
    "error_message": "",
    "size": 86400
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::exports_list(
  
  status = NULL
)

# Or provide directly
result <- ubiops::exports_list(
  
  status = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_create**
> imports_create(file=NULL, import.link=NULL, export.id=NULL, skip.confirmation=NULL)

Create an import

## Description
Create an import by uploading a zip file, providing a link to an import file or by giving an export id.
Only one of the fields `file`, `import_link` or `export_id` may be given at a time.
When providing a link to an import file, make sure it is publicly downloadable.

### Required Parameters
Only one of the following fields should be given:

- `file`: A zip file
- `import_link`: url to a publicly downloadable zip file
- `export_id`: UUID of a previously created export in the same project

### Optional Parameters

- `skip_confirmation`: Whether to skip the confirmation step, default to False

### Response Structure
Details of the created import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": 28391
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::imports_create(
  
  file = NULL, import.link = NULL, export.id = NULL, skip.confirmation = NULL
)

# Or provide directly
result <- ubiops::imports_create(
  
  file = NULL, import.link = NULL, export.id = NULL, skip.confirmation = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_delete**
> imports_delete(import.id)

Delete an import

## Description
Delete an import from a project

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::imports_delete(
  import.id
)

# Or provide directly
ubiops::imports_delete(
  import.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_download**
> imports_download(import.id)

Download an import

## Description
Download an import in a project

### Response Structure

- `file`: Zip file

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::imports_download(
  import.id
)

# Or provide directly
result <- ubiops::imports_download(
  import.id,
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
output_path <- ubiops::imports_download(
  import.id,
  preload_content=TRUE
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_get**
> imports_get(import.id)

Get an import

## Description
Get the details of an import in a project

### Response Structure

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes
- `deployments`: Dictionary of the deployments in the import
- `pipelines`: Dictionary of the pipelines in the import
- `environment_variables`: Dictionary of the environment variables in the import

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::imports_get(
  import.id
)

# Or provide directly
result <- ubiops::imports_get(
  import.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_list**
> imports_list(status=NULL)

List imports

## Description
List all imports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the import. Can be 'pending', 'scanning', 'confirmation', 'confirmation_pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the imports in the project

- `id`: Unique identifier for the import (UUID)
- `creation_date`: Time the import was created
- `status`: The status of the import
- `error_message`: The error message in case of a failure
- `size`: Size of the import in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 126832
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 86400
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::imports_list(
  
  status = NULL
)

# Or provide directly
result <- ubiops::imports_list(
  
  status = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **imports_update**
> imports_update(import.id, data)

Confirm an import

## Description
Confirm (and update) an import by selecting the objects in the import

### Optional Parameters

- `deployments`: Dictionary containing the deployments to create
- `pipelines`: Dictionary containing the pipelines to create
- `environment_variables`: Dictionary containing the project-level environment variables to create

## Request Examples


```
{
    "deployments": {
    "deployment-1: {
      "description": "",
      "labels": {
        "my-label": "my-value"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "zip": "deployments/deployment_deployment-1/versions/deployment_deployment-1_version_v1.zip",
          "description": "",
          "labels": {},
          "language": "python3.7",
          "maximum_idle_time": 300,
          "maximum_instances": 5,
          "instance_type": "256mb",
          "minimum_instances": 0,
          "environment_variables": {
            "VERSION_ENV_VAR_1": {
              "value": "my-secret-value",
              "secret": true
            },
            "VERSION_ENV_VAR_2": {
              "value": "test2"
            }
          },
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ],
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_1": {
          "value": "my-secret-value",
          "secret": true
        },
        "DEPLOYMENT_ENV_VAR_2": {
          "value": "test"
        }
      }
    }
  },
  "pipelines": {
    "pipeline-1: {
      "description": "",
      "labels": {
        "test": "label"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "description": "",
          "labels": {},
          "objects": [
            {
              "name": "obj-1",
              "reference_name": "deployment-1",
              "reference_version": "v1"
            }
          ],
          "attachments": [
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "input",
                      "destination_field_name": "input"
                    }
                  ],
                  "source_name": "pipeline_start"
                }
              ],
              "destination_name": "obj-1"
            },
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "output",
                      "destination_field_name": "output"
                    }
                  ],
                  "source_name": "obj-1"
                }
              ],
              "destination_name": "pipeline_end"
            }
          ],
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ]
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_1": {
      "value": "value1",
      "secret": true
    },
    "PROJECT_ENV_VAR_2": {
      "value": "value2"
    }
  }
}
```

### Response Structure
Details of the updated import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

### Example
```R
data <- list(
  deployments = list(key = list(key = "value")),  # (optional)
  pipelines = list(key = list(key = "value")),  # (optional)
  environment_variables = list(key = list(key = "value"))  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::imports_update(
  import.id, data
)

# Or provide directly
result <- ubiops::imports_update(
  import.id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


