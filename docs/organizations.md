# Organizations

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_usage_details_get**](organizations.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
[**organization_usage_get**](organizations.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
[**organization_users_create**](organizations.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](organizations.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](organizations.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](organizations.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](organizations.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](organizations.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](organizations.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](organizations.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](organizations.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
[**organizations_update**](organizations.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization


# **organization_usage_details_get**
> organization_usage_details_get(organization.name, month=NULL)

Get resource usage details

## Description
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per day.

### Optional Parameters

- `month`: date indicating the month to fetch usage data for, formatted `YYYY-MM`. If omitted defaults to the current month

### Response Structure

- `metric`: The metric that was measured
- `object_type`: Type of object the metric was measured for (version or pipeline)
- `usage`: an array of objects each containing the following:
     - `day`: Timestamp denoting the start of the day
     - `value`: Aggregated metric value for the given unit over the given day

## Response Examples

```
[
  {
    "object_type": "version",
    "metric": "gb_seconds",
    "usage": [
      {
        "day": "2020-07-29T00:00:00Z",
        "value": 4200
      },
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 840
      },
      {
        "day": "2020-07-30T00:00:00Z",
        "value": 960
      }
    ]
  },
  {
    "object_type": "pipeline",
    "metric": "input_volume",
    "usage": [
      {
        "day": "2020-07-28T00:00:00Z",
        "value": 1098
      },
      {
        "day": "2020-07-06T00:00:00Z",
        "value": 18
      },
      {
        "day": "2020-07-16T00:00:00Z",
        "value": 9
      },
      {
        "day": "2020-07-15T00:00:00Z",
        "value": 117
      },
      {
        "day": "2020-07-08T00:00:00Z",
        "value": 90
      }
    ]
  }
]

```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_usage_details_get(
  organization.name,
  month = NULL
)

# Or provide directly
result <- ubiops::organization_usage_details_get(
  organization.name,
  month = NULL, 
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_usage_get**
> organization_usage_get(organization.name, start.month=NULL)

Get resource usage

## Description
Get resource usage for the organization. This returns a list of metrics that are used for billing, aggregated per month.

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
    "object_type": "pipeline",
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
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_usage_get(
  organization.name,
  start.month = NULL
)

# Or provide directly
result <- ubiops::organization_usage_get(
  organization.name,
  start.month = NULL, 
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_users_create**
> organization_users_create(organization.name, data)

Add a user to an organization

## Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters

- `email`: Email of the user

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```

### Example
```R
data <- list(
  email = "email",
  admin = FALSE  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_users_create(
  organization.name, data
)

# Or provide directly
result <- ubiops::organization_users_create(
  organization.name, data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_users_delete**
> organization_users_delete(organization.name, user.id)

Delete a user from an organization

## Description
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::organization_users_delete(
  organization.name, user.id
)

# Or provide directly
ubiops::organization_users_delete(
  organization.name, user.id,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_users_get**
> organization_users_get(organization.name, user.id)

Get details of a user in an organization

## Description
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_users_get(
  organization.name, user.id
)

# Or provide directly
result <- ubiops::organization_users_get(
  organization.name, user.id,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_users_list**
> organization_users_list(organization.name)

List the users in an organization

## Description
List users and their details in an organization

### Response Structure
List of details of users

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_users_list(
  organization.name
)

# Or provide directly
result <- ubiops::organization_users_list(
  organization.name,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organization_users_update**
> organization_users_update(organization.name, user.id, data)

Update details of a user in an organization

## Description
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "admin": true
}
```

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
}
```

### Example
```R
data <- list(
  admin = FALSE  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organization_users_update(
  organization.name, user.id, data
)

# Or provide directly
result <- ubiops::organization_users_update(
  organization.name, user.id, data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organizations_create**
> organizations_create(data)

Create organizations

## Description
Create a new organization. When a user creates an organization, s/he will automatically become an organization admin.

### Required Parameters

- `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `subscription`: Name of the subscription for the organization
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted

### Optional Parameters

- `subscription_end_date`: End date of the subscription. The subscription will be cancelled on this date. A 'free' subscription cannot have a custom end_date as this subscription is always valid for a year. **Provide a null value for this field to have no end date.**

## Request Examples

```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true
}
```


```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true,
  "subscription_end_date": "2021-03-25"
}
```

### Response Structure
Details of the created organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
}
```

### Example
```R
data <- list(
  name = "name",
  subscription = "subscription",
  subscription_agreed = FALSE,
  subscription_end_date = subscription_end_date  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_create(
  data
)

# Or provide directly
result <- ubiops::organizations_create(
  data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organizations_get**
> organizations_get(organization.name)

Get details of an organization

## Description
Get the details of an organization

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Dictionary with details of the active subscription

- `subscription_self_service`: Boolean indicating if the organization subscription is self service

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "name": "custom-subscription",
    "max_projects": 2,
    "max_users": 3,
    "agreement": "",
    "terms_conditions": "",
    "gb_seconds": 10000,
    "deployment_versions": 15
  },
  "subscription_self_service": true
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_get(
  organization.name
)

# Or provide directly
result <- ubiops::organizations_get(
  organization.name,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organizations_list**
> organizations_list()

List organizations

## Description
List all organizations where the user making the request is a member

### Response Structure
A list of details of the organizations

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_list()

# Or provide directly
result <- ubiops::organizations_list(
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organizations_resource_usage**
> organizations_resource_usage(organization.name)

List resource usage of an organization

## Description
List the total number of resources used by this organization

### Response Structure
A list containing the number of

- projects

- users

- deployments

- deployment_versions

- pipelines

- pipeline_versions

currently used by the organization.

## Response Examples

```
{
  "projects": 5,
  "users": 3,
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_resource_usage(
  organization.name
)

# Or provide directly
result <- ubiops::organizations_resource_usage(
  organization.name,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **organizations_update**
> organizations_update(organization.name, data)

Update details of an organization

## Description
Update an organization. The user making the request must be admin of the organization. Users are able to update the name of the organization, but changes to the subscription can only be done by Dutch Analytics.
To delete the end date of the current subscription, give the 'subscription_end_date' parameter with value null.

### Optional Parameters

- `name`: New organization name
- `subscription`: New subscription
- `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted upon upgrading the subscription
- `subscription_end_date`: End date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will be cancelled on this date. If the subscription_end_date was previously set, but should be removed, give a null value for this field.

## Request Examples



```
{
  "name": "new-organization-name"
}
```

```
{
  "subscription": "professional",
  "subscription_agreed": true
}
```

```
{
  "subscription_end_date": "2020-08-30",
  "subscription_agreed": true
}
```

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Name of the subscription

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  subscription = "subscription",  # (optional)
  subscription_agreed = FALSE,  # (optional)
  subscription_end_date = subscription_end_date  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_update(
  organization.name, data
)

# Or provide directly
result <- ubiops::organizations_update(
  organization.name, data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

