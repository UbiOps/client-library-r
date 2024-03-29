% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/webhooks.R
\name{webhook_tests_get}
\alias{webhook_tests_get}
\title{Get webhook test}
\usage{
webhook_tests_get(test.id, preload_content = TRUE, ...)
}
\arguments{
\item{test.id}{character}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 Details of a test
  - `id`: Unique identifier for the test (UUID)
  - `status`: Status of the test. It can be one of the following: 'pending', 'completed' or 'failed'.
  - `error_message`: An error message explaining why the test has failed
}
\description{
Retrieve details of a webhook test in a project
}
\examples{
\dontrun{
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::webhook_tests_get(
   test.id
)

# Or provide directly
result <- ubiops::webhook_tests_get(
   test.id,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
