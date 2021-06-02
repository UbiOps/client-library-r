#' @docType class
#' @title ApiResponse
#' @description ApiResponse Class
#' @format An \code{R6Class} generator object
#' @field response The raw response from the endpoint.
#' @export
ApiResponse  <- R6::R6Class(
  'ApiResponse',
  public = list(
    response = NULL,
    initialize = function(response){
      self$response <- response
    },
    getContent = function () {
      httr::content(self$response, "text", encoding = "UTF-8")
    }
  )
)


#' @docType class
#' @title ApiFileResponse
#' @description ApiFileResponse Class
#' @format An \code{R6Class} generator object
#' @field response The raw response from the endpoint.
#' @export
ApiFileResponse <- R6::R6Class(
  'ApiFileResponse',
  public = list(
    response = NULL,
    initialize = function(response){
      self$response <- response
    },
    getContent = function () {
      httr::content(self$response)
    },
    getFileName = function () {
      content_disposition <- httr::headers(self$response)[['content-disposition']]
      file_name <- stringr::str_trim(substring(content_disposition, 23, stringr::str_length(content_disposition)-1))
    }
))
