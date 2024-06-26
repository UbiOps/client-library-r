% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/roles.R
\name{roles_get}
\alias{roles_get}
\title{Get details of a role}
\usage{
roles_get(role.name, preload_content = TRUE, ...)
}
\arguments{
\item{role.name}{character}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 Details of the role
  - `id`: Unique identifier for the role (UUID)
  - `name`: Name of the role
  - `default`: A boolean value that indicates whether the role is a default role or not
  - `permissions`: A list of permissions which the role contains
}
\description{
Get the details of a role. The user making the request must have appropriate permissions.
}
\examples{
\dontrun{
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::roles_get(
   role.name
)

# Or provide directly
result <- ubiops::roles_get(
   role.name,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
