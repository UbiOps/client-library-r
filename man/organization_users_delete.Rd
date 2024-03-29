% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/organizations.R
\name{organization_users_delete}
\alias{organization_users_delete}
\title{Delete a user from an organization}
\usage{
organization_users_delete(organization.name, user.id, ...)
}
\arguments{
\item{organization.name}{character}

\item{user.id}{character}

\item{...}{UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
}
\description{
Delete a user from an organization. The user making the request must be admin of the organization. It is not possible to delete the last admin of an organization.  **When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**
}
\examples{
\dontrun{
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::organization_users_delete(
   organization.name, user.id
)

# Or provide directly
ubiops::organization_users_delete(
   organization.name, user.id,
   UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
