# ubiops

[www.ubiops.com](https://ubiops.com)

Client Library to interact with the UbiOps API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.1
- Package version: 3.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://ubiops.com/docs](https://ubiops.com/docs)

## Requirements.

Python 3.5+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install ubiops
```
(you may need to run `pip` with root permission: `sudo pip install ubiops`)

Then import the package:
```python
import ubiops
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ubiops
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import ubiops


configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'YOUR_API_TOKEN'
configuration.api_key_prefix['Authorization'] = ''

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)
# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

api_response = api_instance.service_status()
print(api_response)

# Close the connection
api_client.close()

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ubiops.com/v2.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoreApi* | [**batch_deployment_requests_batch_delete**](docs/CoreApi.md#batch_deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch-delete | Delete multiple batch deployment requests
*CoreApi* | [**batch_deployment_requests_batch_get**](docs/CoreApi.md#batch_deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch-collect | Retrieve multiple batch deployment request results
*CoreApi* | [**batch_deployment_requests_create**](docs/CoreApi.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch | Create batch deployment requests
*CoreApi* | [**batch_deployment_requests_delete**](docs/CoreApi.md#batch_deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch/{request_id} | Delete batch deployment requests
*CoreApi* | [**batch_deployment_requests_get**](docs/CoreApi.md#batch_deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch/{request_id} | Get batch deployment request
*CoreApi* | [**batch_deployment_requests_list**](docs/CoreApi.md#batch_deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request-batch | List batch deployment requests
*CoreApi* | [**batch_pipeline_requests_batch_delete**](docs/CoreApi.md#batch_pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-delete | Delete multiple batch pipeline requests
*CoreApi* | [**batch_pipeline_requests_batch_get**](docs/CoreApi.md#batch_pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-collect | Retrieve multiple batch pipeline request results
*CoreApi* | [**batch_pipeline_requests_create**](docs/CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | Create batch pipeline requests
*CoreApi* | [**batch_pipeline_requests_delete**](docs/CoreApi.md#batch_pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Delete batch pipeline requests
*CoreApi* | [**batch_pipeline_requests_get**](docs/CoreApi.md#batch_pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Get batch pipeline request
*CoreApi* | [**batch_pipeline_requests_list**](docs/CoreApi.md#batch_pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | List batch pipeline requests
*CoreApi* | [**blobs_create**](docs/CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
*CoreApi* | [**blobs_delete**](docs/CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
*CoreApi* | [**blobs_get**](docs/CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
*CoreApi* | [**blobs_list**](docs/CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
*CoreApi* | [**builds_get**](docs/CoreApi.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
*CoreApi* | [**builds_list**](docs/CoreApi.md#builds_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds | List builds
*CoreApi* | [**deployment_audit_events_list**](docs/CoreApi.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
*CoreApi* | [**deployment_environment_variables_copy**](docs/CoreApi.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
*CoreApi* | [**deployment_environment_variables_create**](docs/CoreApi.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
*CoreApi* | [**deployment_environment_variables_delete**](docs/CoreApi.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
*CoreApi* | [**deployment_environment_variables_get**](docs/CoreApi.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
*CoreApi* | [**deployment_environment_variables_list**](docs/CoreApi.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
*CoreApi* | [**deployment_environment_variables_update**](docs/CoreApi.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
*CoreApi* | [**deployment_requests_create**](docs/CoreApi.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/request | Create deployment requests
*CoreApi* | [**deployments_create**](docs/CoreApi.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create a deployment
*CoreApi* | [**deployments_delete**](docs/CoreApi.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
*CoreApi* | [**deployments_get**](docs/CoreApi.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of deployment
*CoreApi* | [**deployments_list**](docs/CoreApi.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments in project
*CoreApi* | [**deployments_update**](docs/CoreApi.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
*CoreApi* | [**metrics_get**](docs/CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
*CoreApi* | [**organization_usage_details_get**](docs/CoreApi.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
*CoreApi* | [**organization_usage_get**](docs/CoreApi.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
*CoreApi* | [**organization_users_create**](docs/CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
*CoreApi* | [**organization_users_delete**](docs/CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
*CoreApi* | [**organization_users_get**](docs/CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
*CoreApi* | [**organization_users_list**](docs/CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
*CoreApi* | [**organization_users_update**](docs/CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
*CoreApi* | [**organizations_create**](docs/CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
*CoreApi* | [**organizations_get**](docs/CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
*CoreApi* | [**organizations_list**](docs/CoreApi.md#organizations_list) | **GET** /organizations | List organizations
*CoreApi* | [**organizations_resource_usage**](docs/CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
*CoreApi* | [**organizations_update**](docs/CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
*CoreApi* | [**permissions_list**](docs/CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
*CoreApi* | [**pipeline_audit_events_list**](docs/CoreApi.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
*CoreApi* | [**pipeline_object_attachments_create**](docs/CoreApi.md#pipeline_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/attachments | Create object attachments
*CoreApi* | [**pipeline_object_attachments_delete**](docs/CoreApi.md#pipeline_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/attachments/{attachment_id} | Delete attachment in a pipeline
*CoreApi* | [**pipeline_object_attachments_destination_get**](docs/CoreApi.md#pipeline_object_attachments_destination_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{destination_name}/attachments/ | List the attachments of a destination object
*CoreApi* | [**pipeline_object_attachments_get**](docs/CoreApi.md#pipeline_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments/{attachment_id} | Get an attachment in a pipeline
*CoreApi* | [**pipeline_object_attachments_list**](docs/CoreApi.md#pipeline_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments | List object attachments
*CoreApi* | [**pipeline_object_environment_variables_list**](docs/CoreApi.md#pipeline_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name}/environment-variables | List pipeline object environment variables
*CoreApi* | [**pipeline_objects_create**](docs/CoreApi.md#pipeline_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/objects | Add an object to a pipeline
*CoreApi* | [**pipeline_objects_delete**](docs/CoreApi.md#pipeline_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Delete object from pipeline
*CoreApi* | [**pipeline_objects_get**](docs/CoreApi.md#pipeline_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Get an object in a pipeline
*CoreApi* | [**pipeline_objects_list**](docs/CoreApi.md#pipeline_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects | List objects in a pipeline
*CoreApi* | [**pipeline_objects_update**](docs/CoreApi.md#pipeline_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Update an object in a pipeline
*CoreApi* | [**pipeline_requests_create**](docs/CoreApi.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request | Make a request to a pipeline
*CoreApi* | [**pipelines_create**](docs/CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
*CoreApi* | [**pipelines_delete**](docs/CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete pipeline
*CoreApi* | [**pipelines_get**](docs/CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get pipeline
*CoreApi* | [**pipelines_list**](docs/CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
*CoreApi* | [**pipelines_update**](docs/CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update pipeline
*CoreApi* | [**project_audit_events_list**](docs/CoreApi.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
*CoreApi* | [**project_environment_variables_create**](docs/CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
*CoreApi* | [**project_environment_variables_delete**](docs/CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
*CoreApi* | [**project_environment_variables_get**](docs/CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
*CoreApi* | [**project_environment_variables_list**](docs/CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
*CoreApi* | [**project_environment_variables_update**](docs/CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
*CoreApi* | [**project_usage_get**](docs/CoreApi.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
*CoreApi* | [**projects_create**](docs/CoreApi.md#projects_create) | **POST** /projects | Create projects
*CoreApi* | [**projects_delete**](docs/CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
*CoreApi* | [**projects_get**](docs/CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
*CoreApi* | [**projects_list**](docs/CoreApi.md#projects_list) | **GET** /projects | List projects
*CoreApi* | [**projects_log_list**](docs/CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
*CoreApi* | [**projects_resource_usage**](docs/CoreApi.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
*CoreApi* | [**projects_update**](docs/CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
*CoreApi* | [**request_schedules_create**](docs/CoreApi.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
*CoreApi* | [**request_schedules_delete**](docs/CoreApi.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
*CoreApi* | [**request_schedules_get**](docs/CoreApi.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
*CoreApi* | [**request_schedules_list**](docs/CoreApi.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
*CoreApi* | [**request_schedules_update**](docs/CoreApi.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
*CoreApi* | [**revisions_file_download**](docs/CoreApi.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
*CoreApi* | [**revisions_file_upload**](docs/CoreApi.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
*CoreApi* | [**revisions_get**](docs/CoreApi.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
*CoreApi* | [**revisions_list**](docs/CoreApi.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions
*CoreApi* | [**role_assignments_create**](docs/CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
*CoreApi* | [**role_assignments_delete**](docs/CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
*CoreApi* | [**role_assignments_get**](docs/CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
*CoreApi* | [**role_assignments_per_user_list**](docs/CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
*CoreApi* | [**roles_create**](docs/CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
*CoreApi* | [**roles_delete**](docs/CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
*CoreApi* | [**roles_get**](docs/CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
*CoreApi* | [**roles_list**](docs/CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
*CoreApi* | [**roles_update**](docs/CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
*CoreApi* | [**service_status**](docs/CoreApi.md#service_status) | **GET** /status | Service status
*CoreApi* | [**service_users_create**](docs/CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
*CoreApi* | [**service_users_delete**](docs/CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
*CoreApi* | [**service_users_get**](docs/CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
*CoreApi* | [**service_users_list**](docs/CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
*CoreApi* | [**service_users_token**](docs/CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
*CoreApi* | [**service_users_update**](docs/CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
*CoreApi* | [**user_create**](docs/CoreApi.md#user_create) | **POST** /user | Create a new user
*CoreApi* | [**user_delete**](docs/CoreApi.md#user_delete) | **DELETE** /user | Delete user
*CoreApi* | [**version_environment_variables_copy**](docs/CoreApi.md#version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy version environment variable
*CoreApi* | [**version_environment_variables_create**](docs/CoreApi.md#version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create version environment variable
*CoreApi* | [**version_environment_variables_delete**](docs/CoreApi.md#version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete version environment variable
*CoreApi* | [**version_environment_variables_get**](docs/CoreApi.md#version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get version environment variable
*CoreApi* | [**version_environment_variables_list**](docs/CoreApi.md#version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List version environment variables
*CoreApi* | [**version_environment_variables_update**](docs/CoreApi.md#version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update version environment variable
*CoreApi* | [**versions_create**](docs/CoreApi.md#versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create versions
*CoreApi* | [**versions_delete**](docs/CoreApi.md#versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete version
*CoreApi* | [**versions_get**](docs/CoreApi.md#versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get version
*CoreApi* | [**versions_list**](docs/CoreApi.md#versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List versions
*CoreApi* | [**versions_update**](docs/CoreApi.md#versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update version


## Documentation For Models

 - [AttachmentFieldsCreate](docs/AttachmentFieldsCreate.md)
 - [AttachmentFieldsList](docs/AttachmentFieldsList.md)
 - [AttachmentSourcesCreate](docs/AttachmentSourcesCreate.md)
 - [AttachmentSourcesList](docs/AttachmentSourcesList.md)
 - [AttachmentsCreate](docs/AttachmentsCreate.md)
 - [AttachmentsList](docs/AttachmentsList.md)
 - [AuditList](docs/AuditList.md)
 - [BatchDeploymentRequestCreateResponse](docs/BatchDeploymentRequestCreateResponse.md)
 - [BatchDeploymentRequestDetail](docs/BatchDeploymentRequestDetail.md)
 - [BatchDeploymentRequestList](docs/BatchDeploymentRequestList.md)
 - [BatchDeploymentRequestSingleDetail](docs/BatchDeploymentRequestSingleDetail.md)
 - [BatchPipelineRequestCreateResponse](docs/BatchPipelineRequestCreateResponse.md)
 - [BatchPipelineRequestDeploymentRequest](docs/BatchPipelineRequestDeploymentRequest.md)
 - [BatchPipelineRequestDetail](docs/BatchPipelineRequestDetail.md)
 - [BatchPipelineRequestList](docs/BatchPipelineRequestList.md)
 - [BatchPipelineRequestSingleDetail](docs/BatchPipelineRequestSingleDetail.md)
 - [BlobList](docs/BlobList.md)
 - [BlobUpload](docs/BlobUpload.md)
 - [BuildList](docs/BuildList.md)
 - [DeploymentCreate](docs/DeploymentCreate.md)
 - [DeploymentInputFieldCreate](docs/DeploymentInputFieldCreate.md)
 - [DeploymentInputFieldList](docs/DeploymentInputFieldList.md)
 - [DeploymentList](docs/DeploymentList.md)
 - [DeploymentOutputFieldCreate](docs/DeploymentOutputFieldCreate.md)
 - [DeploymentOutputFieldList](docs/DeploymentOutputFieldList.md)
 - [DeploymentRequestList](docs/DeploymentRequestList.md)
 - [DeploymentUpdate](docs/DeploymentUpdate.md)
 - [EnvironmentVariableCopy](docs/EnvironmentVariableCopy.md)
 - [EnvironmentVariableCreate](docs/EnvironmentVariableCreate.md)
 - [EnvironmentVariableList](docs/EnvironmentVariableList.md)
 - [InheritedEnvironmentVariableList](docs/InheritedEnvironmentVariableList.md)
 - [Logs](docs/Logs.md)
 - [LogsCreate](docs/LogsCreate.md)
 - [Metrics](docs/Metrics.md)
 - [OrganizationCreate](docs/OrganizationCreate.md)
 - [OrganizationDetail](docs/OrganizationDetail.md)
 - [OrganizationList](docs/OrganizationList.md)
 - [OrganizationUpdate](docs/OrganizationUpdate.md)
 - [OrganizationUserCreate](docs/OrganizationUserCreate.md)
 - [OrganizationUserDetail](docs/OrganizationUserDetail.md)
 - [OrganizationUserUpdate](docs/OrganizationUserUpdate.md)
 - [PermissionList](docs/PermissionList.md)
 - [PipelineCreate](docs/PipelineCreate.md)
 - [PipelineInputFieldCreate](docs/PipelineInputFieldCreate.md)
 - [PipelineInputFieldList](docs/PipelineInputFieldList.md)
 - [PipelineList](docs/PipelineList.md)
 - [PipelineObjectCreate](docs/PipelineObjectCreate.md)
 - [PipelineObjectList](docs/PipelineObjectList.md)
 - [PipelineObjectUpdate](docs/PipelineObjectUpdate.md)
 - [PipelineRequestDeploymentRequest](docs/PipelineRequestDeploymentRequest.md)
 - [PipelineRequestList](docs/PipelineRequestList.md)
 - [ProjectCreate](docs/ProjectCreate.md)
 - [ProjectList](docs/ProjectList.md)
 - [ProjectResourceUsage](docs/ProjectResourceUsage.md)
 - [ProjectUpdate](docs/ProjectUpdate.md)
 - [ResourceUsage](docs/ResourceUsage.md)
 - [RevisionCreate](docs/RevisionCreate.md)
 - [RevisionList](docs/RevisionList.md)
 - [RoleAssignmentCreate](docs/RoleAssignmentCreate.md)
 - [RoleAssignmentList](docs/RoleAssignmentList.md)
 - [RoleCreate](docs/RoleCreate.md)
 - [RoleDetailList](docs/RoleDetailList.md)
 - [RoleList](docs/RoleList.md)
 - [RoleUpdate](docs/RoleUpdate.md)
 - [ScheduleCreate](docs/ScheduleCreate.md)
 - [ScheduleList](docs/ScheduleList.md)
 - [ScheduleUpdate](docs/ScheduleUpdate.md)
 - [ServiceUserCreate](docs/ServiceUserCreate.md)
 - [ServiceUserDetail](docs/ServiceUserDetail.md)
 - [ServiceUserList](docs/ServiceUserList.md)
 - [ServiceUserTokenList](docs/ServiceUserTokenList.md)
 - [Status](docs/Status.md)
 - [UsagePerDay](docs/UsagePerDay.md)
 - [UsagePerDayMetric](docs/UsagePerDayMetric.md)
 - [UsagePerMonth](docs/UsagePerMonth.md)
 - [UsagePerMonthMetric](docs/UsagePerMonthMetric.md)
 - [UserPendingCreate](docs/UserPendingCreate.md)
 - [UserPendingDetail](docs/UserPendingDetail.md)
 - [VersionCreate](docs/VersionCreate.md)
 - [VersionDetail](docs/VersionDetail.md)
 - [VersionList](docs/VersionList.md)
 - [VersionUpdate](docs/VersionUpdate.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


