# Monitoring

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_groups_create**](monitoring.md#notification_groups_create) | **POST** /projects/{project_name}/monitoring/notification-groups | Create notification groups
[**notification_groups_delete**](monitoring.md#notification_groups_delete) | **DELETE** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Delete notification group
[**notification_groups_get**](monitoring.md#notification_groups_get) | **GET** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Get notification group
[**notification_groups_list**](monitoring.md#notification_groups_list) | **GET** /projects/{project_name}/monitoring/notification-groups | List notification groups
[**notification_groups_update**](monitoring.md#notification_groups_update) | **PATCH** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Update notification group


# **notification_groups_create**
> notification_groups_create(data)

Create notification groups

## Description
Create a notification group by defining a name and a list of contacts

### Required Parameters

- `name`: Name of the notification group. It is unique within a project.

### Optional Parameters

- `contacts`: A list of dictionaries containing the following keys:
    - `type`: Type of the contact. It can be `email`.
    - `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Response Structure
Details of the created notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Example
```R
data <- list(
  name = "name",
  contacts = list(  # (optional)
    list(
      type = "type",
      configuration = list(key = "value")
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::notification_groups_create(
  data
)

# Or provide directly
result <- ubiops::notification_groups_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **notification_groups_delete**
> notification_groups_delete(notification.group.name)

Delete notification group

## Description
Delete a notification group

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::notification_groups_delete(
  notification.group.name
)

# Or provide directly
ubiops::notification_groups_delete(
  notification.group.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **notification_groups_get**
> notification_groups_get(notification.group.name)

Get notification group

## Description
Retrieve details of a single notification group in a project

### Response Structure
Details of a notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::notification_groups_get(
  notification.group.name
)

# Or provide directly
result <- ubiops::notification_groups_get(
  notification.group.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **notification_groups_list**
> notification_groups_list()

List notification groups

## Description
List the notification groups in a project

### Response Structure
A list of details of the notification groups in the project

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
[
  {
    "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
    "name": "notification-group-1",
    "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user@ubiops.com"
        }
      },
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.2@ubiops.com"
        }
      }
    ],
  },
  {
    "id": "7193ca09-d28b-4fce-a15a-11e0bc9f7f6f",
    "name": "notification-group-2",
     "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.3@ubiops.com"
        }
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
result <- ubiops::notification_groups_list(
  
)

# Or provide directly
result <- ubiops::notification_groups_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **notification_groups_update**
> notification_groups_update(notification.group.name, data)

Update notification group

## Description
Update a notification group

### Optional Parameters

- `name`: New name for the deployment
- `contacts`: A list of dictionaries containing the following keys:
    - `type`: Type of the contact. It can be `email`.
    - `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "new-notification-group-name"
}
```

### Response Structure
Details of the updated notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "new-notification-group-name",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  contacts = list(  # (optional)
    list(
      type = "type",
      configuration = list(key = "value")
    )
  )
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::notification_groups_update(
  notification.group.name, data
)

# Or provide directly
result <- ubiops::notification_groups_update(
  notification.group.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


