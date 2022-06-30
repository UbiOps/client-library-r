# Status

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_status**](status.md#service_status) | **GET** /status | Service status


# **service_status**
> service_status()

Service status

## Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure

- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

## Response Examples

```	
{
  "status": "ok"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::service_status()

# Or provide directly
result <- ubiops::service_status(
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


