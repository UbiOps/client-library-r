# UbiOps
#
# Client Library to interact with the UbiOps API.
#
# UbiOps API version: v2.1
# Generated by custom generator based on: https://openapi-generator.tech

# Monitoring operations


#' @title Create notification groups
#' @description Create a notification group by defining a name and a list of contacts
#' @param data  named list of: [ name, contacts ]
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the created notification group
#'   - `id`: Unique identifier for the notification group (UUID)
#'   - `name`: Name of the notification group
#'   - `contacts`: A list of contacts in the notification group
#' @examples
#' \dontrun{
#' data <- list(
#'  name = "name",
#'  contacts = list(  # (optional)
#'    list(
#'      type = "type",
#'      configuration = list(key = "value")
#'    )
#'  )
#' )
#'
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::notification_groups_create(
#'    data
#' )
#' 
#' # Or provide directly
#' result <- ubiops::notification_groups_create(
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
notification_groups_create <- function(data,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`data`)) {
    stop("Missing required parameter `data`.")
  }
  
  body <- rjson::toJSON(data)
  
  url_path <- "/projects/{project_name}/monitoring/notification-groups"

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


#' @title Delete notification group
#' @description Delete a notification group
#' @param notification.group.name  character
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
#' ubiops::notification_groups_delete(
#'    notification.group.name
#' )
#' 
#' # Or provide directly
#' ubiops::notification_groups_delete(
#'    notification.group.name,
#'    UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
#' )
#' 
#' # The default API url is https://api.ubiops.com/v2.1
#' # Want to use a different API url?
#' # Provide `UBIOPS_API_URL`, either directly or as environment variable.
#' }
#' @export
notification_groups_delete <- function(notification.group.name,  ...){
  query_params <- list()

  if (missing(`notification.group.name`)) {
    stop("Missing required parameter `notification.group.name`.")
  }
  
  url_path <- "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"
  if (!missing(`notification.group.name`)) {
    url_path <- gsub("\\{notification_group_name\\}", utils::URLencode(as.character(`notification.group.name`), reserved = TRUE), url_path)
  }

  api.response <- call_api(url_path, "DELETE", NULL, query_params, ...)
  return(invisible(NULL))
}


#' @title Get notification group
#' @description Retrieve details of a single notification group in a project
#' @param notification.group.name  character
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of a notification group
#'   - `id`: Unique identifier for the notification group (UUID)
#'   - `name`: Name of the notification group
#'   - `contacts`: A list of contacts in the notification group
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::notification_groups_get(
#'    notification.group.name
#' )
#' 
#' # Or provide directly
#' result <- ubiops::notification_groups_get(
#'    notification.group.name,
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
notification_groups_get <- function(notification.group.name,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`notification.group.name`)) {
    stop("Missing required parameter `notification.group.name`.")
  }
  
  url_path <- "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"
  if (!missing(`notification.group.name`)) {
    url_path <- gsub("\\{notification_group_name\\}", utils::URLencode(as.character(`notification.group.name`), reserved = TRUE), url_path)
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


#' @title List notification groups
#' @description List the notification groups in a project
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  A list of details of the notification groups in the project
#'   - `id`: Unique identifier for the notification group (UUID)
#'   - `name`: Name of the notification group
#'   - `contacts`: A list of contacts in the notification group
#' @examples
#' \dontrun{
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::notification_groups_list(
#'    
#' )
#' 
#' # Or provide directly
#' result <- ubiops::notification_groups_list(
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
notification_groups_list <- function( preload_content=TRUE, ...){
  query_params <- list()

  
  url_path <- "/projects/{project_name}/monitoring/notification-groups"

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


#' @title Update notification group
#' @description Update a notification group
#' @param notification.group.name  character
#' @param data  named list of: [ name (optional), contacts (optional) ]
#' @param preload_content (optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE
#' @param ...
#'  UBIOPS_PROJECT (system environment variable) UbiOps project name
#'  UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#'  UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#'  UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#'  UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @return Response from the API
#'  Details of the updated notification group
#'   - `id`: Unique identifier for the notification group (UUID)
#'   - `name`: Name of the notification group
#'   - `contacts`: A list of contacts in the notification group
#' @examples
#' \dontrun{
#' data <- list(
#'  name = "name",  # (optional)
#'  contacts = list(  # (optional)
#'    list(
#'      type = "type",
#'      configuration = list(key = "value")
#'    )
#'  )
#' )
#'
#' # Use environment variables
#' Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
#' Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
#' result <- ubiops::notification_groups_update(
#'    notification.group.name, data
#' )
#' 
#' # Or provide directly
#' result <- ubiops::notification_groups_update(
#'    notification.group.name, data,
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
notification_groups_update <- function(notification.group.name, data,  preload_content=TRUE, ...){
  query_params <- list()

  if (missing(`notification.group.name`)) {
    stop("Missing required parameter `notification.group.name`.")
  }
  if (missing(`data`)) {
    stop("Missing required parameter `data`.")
  }
  
  body <- rjson::toJSON(data)
  
  url_path <- "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"
  if (!missing(`notification.group.name`)) {
    url_path <- gsub("\\{notification_group_name\\}", utils::URLencode(as.character(`notification.group.name`), reserved = TRUE), url_path)
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
