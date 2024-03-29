% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/deployment_requests.R
\name{deployment_requests_update}
\alias{deployment_requests_update}
\title{Update a deployment request}
\usage{
deployment_requests_update(
  deployment.name,
  request.id,
  data,
  preload_content = TRUE,
  ...
)
}
\arguments{
\item{deployment.name}{character}

\item{request.id}{character}

\item{data}{named list of: [ status (optional), notification_group (optional) ]}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
}
\description{
Update a deployment request for the default version of a deployment. It is possible to **cancel** a request by giving `cancelled` in the status field.
}
\examples{
\dontrun{
data <- list(
 status = "status",  # (optional)
 notification_group = "notification_group"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_requests_update(
   deployment.name, request.id, data
)

# Or provide directly
result <- ubiops::deployment_requests_update(
   deployment.name, request.id, data,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
