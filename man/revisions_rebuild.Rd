% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/deployments.R
\name{revisions_rebuild}
\alias{revisions_rebuild}
\title{Rebuild revision}
\usage{
revisions_rebuild(
  deployment.name,
  revision.id,
  version,
  data,
  preload_content = TRUE,
  ...
)
}
\arguments{
\item{deployment.name}{character}

\item{revision.id}{character}

\item{version}{character}

\item{data}{list(key = "value") - Example: list(input_field_1 = "input_value_1", input_field_2 = "input_value_2")}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 Details of the created revision
  - `id`: Unique identifier for the revision (UUID)
  - `version`: Version to which the revision is linked
  - `creation_date`: The date when the revision was created
  - `created_by`: The email of the user that created the revision
  - `status`: Status of the revision
  - `error_message`: Error message which explains why the revision has failed. It is empty if the revision is successful.
  - `has_request_method`: Whether the deployment code corresponding to the revision has a 'request' method
  - `has_requests_method`: Whether the deployment code corresponding to the revision has a 'requests' method
}
\description{
Trigger a rebuild for a revision of a deployment
}
\examples{
\dontrun{
data <- list(input_field_1 = "input_value_1", input_field_2 = "input_value_2")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::revisions_rebuild(
   deployment.name, revision.id, version, data
)

# Or provide directly
result <- ubiops::revisions_rebuild(
   deployment.name, revision.id, version, data,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
