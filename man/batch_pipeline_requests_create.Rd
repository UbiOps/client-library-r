% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/pipeline_requests.R
\name{batch_pipeline_requests_create}
\alias{batch_pipeline_requests_create}
\title{Create a batch pipeline request}
\usage{
batch_pipeline_requests_create(
  pipeline.name,
  data,
  timeout = NULL,
  notification.group = NULL,
  preload_content = TRUE,
  ...
)
}
\arguments{
\item{pipeline.name}{character}

\item{data}{list() - Example: list( list(input_field_1 = "input_value_1", input_field_2 = "input_value_2") )}

\item{timeout}{(optional) integer}

\item{notification.group}{(optional) character}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 A list of dictionaries containing the details of the created pipeline requests with the following fields:
  - `id`: Unique identifier for the pipeline request, which can be used to collect the result
  - `pipeline`: Name of the pipeline for which the request is made
  - `version`: Name of the pipeline version for which the request is made
  - `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
  - `time_created`: Server time that the request was made (current time)
}
\description{
Make a batch request to the default version of a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.  The maximum number of requests that can be created per batch is 250.
}
\examples{
\dontrun{
data <- list( list(input_field_1 = "input_value_1", input_field_2 = "input_value_2") )

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::batch_pipeline_requests_create(
   pipeline.name, data,
   timeout = NULL, notification.group = NULL
)

# Or provide directly
result <- ubiops::batch_pipeline_requests_create(
   pipeline.name, data,
   timeout = NULL, notification.group = NULL, 
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
