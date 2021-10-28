# ubiops

[www.ubiops.com](https://ubiops.com)

Client Library to interact with the UbiOps API.

This R package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.1
- Package version: 0.3.0

For more information, please visit [https://ubiops.com/docs](https://ubiops.com/docs)

## Installation

### DevTools

To install directly from Github, use `devtools`:
```R
install.packages("devtools")
library(devtools)
install_github("UbiOps/client-library-r")
```

### Local build

To build and install locally:

1. Install the dependencies from CRAN

```R
install.packages("caTools")
install.packages("httr")
install.packages("jsonlite")
install.packages("R6")
install.packages("readr")
install.packages("rjson")
install.packages("stringr")
```

2. Build the package

```sh
git clone https://github.com/UbiOps/client-library-r
cd client-library-r
R CMD build .
R CMD INSTALL ubiops_0.3.0.tar.gz
```

### Troubleshooting

Getting errors while installing `devtools`? You may need to install some OS level packages.
On Ubuntu, you can try with `build-essential`, `libcurl4-gnutls-dev`, `libxml2-dev` and `libssl-dev`.

Getting errors about `LC_../LANG` variables missing? You may need to export the following variables:
`LC_CTYPE=en_US.UTF-8` and `LC_MESSAGES=en_US.UTF-8`.

## Usage

```R
library(ubiops)

# 1) Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- deployments_list()

# 2) Or provide directly
# result <- deployments_list(UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN")

print(result)
# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

## Documentation for API Endpoints

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_create**](docs/blobs.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](docs/blobs.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](docs/blobs.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](docs/blobs.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**blobs_update**](docs/blobs.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob
[**batch_deployment_requests_create**](docs/deployment_requests.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
[**batch_deployment_version_requests_create**](docs/deployment_requests.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
[**deployment_requests_batch_delete**](docs/deployment_requests.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
[**deployment_requests_batch_get**](docs/deployment_requests.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
[**deployment_requests_create**](docs/deployment_requests.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
[**deployment_requests_delete**](docs/deployment_requests.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
[**deployment_requests_get**](docs/deployment_requests.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
[**deployment_requests_list**](docs/deployment_requests.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
[**deployment_requests_update**](docs/deployment_requests.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
[**deployment_version_requests_batch_delete**](docs/deployment_requests.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
[**deployment_version_requests_batch_get**](docs/deployment_requests.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
[**deployment_version_requests_create**](docs/deployment_requests.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
[**deployment_version_requests_delete**](docs/deployment_requests.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
[**deployment_version_requests_get**](docs/deployment_requests.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
[**deployment_version_requests_list**](docs/deployment_requests.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
[**deployment_version_requests_update**](docs/deployment_requests.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request
[**builds_get**](docs/deployments.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
[**builds_list**](docs/deployments.md#builds_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds | List builds
[**deployment_audit_events_list**](docs/deployments.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
[**deployment_environment_variables_copy**](docs/deployments.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
[**deployment_environment_variables_create**](docs/deployments.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
[**deployment_environment_variables_delete**](docs/deployments.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
[**deployment_environment_variables_get**](docs/deployments.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
[**deployment_environment_variables_list**](docs/deployments.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
[**deployment_environment_variables_update**](docs/deployments.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
[**deployment_version_environment_variables_copy**](docs/deployments.md#deployment_version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy deployment version environment variable
[**deployment_version_environment_variables_create**](docs/deployments.md#deployment_version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create deployment version environment variable
[**deployment_version_environment_variables_delete**](docs/deployments.md#deployment_version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete deployment version environment variable
[**deployment_version_environment_variables_get**](docs/deployments.md#deployment_version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get deployment version environment variable
[**deployment_version_environment_variables_list**](docs/deployments.md#deployment_version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List deployment version environment variables
[**deployment_version_environment_variables_update**](docs/deployments.md#deployment_version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update deployment version environment variable
[**deployment_versions_create**](docs/deployments.md#deployment_versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create deployment versions
[**deployment_versions_delete**](docs/deployments.md#deployment_versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete deployment version
[**deployment_versions_get**](docs/deployments.md#deployment_versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get deployment version
[**deployment_versions_list**](docs/deployments.md#deployment_versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List deployment versions
[**deployment_versions_update**](docs/deployments.md#deployment_versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update deployment version
[**deployments_create**](docs/deployments.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create deployments
[**deployments_delete**](docs/deployments.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
[**deployments_get**](docs/deployments.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of a deployment
[**deployments_list**](docs/deployments.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments
[**deployments_update**](docs/deployments.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
[**revisions_file_download**](docs/deployments.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
[**revisions_file_upload**](docs/deployments.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
[**revisions_get**](docs/deployments.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
[**revisions_list**](docs/deployments.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions
[**exports_create**](docs/imports_and_exports.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
[**exports_delete**](docs/imports_and_exports.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
[**exports_download**](docs/imports_and_exports.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
[**exports_get**](docs/imports_and_exports.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
[**exports_list**](docs/imports_and_exports.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
[**imports_create**](docs/imports_and_exports.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
[**imports_delete**](docs/imports_and_exports.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
[**imports_download**](docs/imports_and_exports.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
[**imports_get**](docs/imports_and_exports.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
[**imports_list**](docs/imports_and_exports.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
[**imports_update**](docs/imports_and_exports.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import
[**organization_usage_details_get**](docs/organizations.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
[**organization_usage_get**](docs/organizations.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
[**organization_users_create**](docs/organizations.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](docs/organizations.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](docs/organizations.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](docs/organizations.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](docs/organizations.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](docs/organizations.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](docs/organizations.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](docs/organizations.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](docs/organizations.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
[**organizations_update**](docs/organizations.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**batch_pipeline_requests_create**](docs/pipeline_requests.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
[**batch_pipeline_version_requests_create**](docs/pipeline_requests.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
[**pipeline_requests_batch_delete**](docs/pipeline_requests.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
[**pipeline_requests_batch_get**](docs/pipeline_requests.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
[**pipeline_requests_create**](docs/pipeline_requests.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
[**pipeline_requests_delete**](docs/pipeline_requests.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
[**pipeline_requests_get**](docs/pipeline_requests.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
[**pipeline_requests_list**](docs/pipeline_requests.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
[**pipeline_version_requests_batch_delete**](docs/pipeline_requests.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
[**pipeline_version_requests_batch_get**](docs/pipeline_requests.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
[**pipeline_version_requests_create**](docs/pipeline_requests.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
[**pipeline_version_requests_delete**](docs/pipeline_requests.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
[**pipeline_version_requests_get**](docs/pipeline_requests.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
[**pipeline_version_requests_list**](docs/pipeline_requests.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests
[**pipeline_audit_events_list**](docs/pipelines.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_version_object_attachments_create**](docs/pipelines.md#pipeline_version_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/attachments | Create object attachments
[**pipeline_version_object_attachments_delete**](docs/pipelines.md#pipeline_version_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/attachments/{attachment_id} | Delete object attachment
[**pipeline_version_object_attachments_destination_get**](docs/pipelines.md#pipeline_version_object_attachments_destination_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{destination_name}/attachments | List the attachments of a destination object
[**pipeline_version_object_attachments_get**](docs/pipelines.md#pipeline_version_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/attachments/{attachment_id} | Get object attachment
[**pipeline_version_object_attachments_list**](docs/pipelines.md#pipeline_version_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/attachments | List object attachments
[**pipeline_version_object_environment_variables_list**](docs/pipelines.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_version_objects_create**](docs/pipelines.md#pipeline_version_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects | Create pipeline object
[**pipeline_version_objects_delete**](docs/pipelines.md#pipeline_version_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name} | Delete pipeline object
[**pipeline_version_objects_get**](docs/pipelines.md#pipeline_version_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name} | Get pipeline object
[**pipeline_version_objects_list**](docs/pipelines.md#pipeline_version_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects | List pipeline objects
[**pipeline_version_objects_update**](docs/pipelines.md#pipeline_version_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name} | Update pipeline object
[**pipeline_versions_create**](docs/pipelines.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
[**pipeline_versions_delete**](docs/pipelines.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
[**pipeline_versions_get**](docs/pipelines.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
[**pipeline_versions_list**](docs/pipelines.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
[**pipeline_versions_update**](docs/pipelines.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
[**pipelines_create**](docs/pipelines.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](docs/pipelines.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
[**pipelines_get**](docs/pipelines.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
[**pipelines_list**](docs/pipelines.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](docs/pipelines.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline
[**metrics_get**](docs/projects.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**project_audit_events_list**](docs/projects.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](docs/projects.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](docs/projects.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](docs/projects.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](docs/projects.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](docs/projects.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_usage_get**](docs/projects.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**projects_create**](docs/projects.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](docs/projects.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](docs/projects.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](docs/projects.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](docs/projects.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](docs/projects.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](docs/projects.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**request_schedules_create**](docs/request_schedules.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](docs/request_schedules.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](docs/request_schedules.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](docs/request_schedules.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](docs/request_schedules.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
[**permissions_list**](docs/roles.md#permissions_list) | **GET** /permissions | List the available permissions
[**role_assignments_create**](docs/roles.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
[**role_assignments_delete**](docs/roles.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
[**role_assignments_get**](docs/roles.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
[**role_assignments_per_user_list**](docs/roles.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
[**roles_create**](docs/roles.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](docs/roles.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](docs/roles.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](docs/roles.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](docs/roles.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**service_users_create**](docs/service_users.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](docs/service_users.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](docs/service_users.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](docs/service_users.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](docs/service_users.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](docs/service_users.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**service_status**](docs/status.md#service_status) | **GET** /status | Service status
[**user_create**](docs/user.md#user_create) | **POST** /user | Create a new user
[**user_delete**](docs/user.md#user_delete) | **DELETE** /user | Delete user


## Documentation for Authorization


### api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


