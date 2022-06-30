# Blobs

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_create**](blobs.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](blobs.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](blobs.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](blobs.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**blobs_update**](blobs.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob


# **blobs_create**
> blobs_create(file, blob.ttl=NULL)

Upload a blob

## Description
Upload a blob to a project. The uploaded blob file can be retrieved by passing the blob_id. The returned blob_id may be passed in a deployment or pipeline request as input.

### Optional Parameters
These parameters should be given in the header.

- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds. The default value is 86400 seconds (1 day).

### Response Structure
The details of the uploaded blob

- `id`: Unique identifier for the blob (UUID)
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
}}
```

### Example
```R
file <- file.path("path", "to", "file")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::blobs_create(
  file,
  blob.ttl = NULL
)

# Or provide directly
result <- ubiops::blobs_create(
  file,
  blob.ttl = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **blobs_delete**
> blobs_delete(blob.id)

Delete a blob

## Description
Delete a blob from a project

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::blobs_delete(
  blob.id
)

# Or provide directly
ubiops::blobs_delete(
  blob.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **blobs_get**
> blobs_get(blob.id)

Get a blob

## Description
Download a blob file in a project

### Response Structure

- `file`: Blob file

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::blobs_get(
  blob.id
)

# Or provide directly
result <- ubiops::blobs_get(
  blob.id,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# Save file manually
file_name <- result$getFileName()

output <- file(file.path(getwd(), file_name), "wb")
readr::write_file(result$getContent(), output)
close(output)

# Or save file directly in temp folder
# by using environment variables or providing directly
Sys.setenv("UBIOPS_TEMP_FOLDER_PATH" = getwd())
output_path <- ubiops::blobs_get(
  blob.id,
  preload_content=TRUE
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **blobs_list**
> blobs_list(range=NULL, creation.date=NULL)

List blobs

## Description
List all blobs in a project

### Optional Parameters
These parameters should be given as GET parameters.

- `range`: Number of blobs to be returned. It may be a positive or a negative value. If it is positive, blobs uploaded starting from the creation_date towards the present time are returned. Otherwise, blobs uploaded towards the past are returned. The default value is -50.
- `creation_date`: Get the blobs uploaded starting from this date. If it is not provided, the uploaded blobs are returned according to the *range* parameter. It should be provided in year-month-day hour:minute:second format.

### Response Structure
A list of details of the blobs in the project

- `id`: Unique identifier for the blob (UUID)
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename.jpg",
    "size": 562,
    "ttl": 12338
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename2.jpg",
    "size": 3439,
    "ttl": 86400
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::blobs_list(
  
  range = NULL, creation.date = NULL
)

# Or provide directly
result <- ubiops::blobs_list(
  
  range = NULL, creation.date = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **blobs_update**
> blobs_update(blob.id, file, blob.ttl=NULL)

Update a blob

## Description
Overwrite a blob with given blob id. The uploaded blob file can be retrieved by passing the blob_id.

### Optional Parameters
These parameters should be given in the header.

- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds. The default value is 86400 seconds (1 day).

### Response Structure
The details of the uploaded blob

- `id`: Unique identifier for the blob (UUID)
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
}}
```

### Example
```R
file <- file.path("path", "to", "file")

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::blobs_update(
  blob.id, file,
  blob.ttl = NULL
)

# Or provide directly
result <- ubiops::blobs_update(
  blob.id, file,
  blob.ttl = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


