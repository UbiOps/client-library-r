# Metrics

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_create**](metrics.md#metrics_create) | **POST** /projects/{project_name}/metrics | Create metrics
[**metrics_delete**](metrics.md#metrics_delete) | **DELETE** /projects/{project_name}/metrics/{metric_name} | Delete metric
[**metrics_get**](metrics.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric_name} | Get metric
[**metrics_list**](metrics.md#metrics_list) | **GET** /projects/{project_name}/metrics | List metrics
[**metrics_update**](metrics.md#metrics_update) | **PATCH** /projects/{project_name}/metrics/{metric_name} | Update metric
[**time_series_data_aggregate**](metrics.md#time_series_data_aggregate) | **POST** /projects/{project_name}/time-series/aggregate | Aggregate metric data
[**time_series_data_create**](metrics.md#time_series_data_create) | **POST** /projects/{project_name}/time-series/data | Create metric data
[**time_series_data_list**](metrics.md#time_series_data_list) | **GET** /projects/{project_name}/time-series/data | List time series data
[**time_series_delete**](metrics.md#time_series_delete) | **DELETE** /projects/{project_name}/time-series/{time_series_id} | Delete time series
[**time_series_search**](metrics.md#time_series_search) | **GET** /projects/{project_name}/time-series/search | Search time series


# **metrics_create**
> metrics_create(data)

Create metrics

## Description
Create a custom metric. The name must start with *custom.*.

### Required Parameters

- `name`: Name of the metric
- `metric_type`: Type of the metric. It can be either 'delta' or 'gauge'.

### Optional Parameters

- `description`: Description of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric. For example, if the metric is defined for a deployment version and can be queried later with the ID of the deployment version, the labels list should contain 'deployment_version_id'.

## Request Examples

```
{
  "name": "custom.metric-1",
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Response Structure
Details of the created metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-1",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example
```R
data <- list(
  name = "name",
  description = "description",  # (optional)
  metric_type = "metric_type",
  unit = "unit",  # (optional)
  labels = list("value-1", "value-2")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::metrics_create(
  data
)

# Or provide directly
result <- ubiops::metrics_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **metrics_delete**
> metrics_delete(metric.name)

Delete metric

## Description
Delete a metric. Only custom metrics can be deleted.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::metrics_delete(
  metric.name
)

# Or provide directly
ubiops::metrics_delete(
  metric.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **metrics_get**
> metrics_get(metric.name)

Get metric

## Description
Retrieve details of a metric

### Response Structure
Details of a metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-1",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::metrics_get(
  metric.name
)

# Or provide directly
result <- ubiops::metrics_get(
  metric.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **metrics_list**
> metrics_list(custom=NULL)

List metrics

## Description
List available metrics in the project

### Optional Parameters

- `custom`: A boolean indicating whether to list default or custom metrics for the project

### Response Structure
A list of details of metrics

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
[
  {
    "id": 1,
    "name": "deployments.requests",
    "description": "Requests to a deployment version",
    "creation_date": "2023-09-01T08:32:14.876451Z",
    "last_updated": "2023-09-01T10:52:23.124784Z",
    "custom": false,
    "metric_type": "delta",
    "unit": "requests",
    "labels": ["deployment_version_id", "user_id"]
  },
  {
    "id": 2,
    "name": "deployments.credits",
    "description": "Credits usage",
    "creation_date": "2023-09-02T10:12:51.195381Z",
    "last_updated": "2023-09-02T10:12:51.195381Z",
    "custom": false,
    "metric_type": "delta",
    "unit": "credits",
    "labels": ["deployment_version_id"]
  },
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::metrics_list(
  
  custom = NULL
)

# Or provide directly
result <- ubiops::metrics_list(
  
  custom = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **metrics_update**
> metrics_update(metric.name, data)

Update metric

## Description
Update a metric. Only custom metrics can be updated.

### Optional Parameters

- `name`: Name of the metric
- `description`: Description of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric. For example, if the metric is defined for a deployment version and can be queried later with the ID of the deployment version, the labels list should contain 'deployment_version_id'.

## Request Examples

```
{
  "name": "custom.metric-2"
}
```

### Response Structure
Details of the updated metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-2",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  description = "description",  # (optional)
  unit = "unit",  # (optional)
  labels = list("value-1", "value-2")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::metrics_update(
  metric.name, data
)

# Or provide directly
result <- ubiops::metrics_update(
  metric.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **time_series_data_aggregate**
> time_series_data_aggregate(data)

Aggregate metric data

## Description
Aggregate metric data for given date, metrics and labels. Only data up to 2 minutes ago is accepted.

### Required Parameters

- `metric`: Name of the metric
- `labels`: Dictionary containing key/value pairs where key indicates the string that can be used to query this metric later and value is the corresponding value of that
- `data`: A list of dictionaries containing 'date' and 'value' fields to indicate the value of the metric for a specific date

## Request Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "056efa9e-67eb-45e3-a49a-0742b3f08aee"
    },
    "data": [
      {
        "date": "2023-09-15T20:12:33.210+00:00",
        "value": 182
      },
      {
        "date": "2023-09-15T21:41:12.532+00:00",
        "value": 1
      }
    ]
  }
]
```

### Example
```R
data <- list(
  metric = "metric",
  labels = list(key = "value"),  # (optional)
  data = list(  # (optional)
    list(
      date = date,
      value = 0
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::time_series_data_aggregate(
  data
)

# Or provide directly
result <- ubiops::time_series_data_aggregate(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **time_series_data_create**
> time_series_data_create(data)

Create metric data

## Description
Insert data points for a metric. Multiple metrics for different types is supported.

### Required Parameters

- `metric`: Name of the metric
- `labels`: Dictionary containing key/value pairs where key indicates the string that can be used to query this metric later and value is the corresponding value of that
- `data`: A list of dictionaries containing 'date' and 'value' fields to indicate the value of the metric for a specific date

## Request Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "056efa9e-67eb-45e3-a49a-0742b3f08aee"
    },
    "data": [
      {
        "date": "2023-09-15T20:00:00.000+00:00",
        "value": 182
      },
      {
        "date": "2023-09-15T21:00:00.000+00:00",
        "value": 1
      }
    ]
  }
]
```

### Example
```R
data <- list(
  metric = "metric",
  labels = list(key = "value"),  # (optional)
  data = list(  # (optional)
    list(
      date = date,
      value = 0
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::time_series_data_create(
  data
)

# Or provide directly
result <- ubiops::time_series_data_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **time_series_data_list**
> time_series_data_list(metric=NULL, start.date=NULL, end.date=NULL, aggregation.period=NULL, labels=NULL)

List time series data

## Description
List data points for a metric

Available metrics for deployments:
- `deployments.requests`: Number of requests to a deployment version
- `deployments.failed_requests`: Number of failed requests to a deployment version
- `deployments.request_duration`: Average time in seconds for a deployment request to complete
- `deployments.input_volume`: Volume of incoming data in bytes
- `deployments.output_volume`: Volume of outgoing data in bytes
- `deployments.network_in`: Volume of inbound data traffic in bytes
- `deployments.network_out`: Volume of outbound data traffic in bytes
- `deployments.express_queue_size`: Average number of queued express requests
- `deployments.batch_queue_size`: Average number of queued batch requests
- `deployments.express_queue_time`: Average time in seconds for an express request to start processing
- `deployments.batch_queue_time`: Average time in seconds for a batch request to start processing
- `deployments.memory_utilization`: Average memory used during a request
- `deployments.instances`: Number of active deployment instances
- `deployments.credits`: Usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours the deployments are running

Available metrics for pipelines:
- `pipelines.requests`: Number of requests to a pipeline version
- `pipelines.failed_requests`: Number of failed requests to a pipeline version
- `pipelines.request_duration`: Average time in seconds for a pipeline request to complete
- `pipelines.input_volume`: Volume of incoming data in bytes
- `pipelines.output_volume`: Volume of outgoing data in bytes
- `pipelines.object_requests`: Number of object requests in a pipeline version
- `pipelines.object_failed_requests`: Number of failed object requests in a pipeline version

### Required Parameters

- `metric`: Name of the metric
- `start_date`: Start date for metric data points
- `end_date`: End date for metric data points

### Optional Parameters

- `aggregation_period`: Time period in seconds in which data points are grouped. It defaults to the highest resolution possible given the provided date range.
- `labels`: Comma-separated values for labels to filter on data points. It must be in the format: key-1:value-1,key-2:value-2.

### Response Structure

- `metric`: Name of the metric
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `start_date`: Start date for metric data points
- `end_date`: End date for metric data points
- `aggregation_period`: Time period in seconds in which data points are grouped
- `labels`: Labels to filter on data points
- `data`: A list of dictionaries containing the data points

## Response Examples

```
{
  "metric": "deployments.requests",
  "metric_type": "delta",
  "unit": "requests/s",
  "start_date": "2023-01-01T10:00:00Z",
  "end_date": 2023-01-01T12:00:00Z",
  "aggregation_period": 3600,
  "labels": {
    "deployment_version_id": "8935a589-8686-4ce7-8c9e-8b5e529c6b47"
  },
  "data": [
    {
      "start_date": "2023-01-01T10:00:00Z",
      "end_date": 2023-01-01T11:00:00Z",
      "value": 3
    },
    {
      "start_date": "2023-01-01T11:00:00Z",
      "end_date": 2023-01-01T12:00:00Z",
      "value": 10
    }
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::time_series_data_list(
  
  metric = NULL, start.date = NULL, end.date = NULL, aggregation.period = NULL, labels = NULL
)

# Or provide directly
result <- ubiops::time_series_data_list(
  
  metric = NULL, start.date = NULL, end.date = NULL, aggregation.period = NULL, labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **time_series_delete**
> time_series_delete(time.series.id)

Delete time series

## Description
Delete a time series

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::time_series_delete(
  time.series.id
)

# Or provide directly
ubiops::time_series_delete(
  time.series.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **time_series_search**
> time_series_search(metric=NULL, labels=NULL, custom=NULL, exact.match=NULL, limit=NULL, offset=NULL)

Search time series

## Description
Search through time series

### Optional Parameters

- `metric`: Name of the metric
- `labels`: Comma-separated values for labels to filter on data points. It must be in the format: key-1:value-1,key-2:value-2.
- `custom`: A boolean indicating whether only default or custom metrics should be returned. If this parameter is not provided, both types are returned.
- `exact_match`: A boolean indicating whether the provided labels should match exactly or whether matching a subset is allowed. Defaults to false (matching a subset is allowed).
- `limit`: The maximum number of time series to return. It defaults to 500.
- `offset`: The number that indicates the starting point of the time series to return. It defaults to 0.

### Response Structure
A list of time series

- `metric`: Name of the metric
- `labels`: Labels that the time series has
- `resolution`: Metric resolution in seconds

## Response Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "8935a589-8686-4ce7-8c9e-8b5e529c6b47",
      "user_id": "5bb50513-2b4e-466a-ab88-e5be70d63f75"
    },
    "resolution": 60
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::time_series_search(
  
  metric = NULL, labels = NULL, custom = NULL, exact.match = NULL, limit = NULL, offset = NULL
)

# Or provide directly
result <- ubiops::time_series_search(
  
  metric = NULL, labels = NULL, custom = NULL, exact.match = NULL, limit = NULL, offset = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


