# Roles

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_list**](roles.md#permissions_list) | **GET** /permissions | List the available permissions
[**role_assignments_create**](roles.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
[**role_assignments_delete**](roles.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
[**role_assignments_get**](roles.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
[**role_assignments_per_user_list**](roles.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
[**roles_create**](roles.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](roles.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](roles.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](roles.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](roles.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project


# **permissions_list**
> permissions_list()

List the available permissions

## Description
List all the available permissions which can be used to create custom roles.

### Response Structure
A list of available permissions

- `name`: Name of the permission

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::permissions_list()

# Or provide directly
result <- ubiops::permissions_list(
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **role_assignments_create**
> role_assignments_create(data)

Assign a role to a user in a project

## Description
Assign a role to a user in the scope of a project. This role can be assigned on either project level or on object level, which can be a deployment or pipeline.
The user making the request must have appropriate permissions.

### Required Parameters

- `user_id`: Unique identifier for the user (UUID)

- `role`: Name of the role to be assigned to the user

### Optional Parameters

- `object_name`: Name of the object for which the role will be assigned

- `object_type`: Type of the object for which the role will be assigned. It can be project, deployment or pipeline.

**object_name and object_type must be provided together. If neither of them is provided, the role is set on project level.**

## Request Examples
Setting the role deployment-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-admin"
}
```

Setting the role deployment-viewer on deployment-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```

### Response Structure
Details of the created role assignment

- `id`: Unique identifier for the role assignment (UUID)

- `user_id`: Unique identifier for the user (UUID)

- `role`: Name of the role assigned to the user

- `object_name`: Name of the object for which the role is assigned

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-admin",
  "object_name": "project-1",
  "object_type": "project"
}
```


```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```

### Example
```R
data <- list(
  user_id = "user_id",
  role = "role",
  object_name = "object_name",  # (optional)
  object_type = "object_type"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::role_assignments_create(
  data
)

# Or provide directly
result <- ubiops::role_assignments_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **role_assignments_delete**
> role_assignments_delete(id)

Delete a role from a user with the given role assignment id

## Description
Delete a role of a user. The user making the request must have appropriate permissions. It is possible for a user to delete their own role if they have permissions to do so.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::role_assignments_delete(
  id
)

# Or provide directly
ubiops::role_assignments_delete(
  id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **role_assignments_get**
> role_assignments_get(id)

Get details of a role assignment

## Description
Get the details of a role assignment of a user. The user making the request must have appropriate permissions.

### Response Structure
Details of the role assignment

- `id`: Unique identifier for the role assignment (UUID)

- `user_id`: Unique identifier for the user (UUID)

- `role`: Name of the role assigned to the user

- `object_name`: Name of the object for which the role is assigned

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "deployment-viewer",
  "object_name": "deployment-1",
  "object_type": "deployment"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::role_assignments_get(
  id
)

# Or provide directly
result <- ubiops::role_assignments_get(
  id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **role_assignments_per_user_list**
> role_assignments_per_user_list(user.id)

List the roles assigned to a specific user in a project

## Description
List the roles assigned to a user in the scope of a project.

### Response Structure

- `id`: Unique identifier for the role assignment (UUID)

- `user_id`: Unique identifier for the user (UUID)

- `role`: Name of the role assigned to the user

- `object_name`: Name of the object for which the role is assigned

- `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.

## Response Examples

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "deployment-viewer",
    "object_name": "deployment-1",
    "object_type": "deployment"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "pipeline-admin",
    "object_name": "pipeline-1",
    "object_type": "pipeline"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::role_assignments_per_user_list(
  user.id
)

# Or provide directly
result <- ubiops::role_assignments_per_user_list(
  user.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **roles_create**
> roles_create(data)

Create a custom role scoped in a project

## Description
Create a custom role in the scope of a project. This role is not accessible from other projects.
The user making the request must have appropriate permissions.

### Required Parameters

- `name`: Name of the role which will be created. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `permissions`: A list of permissions which the role will contain. The list of available permissions can be obtained with */permissions* endpoint.

## Request Examples

```
{
  "name": "custom-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

### Response Structure
Details of the created role

- `id`: Unique identifier for the created role (UUID)

- `name`: Name of the created role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

### Example
```R
data <- list(
  name = "name",
  permissions = list("value-1", "value-2")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::roles_create(
  data
)

# Or provide directly
result <- ubiops::roles_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **roles_delete**
> roles_delete(role.name)

Delete a role from a project

## Description
Delete a role from a project. The user making the request must have appropriate permissions.
**Default roles cannot be deleted.**

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::roles_delete(
  role.name
)

# Or provide directly
ubiops::roles_delete(
  role.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **roles_get**
> roles_get(role.name)

Get details of a role

## Description
Get the details of a role. The user making the request must have appropriate permissions.

### Response Structure
Details of the role

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::roles_get(
  role.name
)

# Or provide directly
result <- ubiops::roles_get(
  role.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **roles_list**
> roles_list()

List the available roles in a project

## Description
List the roles available in the scope of a project. Information on which permissions each role contains, can be obtained with a call to get details of a single role.

### Response Structure

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the role

- `default`: A boolean value that indicates whether the role is a default role or not

## Response Examples

```
[
  {
    "id": "34e53855-9b50-47bc-b516-6cb971b1949c",
    "name": "project-admin",
    "default": true
  },
  {
    "id": "00132911-b5dd-4017-b399-85f3ffd2a7c3",
    "name": "project-editor",
    "default": true
  },
  {
    "id": "bf0d5823-8062-40f6-bbd2-21bc732f3c3b",
    "name": "project-viewer",
    "default": true
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::roles_list(
  
)

# Or provide directly
result <- ubiops::roles_list(
  
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **roles_update**
> roles_update(role.name, data)

Update a role in a project

## Description
Update a role in a project. The user making the request must have appropriate permissions.
**Default roles cannot be updated.**

### Optional Parameters

- `name`: New name for the role. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `permissions`: A new list of permissions which the role will contain. The previous permissions will be replaced with the given ones. The list of available permissions can be obtained with */permissions* endpoint.

## Request Examples

```
{
  "name": "new-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```

### Response Structure
Details of the updated role

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the updated role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "new-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```

### Example
```R
data <- list(
  name = "name",  # (optional)
  permissions = list("value-1", "value-2")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::roles_update(
  role.name, data
)

# Or provide directly
result <- ubiops::roles_update(
  role.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


