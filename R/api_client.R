# UbiOps
#
# Client Library to interact with the UbiOps API.
#
# UbiOps API version: v2.1
# Generated by custom generator based on: https://openapi-generator.tech


get_setting <- function(var.name, local.var, default="") {
    if (!is.null(local.var)) {
        local.var
    } else {
        Sys.getenv(var.name, unset=default)
    }
}


get_base_path <- function(string) {
    #  Make sure basePath has no "/" at the end
    if (substr(string, nchar(string), nchar(string)) == "/") {
        string <- substr(string, 1, nchar(string) - 1)
    }
    string
}


get_authorization_headers <- function(token) {
    c("Authorization" = token)
}


get_default_headers <- function(string) {
    headers <- c()
    for (i in strsplit(string, ",")[[1]]) {
        key_value <- trimws(strsplit(i, ":", fixed=TRUE)[[1]])
        if (length(key_value) == 2){
            headers[key_value[1]] <- key_value[2]
        }
    }
    headers
}


get_http_timeout <- function(timeout) {
    if (!is.na(timeout)) {
        httr::timeout(strtoi(timeout))
    }
}


#' @title Call API
#' @description Call an endpoint of the UbiOps API
#' @param url_path API endpoint to call, e.g., "status"
#' @param http_method HTTP method to use, e.g., "POST"
#' @param body body of the request (optional)
#' @param query_params query parameters (optional)
#' @param content_type content type (optional)
#' @param encode encode (optional)
#' @param UBIOPS_PROJECT (system environment variable) UbiOps project name
#' @param UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
#' @param UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
#' @param UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
#' @param UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""
#' @param ... additional parameters to pass to httr GET/POST/PUT/PATCH/HEAD/DELETE function
#' @return Response content from the API
call_api <- function(url_path, http_method, body = NULL, query_params = NULL, content_type = NULL, encode = NULL,
                     UBIOPS_API_TOKEN = NULL, UBIOPS_API_URL = NULL, UBIOPS_PROJECT = NULL, UBIOPS_TIMEOUT = NULL,
                     UBIOPS_DEFAULT_HEADERS = NULL, ...){

    project.name <- get_setting("UBIOPS_PROJECT", UBIOPS_PROJECT)
    base_path <- get_base_path(get_setting("UBIOPS_API_URL", UBIOPS_API_URL, default = "https://api.ubiops.com/v2.1"))
    header.params <- get_authorization_headers(get_setting("UBIOPS_API_TOKEN", UBIOPS_API_TOKEN))
    header.defaults <- get_default_headers(get_setting("UBIOPS_DEFAULT_HEADERS", UBIOPS_DEFAULT_HEADERS))
    timeout <- get_http_timeout(get_setting("UBIOPS_TIMEOUT", UBIOPS_TIMEOUT, default = NA))
    user_agent <- "UbiOps/r/0.19.1"

    if (project.name != "") {
        url_path <- gsub("\\{project_name\\}", utils::URLencode(as.character(project.name), reserved = TRUE), url_path)
    } else if (!grepl(url_path, "\\{project_name\\}", fixed = TRUE)) {
        stop("Missing required parameter `UBIOPS_PROJECT`.")
    }

    url <- paste0(base_path, url_path)
    headers <- httr::add_headers(c(header.params, header.defaults))
    user_agent <- httr::user_agent(user_agent)

    if (is.null(content_type)) {
        content_type <- httr::content_type_json()
        encode <- 'json'
    }

    if (http_method == "GET") {
        resp <- httr::GET(url, query = query_params, headers, timeout, user_agent, ...)
    } else if (http_method == "POST") {
        resp <- httr::POST(url, query = query_params, headers, content_type, timeout, user_agent, body = body, encode = encode, ...)
    } else if (http_method == "PUT") {
        resp <- httr::PUT(url, query = query_params, headers, content_type, timeout, timeout, user_agent, body = body, encode = encode, ...)
    } else if (http_method == "PATCH") {
        resp <- httr::PATCH(url, query = query_params, headers, content_type, timeout, timeout, user_agent, body = body, encode = encode, ...)
    } else if (http_method == "HEAD") {
        resp <- httr::HEAD(url, query = query_params, headers, timeout, timeout, user_agent, ...)
    } else if (http_method == "DELETE") {
        resp <- httr::DELETE(url, query = query_params, headers, timeout, timeout, user_agent, ...)
    } else {
        stop("Http method must be `GET`, `HEAD`, `OPTIONS`, `POST`, `PATCH`, `PUT` or `DELETE`.")
    }

    if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        resp

    } else {
        parsed_content <- tryCatch(
            httr::content(resp, "parsed"), error = function(){ list() }
        )

        if (!is.null(parsed_content[["error"]])) {
            error_msg <- paste0("Error (", httr::status_code(resp), ") : ", parsed_content[["error"]])
        } else if (!is.null(parsed_content[["error_message"]])) {
            error_msg <- paste0("Error (", httr::status_code(resp), ") : ", parsed_content[["error_message"]])
        } else {
            error_msg <- paste0("Error (", httr::status_code(resp), ") : ", "An unknown error occured")
        }
        stop(error_msg)
    }
}


#' @title Deserialize the content of api response
#' @param resp API response
#' @return Deserialized content
deserialize <- function(resp) {
    jsonlite::parse_json(httr::content(resp, "text", encoding = "UTF-8"))
}


#' @title Write file to storage location
#' @param resp API response
#' @param ... additional parameters
#' @include api_response.R
#' @return File path
deserialize_file <- function(resp, ...) {
    tmp_dir <- get_setting("UBIOPS_TEMP_FOLDER_PATH", list(...), default = getwd())

    result <- ApiFileResponse$new(resp)
    file_name <- result$getFileName()

    output_location <- file.path(tmp_dir, file_name)
    output <- file(output_location, "wb")
    readr::write_file(result$getContent(), output)
    close(output)

    output_location
}
