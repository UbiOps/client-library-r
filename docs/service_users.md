# ServiceUsers

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_users_create**](service_users.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](service_users.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](service_users.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](service_users.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](service_users.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](service_users.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details


# **service_users_create**
> service_users_create(data)

Create a new service user

## Description
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. It is possible to set an expiry date for this token.
In addition, allowed cors origins can be configured for the service user. The service user will be allowed to make a deployment or pipeline request from these origins.

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters

- `name`: Name of the service user

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account expires (UTC). If null is passed, the account will never expire.

## Request Examples

```
{
  "name": "service-user-1"
}
```


```
{
  "name": "service-user-1",
  "allowed_cors_origins": [
    "https://test.com"
  ]
}
```


```
{
  "name": "service-user-1",
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the created service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `token`: The API token for the created service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": "2021-03-24T00:00:00.000+00:00"
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  allowed_cors_origins = list("value-1", "value-2")  # (optional),
  expiry_date = expiry_date  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_create(
  data
)

# Or provide directly
result <- ubiops::service_users_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **service_users_delete**
> service_users_delete(service.user.id)

Delete service user

## Description
Delete a service user from a project

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::service_users_delete(
  service.user.id
)

# Or provide directly
ubiops::service_users_delete(
  service.user.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **service_users_get**
> service_users_get(service.user.id)

Retrieve details of a service user

## Description
Retrieve details of a service user

### Response Structure
Details of the service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": null
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_get(
  service.user.id
)

# Or provide directly
result <- ubiops::service_users_get(
  service.user.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **service_users_list**
> service_users_list()

List service users

## Description
List service users defined in a project

### Response Structure
List of details of the service users:

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00",
    "allowed_cors_origins": [
      "https://test.com"
    ],
    "expiry_date": "2021-03-24T00:00:00.000+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00",
    "allowed_cors_origins": [
      "https://test.com"
    ],
    "expiry_date": null
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_list(
  
)

# Or provide directly
result <- ubiops::service_users_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **service_users_token**
> service_users_token(service.user.id, data=NULL)

Reset the token of a service user

## Description
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

It is not possible to reset the token of a service user whose expiry date has been reached.

### Response Structure
Details of the new token for the service user

- `token`: The new API token for the service user

## Response Examples

```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_token(
  service.user.id,
  data = NULL
)

# Or provide directly
result <- ubiops::service_users_token(
  service.user.id,
  data = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **service_users_update**
> service_users_update(service.user.id, data)

Update service user details

## Description
Update the name, expiry date and cors allowed origins of a service user. The new value for the cors_allowed_origin will replace the old value.
Leave as an empty list to remove the previous list of allowed origins.

It is not possible to update a service user whose expiry date has been reached.

### Optional Parameters

- `name`: Name of the service user

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC). If null is passed, the account will never expire.

## Request Examples


```
{
  "name": "new-service-user-name",
}
```


```
{
  "name": "service-user-1",
  "allowed_cors_origins": [
    "https://test.com"
  ]
}
```


```
{
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the updated service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": null
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  allowed_cors_origins = list("value-1", "value-2")  # (optional),
  expiry_date = expiry_date  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_update(
  service.user.id, data
)

# Or provide directly
result <- ubiops::service_users_update(
  service.user.id, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


