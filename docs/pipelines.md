# Pipelines

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressions_evaluate**](pipelines.md#expressions_evaluate) | **POST** /expressions/evaluate | Evaluate expression
[**pipeline_audit_events_list**](pipelines.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_version_object_environment_variables_list**](pipelines.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_versions_create**](pipelines.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
[**pipeline_versions_delete**](pipelines.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
[**pipeline_versions_get**](pipelines.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
[**pipeline_versions_list**](pipelines.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
[**pipeline_versions_update**](pipelines.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
[**pipelines_create**](pipelines.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](pipelines.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
[**pipelines_get**](pipelines.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
[**pipelines_list**](pipelines.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](pipelines.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline


# **expressions_evaluate**
> expressions_evaluate(data)

Evaluate expression

## Description
Evaluate a pipeline version operator expression.

### Required Parameters

- `expression`: The expression to evaluate.
- `input_fields`: A list of input fields with name, data_type.
- `request_data`: Data to test the expression with. All its keys must be defined in 'input_fields'.

## Request Examples

```
{
  "expression": "var1 + 10",
  "input_fields": [
    {
      "name": "var1",
      "data_type": "int"
    }
  ],
  "request_data": {
    "var1": 123
  }
}
```

### Response Structure

- `result`: The result of the expression

## Response Examples

```
{
  "result": 133
}
```

### Example
```R
data <- list(
  expression = "expression",
  input_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type"
    )
  ),
  request_data = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::expressions_evaluate(
  data
)

# Or provide directly
result <- ubiops::expressions_evaluate(
  data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_audit_events_list**
> pipeline_audit_events_list(pipeline.name, action=NULL, limit=NULL, offset=NULL)

List audit events for a pipeline

## Description
List all audit events for a pipeline including objects and attachments

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events for a pipeline

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
    "id": "44f326de-0ee3-4741-b72e-69e31b3ec55f",
    "date": "2020-10-23T12:21:12.460+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created pipeline object deployment-1 in version v1 of pipeline pipeline-1",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  },
  {
    "id": "905cdc19-a02c-4f09-b2fb-42d92da21bda",
    "date": "2020-10-23T12:21:37.247+00:00",
    "action": "update",
    "user": "user@example.com",
    "event": "Updated pipeline object deployment-object in version v1 of pipeline pipeline-1: name changed from deployment-1 to deployment-object",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipeline_audit_events_list(
  pipeline.name,
  action = NULL, limit = NULL, offset = NULL
)

# Or provide directly
result <- ubiops::pipeline_audit_events_list(
  pipeline.name,
  action = NULL, limit = NULL, offset = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_version_object_environment_variables_list**
> pipeline_version_object_environment_variables_list(name, pipeline.name, version)

List pipeline object environment variables

## Description
List environment variables accessible to objects in the pipeline version

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or `version`
- `inheritance_name`: Name of the parent object that this variable is inherited from

## Response Examples

```
[
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
result <- ubiops::pipeline_version_object_environment_variables_list(
  name, pipeline.name, version
)

# Or provide directly
result <- ubiops::pipeline_version_object_environment_variables_list(
  name, pipeline.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_versions_create**
> pipeline_versions_create(pipeline.name, data)

Create pipeline versions

## Description
Create a version for a pipeline. The first version of a pipeline is set as default.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

### Required Parameters

- `version`: Name of the version of the pipeline

### Optional Parameters

- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version. It defaults to 604800 seconds (1 week).
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
    - `name`: The name of the object in the pipeline. It must be unique within the pipeline.
    - `reference_type`: The type of object it references. It can be 'deployment', 'pipeline' or 'operator'. It defaults to 'deployment'.
    - `reference_name`: The name of the object it references. The name of the deployment, pipeline or operator.
    - `version`: Optional version for the referenced deployment or pipeline. If not provided, it defaults to the default version of the deployment or pipeline.
    - `configuration`: The configuration specific for the referenced operator, or the 'on_error' policy for the deployment or pipeline.
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1"
}
```


```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1",
  "request_retention_time": 604800,
  "request_retention_mode": "full"
}
```

A pipeline version referencing a default deployment version and a specific deployment version

```
{
  "version": "v1",
  "objects": [
    {
      "name": "default-version",
      "reference_name": "deployment-1",
      "reference_type": "deployment"
    },
    {
      "name": "specific-version",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ]
}
```

A pipeline version with objects and attachments
```
{
  "version": "v1",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

A pipeline version with a sub-pipeline
```
{
  "version": "v1",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "pipeline-1",
      "reference_type": "pipeline",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

A pipeline version with deployment object configuration
```
{
  "version": "v1",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "configuration": {
        "on_error": "stop"
      }
    }
  ]
}
```

A pipeline version with operators
```
{
  "version": "v1",
  "objects": [
    {
      "name": "operator-if-condition",
      "reference_name": "if-condition",
      "reference_type": "operator",
      "configuration": {
        "expression": "input > 0",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": []
      }
    },
    {
      "name": "operator-variable",
      "reference_name": "pipeline-variable",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [],
        "output_fields": [{"name": "variable", "data_type": "int"}],
        "output_values": [{"name": "variable", "value": 1}]
      }
    },
    {
      "name": "operator-function",
      "reference_name": "function",
      "reference_type": "operator",
      "configuration": {
        "expression": "input * 5",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    },
    {
      "name": "operator-if-condition-2",
      "reference_name": "if-condition",
      "reference_type": "operator",
      "configuration": {
        "expression": "input > 50",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": []
      }
    },
    {
      "name": "operator-raise-error",
      "reference_name": "raise-error",
      "reference_type": "operator",
      "configuration": {
        "error_message": "My error message!",
        "input_fields": [],
        "output_fields": []
      }
    },
    {
      "name": "operator-one-to-many",
      "reference_name": "one-to-many",
      "reference_type": "operator",
      "configuration": {
        "batch_size": null,
        "input_fields": [{"name": "output", "data_type": "int"}],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    },
    {
      "name": "operator-many-to-one",
      "reference_name": "many-to-one",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": [{"name": "input", "data_type": "int"}]
      }
    },
    {
      "name": "operator-count-many",
      "reference_name": "count-many",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    }
  ],
  "attachments": [
    {
      "destination_name": "operator-if-condition",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-function",
      "sources": [
        {
          "source_name": "operator-if-condition",
          "mapping": []
        },
        {
          "source_name": "operator-variable",
          "mapping": [
            {
              "source_field_name": "variable",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-one-to-many",
      "sources": [
        {
          "source_name": "operator-function",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "output"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-count-many",
      "sources": [
        {
          "source_name": "operator-one-to-many",
          "mapping": []
        }
      ]
    },
    {
      "destination_name": "operator-many-to-one",
      "sources": [
        {
          "source_name": "operator-one-to-many",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-if-condition-2",
      "sources": [
        {
          "source_name": "operator-many-to-one",
          "mapping": [
            {
              "source_field_name": "input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-raise-error",
      "sources": [
        {
          "source_name": "operator-if-condition-2",
          "mapping": []
        }
      ]
    },
    {
      "destination_name": "pipeline_end",
      "sources": [
        {
          "source_name": "operator-count-many",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "pipeline-output"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response Structure
Details of the created pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `default`: A boolean indicating whether the version is the default version
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "default": true,
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

### Example
```R
data <- list(
  version = "version",
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  monitoring = "monitoring",  # (optional)
  request_retention_time = 0,  # (optional)
  request_retention_mode = 'full',  # (optional)
  default_notification_group = "default_notification_group",  # (optional)
  objects = list(  # (optional)
    list(
      name = "name",
      reference_type = 'deployment',  # (optional)
      reference_name = "reference_name",
      version = "version",  # (optional)
      configuration = list(key = "value")  # (optional)
    )
  ),
  attachments = list(  # (optional)
    list(
      destination_name = "destination_name",
      sources = list(  # (optional)
        list(
          source_name = "source_name",
          mapping = list(  # (optional)
            list(
              source_field_name = source_field_name,
              destination_field_name = destination_field_name
            )
          )
        )
      )
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipeline_versions_create(
  pipeline.name, data
)

# Or provide directly
result <- ubiops::pipeline_versions_create(
  pipeline.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_versions_delete**
> pipeline_versions_delete(pipeline.name, version)

Delete pipeline version

## Description
Delete a pipeline version. This will also delete all objects and attachments in the pipeline version.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::pipeline_versions_delete(
  pipeline.name, version
)

# Or provide directly
ubiops::pipeline_versions_delete(
  pipeline.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_versions_get**
> pipeline_versions_get(pipeline.name, version)

Get pipeline version

## Description
Get the details of a single pipeline version

### Response Structure
Details of the pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `default`: A boolean indicating whether the version is the default version
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "default": true,
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipeline_versions_get(
  pipeline.name, version
)

# Or provide directly
result <- ubiops::pipeline_versions_get(
  pipeline.name, version,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_versions_list**
> pipeline_versions_list(pipeline.name, labels=NULL)

List pipeline versions

## Description
Pipeline versions can be filtered according to the labels they have by giving labels as a query parameter. Pipeline versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the versions of the pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `default`: A boolean indicating whether the version is the default version
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored

## Response Examples

```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v1",
    "default": true,
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-1",
    "default_notification_group": null,
    "request_retention_time": 604800,
    "request_retention_mode": "full"
  },
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v2",
    "default": false,
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-2",
    "default_notification_group": "notification-group-2",
    "request_retention_time": 86400,
    "request_retention_mode": "metadata"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipeline_versions_list(
  pipeline.name,
  labels = NULL
)

# Or provide directly
result <- ubiops::pipeline_versions_list(
  pipeline.name,
  labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipeline_versions_update**
> pipeline_versions_update(pipeline.name, version, data)

Update pipeline version

## Description
Update a pipeline version. When updating labels, the labels will replace the existing value for labels.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

**Attention:** *In case either the `objects` or `attachments` parameter is null or an empty list, all of the objects or attachments of the pipeline will be removed.*

### Optional Parameters

- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
    - `name`: The name of the object in the pipeline. It must be unique within the pipeline.
    - `reference_type`: The type of object it references. It can be 'deployment', 'pipeline' or 'operator'. It defaults to 'deployment'.
    - `reference_name`: The name of the object it references. The name of the deployment, pipeline or operator.
    - `version`: Optional version for the referenced deployment or pipeline. If not provided, it defaults to the default version of the deployment or pipeline.
    - `configuration`: The configuration specific for the referenced operator, or the 'on_error' policy for the deployment or pipeline.
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1"
}
```

Updating a pipeline version with new objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

Updating a pipeline version by removing objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "objects": null,
  "attachments": null
}
```


A pipeline version referencing a default deployment version and a specific deployment version
```
{
  "objects": [
    {
      "name": "default-version",
      "reference_name": "deployment-1",
      "reference_type": "deployment"
    },
    {
      "name": "specific-version",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ]
}
```

A pipeline version with a sub-pipeline
```
{
  "objects": [
    {
      "name": "object-1",
      "reference_name": "pipeline-1",
      "reference_type": "pipeline",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

A pipeline version with deployment object configuration
```
{
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "configuration": {
        "on_error": "stop"
      }
    }
  ]
}
```

A pipeline version with operators
```
{
  "objects": [
    {
      "name": "operator-if-condition",
      "reference_name": "if-condition",
      "reference_type": "operator",
      "configuration": {
        "expression": "input > 0",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": []
      }
    },
    {
      "name": "operator-variable",
      "reference_name": "pipeline-variable",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [],
        "output_fields": [{"name": "variable", "data_type": "int"}],
        "output_values": [{"name": "variable", "value": 1}]
      }
    },
    {
      "name": "operator-function",
      "reference_name": "function",
      "reference_type": "operator",
      "configuration": {
        "expression": "input * 5",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    },
    {
      "name": "operator-if-condition-2",
      "reference_name": "if-condition",
      "reference_type": "operator",
      "configuration": {
        "expression": "input > 50",
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": []
      }
    },
    {
      "name": "operator-raise-error",
      "reference_name": "raise-error",
      "reference_type": "operator",
      "configuration": {
        "error_message": "My error message!",
        "input_fields": [],
        "output_fields": []
      }
    },
    {
      "name": "operator-one-to-many",
      "reference_name": "one-to-many",
      "reference_type": "operator",
      "configuration": {
        "batch_size": 10,
        "input_fields": [{"name": "output", "data_type": "int"}],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    },
    {
      "name": "operator-many-to-one",
      "reference_name": "many-to-one",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [{"name": "input", "data_type": "int"}],
        "output_fields": [{"name": "input", "data_type": "int"}]
      }
    },
    {
      "name": "operator-count-many",
      "reference_name": "count-many",
      "reference_type": "operator",
      "configuration": {
        "input_fields": [],
        "output_fields": [{"name": "output", "data_type": "int"}]
      }
    }
  ],
  "attachments": [
    {
      "destination_name": "operator-if-condition",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-function",
      "sources": [
        {
          "source_name": "operator-if-condition",
          "mapping": []
        },
        {
          "source_name": "operator-variable",
          "mapping": [
            {
              "source_field_name": "variable",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-one-to-many",
      "sources": [
        {
          "source_name": "operator-function",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "output"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-count-many",
      "sources": [
        {
          "source_name": "operator-one-to-many",
          "mapping": []
        }
      ]
    },
    {
      "destination_name": "operator-many-to-one",
      "sources": [
        {
          "source_name": "operator-one-to-many",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-if-condition-2",
      "sources": [
        {
          "source_name": "operator-many-to-one",
          "mapping": [
            {
              "source_field_name": "input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    },
    {
      "destination_name": "operator-raise-error",
      "sources": [
        {
          "source_name": "operator-if-condition-2",
          "mapping": []
        }
      ]
    },
    {
      "destination_name": "pipeline_end",
      "sources": [
        {
          "source_name": "operator-count-many",
          "mapping": [
            {
              "source_field_name": "output",
              "destination_field_name": "pipeline-output"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response Structure
Details of the created pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `default`: A boolean indicating whether the version is the default version
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "default": true,
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

### Example
```R
data <- list(
  version = "version",  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value"),  # (optional)
  monitoring = "monitoring",  # (optional)
  request_retention_time = 0,  # (optional)
  request_retention_mode = "request_retention_mode",  # (optional)
  default_notification_group = "default_notification_group",  # (optional)
  objects = list(  # (optional)
    list(
      name = "name",
      reference_type = 'deployment',  # (optional)
      reference_name = "reference_name",
      version = "version",  # (optional)
      configuration = list(key = "value")  # (optional)
    )
  ),
  attachments = list(  # (optional)
    list(
      destination_name = "destination_name",
      sources = list(  # (optional)
        list(
          source_name = "source_name",
          mapping = list(  # (optional)
            list(
              source_field_name = source_field_name,
              destination_field_name = destination_field_name
            )
          )
        )
      )
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipeline_versions_update(
  pipeline.name, version, data
)

# Or provide directly
result <- ubiops::pipeline_versions_update(
  pipeline.name, version, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipelines_create**
> pipelines_create(data)

Create pipelines

## Description
Create a pipeline in a project.

The input_fields represent the fields that the input data for pipeline requests should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters

- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the pipeline input. It can be either structured or plain.
- `input_fields`: A list of input fields with name, data_type and (optional) widget. In case of plain pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.
- `output_type`: Type of the pipeline output. It can be either structured or plain.
- `output_fields`: A list of output fields with name, data_type and (optional) widget. In case of plain pipelines, the output_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.

### Optional Parameters

- `description`: Description of the pipeline
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples
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
  ],
  "output_type": "structured",
  "output_fields": [
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
  "output_type": "plain",
  "description": "my description"
}
```

A structured pipeline with input/output field widgets

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {
        "type": "slider",
        "configuration": {"min": 0, "max": 10, "default": 4, "step": 2}
      }
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {
        "type": "numberbox",
        "configuration": {"min": 0, "max": 1, "default": 0.5, "step": 0.1}
      }
    }
  ],
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    },
    {
      "name": "field-2",
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
Details of the created pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description`: Description of the pipeline
- `project`: Project name in which the pipeline is created
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

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
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
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
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```

### Example
```R
data <- list(
  name = "name",
  description = "description",  # (optional)
  input_type = "input_type",
  input_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",
      widget = widget  # (optional)
    )
  ),
  output_type = "output_type",  # (optional)
  output_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",
      widget = widget  # (optional)
    )
  ),
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipelines_create(
  data
)

# Or provide directly
result <- ubiops::pipelines_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipelines_delete**
> pipelines_delete(pipeline.name)

Delete a pipeline

## Description
Delete a pipeline. This will also delete all versions of the pipeline.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::pipelines_delete(
  pipeline.name
)

# Or provide directly
ubiops::pipelines_delete(
  pipeline.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipelines_get**
> pipelines_get(pipeline.name)

Get details of a pipeline

## Description
Get the details of a single pipeline

### Response Structure
Details of the pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description` Description of the pipeline
- `project`: Project name in which the pipeline is defined
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipelines_get(
  pipeline.name
)

# Or provide directly
result <- ubiops::pipelines_get(
  pipeline.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipelines_list**
> pipelines_list(labels=NULL)

List pipelines

## Description
Pipelines can be filtered according to the labels they have by giving labels as a query parameter. Pipelines that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the pipelines in the project

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description of the pipeline
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name and data_type
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

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
    "output_type": "structured",
    "output_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "labels": {
      "tag": "production"
    },
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
    "output_type": "plain",
    "output_fields": [],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipelines_list(
  
  labels = NULL
)

# Or provide directly
result <- ubiops::pipelines_list(
  
  labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **pipelines_update**
> pipelines_update(pipeline.name, data)

Update a pipeline

## Description
Update a pipeline. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `name`: New name for the pipeline
- `description`: New description for the pipeline
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `input_type`: New type for the pipeline input. It is possible to change the type from plain to structured and vice versa.
- `input_fields`: New input fields for the pipeline
- `output_type`: New type for the pipeline output. It is possible to change the type from plain to structured and vice versa.
- `output_fields`: New output fields for the pipeline
- `default_version`: Name of a version of this pipeline which will be assigned as default

If the input type of pipeline is updated to plain, the input fields are deleted. In this case, input_fields should either be omitted or provided as en empty list.
If the input type of pipeline is updated to structured, the old input fields are deleted, if there existed any. The new fields are created, if any is provided. If one or more old fields need to be kept, they must be provided again.
The same goes for updating the pipeline output.

**To delete the input/output fields of a pipeline**, provide an empty list for input_fields/output_fields field.

## Request Examples

```
{
  "name": "new-pipeline-name"
}
```


```
{
  "description": "New pipeline description",
  "labels": {
    "tag": "production"
  }
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
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ]
}
```

```
{
  "input_type": "structured",
  "input_fields": []
}
```

```
{
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
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
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

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
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  description = "description",  # (optional)
  input_type = "input_type",  # (optional)
  input_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",
      widget = widget  # (optional)
    )
  ),
  output_type = "output_type",  # (optional)
  output_fields = list(  # (optional)
    list(
      name = "name",
      data_type = "data_type",
      widget = widget  # (optional)
    )
  ),
  labels = list(key = "value"),  # (optional)
  default_version = "default_version"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::pipelines_update(
  pipeline.name, data
)

# Or provide directly
result <- ubiops::pipelines_update(
  pipeline.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


