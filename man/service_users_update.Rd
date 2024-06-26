% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/service_users.R
\name{service_users_update}
\alias{service_users_update}
\title{Update service user details}
\usage{
service_users_update(service.user.id, data, preload_content = TRUE, ...)
}
\arguments{
\item{service.user.id}{character}

\item{data}{named list of: [ name (optional), expiry_date (optional) ]}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 Details of the updated service user
  - `id`: Unique identifier for the service user (UUID)
  - `email`: Email of the service user
  - `name`: Name of the service user
  - `creation_date`: Date when the service user was created
  - `expiry_date`: Date when the service user account will expire (UTC)
}
\description{
Update the name, expiry date and cors allowed origins of a service user. The new value for the cors_allowed_origin will replace the old value. Leave as an empty list to remove the previous list of allowed origins.  It is not possible to update a service user whose expiry date has been reached.
}
\examples{
\dontrun{
data <- list(
 name = "name",  # (optional)
 expiry_date = expiry_date  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_users_update(
   service.user.id, data
)

# Or provide directly
result <- ubiops::service_users_update(
   service.user.id, data,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
