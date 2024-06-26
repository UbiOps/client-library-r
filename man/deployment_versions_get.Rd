% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/deployments.R
\name{deployment_versions_get}
\alias{deployment_versions_get}
\title{Get deployment version}
\usage{
deployment_versions_get(deployment.name, version, preload_content = TRUE, ...)
}
\arguments{
\item{deployment.name}{character}

\item{version}{character}

\item{preload_content}{(optional) Whether the API response should be preloaded. When TRUE the JSON response string is parsed to an R object. When FALSE, unprocessed API response object is returned. - Default = TRUE}

\item{...}{UBIOPS_PROJECT (system environment variable) UbiOps project name
UBIOPS_API_TOKEN (system environment variable) Token to connect to UbiOps API
UBIOPS_API_URL (optional - system environment variable) UbiOps API url - Default = "https://api.ubiops.com/v2.1"
UBIOPS_TIMEOUT (optional - system environment variable) Maximum request timeout to connect to UbiOps API - Default = NA
UBIOPS_DEFAULT_HEADERS (optional - system environment variable) Default headers to pass to UbiOps API, formatted like "header1:value1,header2:value2" - Default = ""}
}
\value{
Response from the API
 Details of a version
  - `id`: Unique identifier for the version (UUID)
  - `deployment`: Deployment name to which the version is associated
  - `version`: Version name
  - `default`: A boolean indicating whether the version is the default version
  - `description`: Description of the version
  - `environment`: Environment of the version
  - `environment_display_name`: Human readable name of the environment
  - `status`: The status of the version
  - `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
  - `latest_revision`: UUID of the latest build of the version. If no deployment files have been uploaded yet, it is None.
  - `instance_type`: The reserved instance type for the version
  - `maximum_instances`: Upper bound of number of deployment pods running in parallel
  - `minimum_instances`: Lower bound of number of deployment pods running in parallel
  - `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
  - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
  - `creation_date`: The date when the version was created
  - `last_updated`: The date when the version was last updated
  - `last_file_upload`: The date when a deployment file was last uploaded for the version
  - `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
  - `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
  - `request_retention_time`: Number of seconds to store requests to the version
  - `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
      - *none* - the requests will not be stored
      - *metadata* - only the metadata of the requests will be stored
      - *full* - both the metadata and input/output of the requests will be stored
  - `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
  - `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
  - `has_request_method`: Whether the latest build of the version has a 'request' method
  - `has_requests_method`: Whether the latest build of the version has a 'requests' method
  - `static_ip`: A boolean indicating whether the deployment version should get a static IP
  - `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption
  - `ports`: A list of ports to open up in the deployment
}
\description{
Retrieve details of a version of a deployment in a project
}
\examples{
\dontrun{
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::deployment_versions_get(
   deployment.name, version
)

# Or provide directly
result <- ubiops::deployment_versions_get(
   deployment.name, version,
   UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url?
# Provide `UBIOPS_API_URL`, either directly or as environment variable.
}
}
