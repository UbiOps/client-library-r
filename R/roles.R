# UbiOps
#
# Client Library to interact with the UbiOps API.
#
# UbiOps API version: v2.1
# Generated by custom generator based on: https://openapi-generator.tech

# Roles operations


#' @title List the available permissions
#' @description List all the available permissions which can be used to create custom roles.
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  A list of available permissions
#'    - `name`: Name of the permission
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::permissions_list(
#'    
#' )
#' 
#' # Or provide directly
#' result <- ubiops::permissions_list(
#'    UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
permissions_list <- function( preload_content=TRUE, ...){
  query_params <- list()

  
  url_path <- "/permissions"
  api.response <- call_api(url_path, "GET", NULL, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title Assign a role to a user in a project
#' @description Assign a role to a user in the scope of a project. This role can be assigned on either project level or on object level, which can be a deployment or pipeline. The user making the request must have appropriate permissions.
#' @param data  named list of: [ user_id, role, object_name (optional), object_type (optional) ]
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the created role assignment
#'   - `id`: Unique identifier for the role assignment (UUID) 
#'   - `user_id`: Unique identifier for the user (UUID) 
#'   - `role`: Name of the role assigned to the user 
#'   - `object_name`: Name of the object for which the role is assigned 
#'   - `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.
#' @examples
#' \dontrun{
#' data <- list(
#'  user_id = "user_id",
#'  role = "role",
#'  object_name = "object_name",  # (optional)
#'  object_type = "object_type"  # (optional)
#' )
#'
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::role_assignments_create(
#'    data
#' )
#' 
#' # Or provide directly
#' result <- ubiops::role_assignments_create(
#'    data,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
role_assignments_create <- function(data,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`data`)) {
    stop("Missing required parameter `data`.")
  }
  
  body <- rjson::toJSON(data)
  
  url_path <- "/projects/{project_name}/role-assignments"

  api.response <- call_api(url_path, "POST", body, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title Delete a role from a user with the given role assignment id
#' @description Delete a role of a user. The user making the request must have appropriate permissions. It is possible for a user to delete their own role if they have permissions to do so.
#' @param id  character
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' ubiops::role_assignments_delete(
#'    id
#' )
#' 
#' # Or provide directly
#' ubiops::role_assignments_delete(
#'    id,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
role_assignments_delete <- function(id,  ...){
  query_params <- list()

  if (missing(`id`)) {
    stop("Missing required parameter `id`.")
  }
  
  url_path <- "/projects/{project_name}/role-assignments/{id}"
  if (!missing(`id`)) {
    url_path <- gsub("\\{id\\}", utils::URLencode(as.character(`id`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "DELETE", NULL, query_params, ...)
  return(invisible(NULL))
}


#' @title Get details of a role assignment
#' @description Get the details of a role assignment of a user. The user making the request must have appropriate permissions.
#' @param id  character
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the role assignment
#'   - `id`: Unique identifier for the role assignment (UUID) 
#'   - `user_id`: Unique identifier for the user (UUID) 
#'   - `role`: Name of the role assigned to the user 
#'   - `object_name`: Name of the object for which the role is assigned 
#'   - `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::role_assignments_get(
#'    id
#' )
#' 
#' # Or provide directly
#' result <- ubiops::role_assignments_get(
#'    id,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
role_assignments_get <- function(id,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`id`)) {
    stop("Missing required parameter `id`.")
  }
  
  url_path <- "/projects/{project_name}/role-assignments/{id}"
  if (!missing(`id`)) {
    url_path <- gsub("\\{id\\}", utils::URLencode(as.character(`id`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "GET", NULL, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title List the roles assigned to a specific user in a project
#' @description List the roles assigned to a user in the scope of a project.
#' @param user.id  character
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  - `id`: Unique identifier for the role assignment (UUID) 
#'   - `user_id`: Unique identifier for the user (UUID) 
#'   - `role`: Name of the role assigned to the user 
#'   - `object_name`: Name of the object for which the role is assigned 
#'   - `object_type`: Type of the object for which the role is assigned. It can be project, deployment or pipeline.
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::role_assignments_per_user_list(
#'    user.id
#' )
#' 
#' # Or provide directly
#' result <- ubiops::role_assignments_per_user_list(
#'    user.id,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
role_assignments_per_user_list <- function(user.id,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`user.id`)) {
    stop("Missing required parameter `user.id`.")
  }
  
  url_path <- "/projects/{project_name}/users/{user_id}/role-assignments"
  if (!missing(`user.id`)) {
    url_path <- gsub("\\{user_id\\}", utils::URLencode(as.character(`user.id`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "GET", NULL, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title Create a custom role scoped in a project
#' @description Create a custom role in the scope of a project. This role is not accessible from other projects.  The user making the request must have appropriate permissions.
#' @param data  named list of: [ name, permissions ]
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the created role
#'   - `id`: Unique identifier for the created role (UUID) 
#'   - `name`: Name of the created role 
#'   - `default`: A boolean value that indicates whether the role is a default role or not 
#'   - `permissions`: A list of permissions which the role contains
#' @examples
#' \dontrun{
#' data <- list(
#'  name = "name",
#'  permissions = list("value-1", "value-2")  # (optional)
#' )
#'
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::roles_create(
#'    data
#' )
#' 
#' # Or provide directly
#' result <- ubiops::roles_create(
#'    data,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
roles_create <- function(data,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`data`)) {
    stop("Missing required parameter `data`.")
  }
  
  body <- rjson::toJSON(data)
  
  url_path <- "/projects/{project_name}/roles"

  api.response <- call_api(url_path, "POST", body, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title Delete a role from a project
#' @description Delete a role from a project. The user making the request must have appropriate permissions. **Default roles cannot be deleted.**
#' @param role.name  character
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' ubiops::roles_delete(
#'    role.name
#' )
#' 
#' # Or provide directly
#' ubiops::roles_delete(
#'    role.name,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
roles_delete <- function(role.name,  ...){
  query_params <- list()

  if (missing(`role.name`)) {
    stop("Missing required parameter `role.name`.")
  }
  
  url_path <- "/projects/{project_name}/roles/{role_name}"
  if (!missing(`role.name`)) {
    url_path <- gsub("\\{role_name\\}", utils::URLencode(as.character(`role.name`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "DELETE", NULL, query_params, ...)
  return(invisible(NULL))
}


#' @title Get details of a role
#' @description Get the details of a role. The user making the request must have appropriate permissions.
#' @param role.name  character
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the role
#'   - `id`: Unique identifier for the role (UUID) 
#'   - `name`: Name of the role 
#'   - `default`: A boolean value that indicates whether the role is a default role or not 
#'   - `permissions`: A list of permissions which the role contains
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::roles_get(
#'    role.name
#' )
#' 
#' # Or provide directly
#' result <- ubiops::roles_get(
#'    role.name,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
roles_get <- function(role.name,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`role.name`)) {
    stop("Missing required parameter `role.name`.")
  }
  
  url_path <- "/projects/{project_name}/roles/{role_name}"
  if (!missing(`role.name`)) {
    url_path <- gsub("\\{role_name\\}", utils::URLencode(as.character(`role.name`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "GET", NULL, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title List the available roles in a project
#' @description List the roles available in the scope of a project. Information on which permissions each role contains, can be obtained with a call to get details of a single role.
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  - `id`: Unique identifier for the role (UUID) 
#'   - `name`: Name of the role 
#'   - `default`: A boolean value that indicates whether the role is a default role or not
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::roles_list(
#'    
#' )
#' 
#' # Or provide directly
#' result <- ubiops::roles_list(
#'    
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
roles_list <- function( preload_content=TRUE, ...){
  query_params <- list()

  
  url_path <- "/projects/{project_name}/roles"

  api.response <- call_api(url_path, "GET", NULL, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}


#' @title Update a role in a project
#' @description Update a role in a project. The user making the request must have appropriate permissions. **Default roles cannot be updated.**
#' @param role.name  character
#' @param data  named list of: [ name (optional), permissions (optional) ]
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the updated role
#'   - `id`: Unique identifier for the role (UUID) 
#'   - `name`: Name of the updated role 
#'   - `default`: A boolean value that indicates whether the role is a default role or not 
#'   - `permissions`: A list of permissions which the role contains
#' @examples
#' \dontrun{
#' data <- list(
#'  name = "name",  # (optional)
#'  permissions = list("value-1", "value-2")  # (optional)
#' )
#'
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::roles_update(
#'    role.name, data
#' )
#' 
#' # Or provide directly
#' result <- ubiops::roles_update(
#'    role.name, data,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' print(result)
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
roles_update <- function(role.name, data,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`role.name`)) {
    stop("Missing required parameter `role.name`.")
  }
  if (missing(`data`)) {
    stop("Missing required parameter `data`.")
  }
  
  body <- rjson::toJSON(data)
  
  url_path <- "/projects/{project_name}/roles/{role_name}"
  if (!missing(`role.name`)) {
    url_path <- gsub("\\{role_name\\}", utils::URLencode(as.character(`role.name`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "PATCH", body, query_params, ...)
  if (preload_content) {
    deserializedRespObj <- tryCatch(
      deserialize(api.response),
      error = function(e){
        stop("Failed to deserialize response")
      }
    )

  } else {
    ApiResponse$new(api.response)
  }
}