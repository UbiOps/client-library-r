% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/organizations.R
\name{organizations_usage_get}
\alias{organizations_usage_get}
\title{Get organization usage}
\usage{
organizations_usage_get(
  organization.name,
  start.date = NULL,
  end.date = NULL,
  interval = "month",
  preload_content = TRUE,
  ...
)
}
\arguments{
\item{organization.name}{character}

\item{start.date}{(optional) character}

\item{end.date}{(optional) character}

\item{interval}{(optional) character}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 - `interval`: Interval for the usage data
  - `data_organization`: A list of dictionaries containing the organization usage for the given date range
  - `data_projects`: A list of dictionaries containing the usage of each project in the organization for the given date range
  - `data_projects_deleted`: A list of dictionaries containing the usage corresponds to deleted projects in the organization for the given date range
}
\description{
Get credits usage for the organization
}
\examples{
\dontrun{
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::organizations_usage_get(
   organization.name,
   start.date = NULL, end.date = NULL, interval = 'month'
)

# Or provide directly
result <- ubiops::organizations_usage_get(
   organization.name,
   start.date = NULL, end.date = NULL, interval = 'month', 
   UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
