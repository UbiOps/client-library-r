# Roles

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissions_list**](roles.md#permissions_list) | **GET** /permissions | List the available permissions
[**role_assignments_create**](roles.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign role to user/object
[**role_assignments_delete**](roles.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete role of user
[**role_assignments_get**](roles.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get role assignment
[**role_assignments_per_object_list**](roles.md#role_assignments_per_object_list) | **GET** /projects/{project_name}/role-assignments | List roles on object/user
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

Assign role to user/object

## Description
Assign a role to a user or an object in the scope of a project. This role can be assigned on either project level or on object level, which can be a deployment, pipeline or bucket.

### Required Parameters

- `user_id`: Unique identifier for the user (UUID)
- `role`: Name of the role to be assigned to the user
- `assignee`: UUID of the user or the name of the object for which the role will be assigned
- `assignee_type`: Type of the assignee. It can be user or deployment.
- `resource`: Name of the object for which the role will be assigned
- `resource_type`: Type of the object for which the role will be assigned. It can be project, deployment, pipeline or bucket.

**resource and resource_type must be provided together. If neither of them is provided, the role is set on project level.**

## Request Examples
Setting the role deployment-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin"
}
```

Setting the role deployment-viewer on deployment-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-viewer",
  "resource": "deployment-1",
  "resource_type": "deployment"
}
```

Setting the role files-reader on bucket-1 for deployment-1

```
{
  "assignee": "deployment-1",
  "assignee_type": "deployment",
  "role": "file-reader",
  "resource": "bucket-1",
  "resource_type": "bucket"
}
```

### Response Structure
Details of the created role assignment

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin",
  "resource": "project-1",
  "resource_type": "project"
}
```


```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "deployment-1",
  "assignee_type": "deployment",
  "role": "file-reader",
  "resource": "bucket-1",
  "resource_type": "bucket"
}
```

### Example
```R
data <- list(
  role = "role",
  assignee = "assignee",  # (optional)
  assignee_type = "assignee_type",  # (optional)
  resource = "resource",  # (optional)
  resource_type = "resource_type"  # (optional)
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

Delete role of user

## Description
Delete a role of a user.  It is possible for a user to delete their own role if they have permissions to do so.

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

Get role assignment

## Description
Get the details of a role assignment of a user/deployment.

### Response Structure
Details of the role assignment

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user/object
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin",
  "resource": "project-1",
  "resource_type": "project"
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

# **role_assignments_per_object_list**
> role_assignments_per_object_list(resource=NULL, resource.type=NULL, assignee=NULL, assignee.type=NULL)

List roles on object/user

## Description
List the roles assigned to a user or on an object in the scope of a project.

### Optional Parameters
These parameters should be given as query parameters

- `resource`: Name of the object on which the assigned roles will be listed
- `resource_type`: Type of the object on which the assigned roles will be listed
- `assignee`: UUID of the user or the name of the object for which the assigned roles will be listed
- `assignee_type`: Type of the assignee for which the assigned roles will be listed

### Response Structure

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user/object
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples
Roles assigned to user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "assignee_type": "user",
    "role": "deployment-admin",
    "resource": "project-1",
    "resource_type": "project"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "assignee_type": "user",
    "role": "pipeline-admin",
    "resource": "pipeline-1",
    "resource_type": "pipeline"
  }
]
```

Roles assigned on deployment with name deployment-1

```
[
  {
    "id": "a24aabc2-c7df-4f7b-b177-f80827aea1bb",
    "assignee": "258771bb-1bc4-4f2f-a3f4-9309cc64d1dd",
    "assignee_type": "user",
    "role": "deployment-admin",
    "resource": "deployment-1",
    "resource_type": "deployment"
  },
  {
    "id": "dfd4e714-9c2d-446e-ae96-4db18f91d3de",
    "assignee": "0ca8a61d-962e-48e3-b558-61e8ca2dae88",
    "assignee_type": "user",
    "role": "deployment-viewer",
    "resource": "deployment-1",
    "resource_type": "deployment"
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::role_assignments_per_object_list(
  
  resource = NULL, resource.type = NULL, assignee = NULL, assignee.type = NULL
)

# Or provide directly
result <- ubiops::role_assignments_per_object_list(
  
  resource = NULL, resource.type = NULL, assignee = NULL, assignee.type = NULL, 
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


