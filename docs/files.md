# Files

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buckets_create**](files.md#buckets_create) | **POST** /projects/{project_name}/buckets | Create bucket
[**buckets_delete**](files.md#buckets_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name} | Delete a bucket
[**buckets_get**](files.md#buckets_get) | **GET** /projects/{project_name}/buckets/{bucket_name} | Get details of a bucket
[**buckets_list**](files.md#buckets_list) | **GET** /projects/{project_name}/buckets | List buckets
[**buckets_update**](files.md#buckets_update) | **PATCH** /projects/{project_name}/buckets/{bucket_name} | Update a bucket
[**files_complete_multipart_upload**](files.md#files_complete_multipart_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file}/complete-multipart-upload | Complete multipart upload
[**files_delete**](files.md#files_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Delete a file
[**files_download**](files.md#files_download) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file}/download | Download a file
[**files_get**](files.md#files_get) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Get a file
[**files_list**](files.md#files_list) | **GET** /projects/{project_name}/buckets/{bucket_name}/files | List files
[**files_start_multipart_upload**](files.md#files_start_multipart_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file}/start-multipart-upload | Start multipart upload
[**files_upload**](files.md#files_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Upload a file


# **buckets_create**
> buckets_create(data)

Create bucket

## Description
Create a bucket in a project

### Required Parameters

- `name`: Name of the bucket. It is unique within a project.

### Optional Parameters

- `provider`: Provider of the bucket. It can be 'ubiops', 'google_cloud_storage', 'amazon_s3' or 'azure_blob_storage'. The default is **ubiops**.
- `credentials`: A dictionary for credentials to connect to the bucket. It is only required for providers other than *ubiops*. Each provider requires a different set of fields:
    - For Amazon S3, provide the fields `access_key` and `secret_key`.
    - For Azure Blob Storage, provide the field `connection_string` in the format: *DefaultEndpointsProtocol=https;AccountName=<account-name>;AccountKey=<account-key>;EndpointSuffix=core.windows.net*.
    - For Google Cloud Storage, provide the field `json_key_file`.
- `configuration`: A dictionary for additional configuration details for the bucket. It is only required for providers other than *ubiops*. Each provider requires a different set of fields:
    - For Amazon S3, provide the fields `bucket` and `prefix`. One of the fields `region` or `endpoint_url` needs to be provided. The fields `signature_version`, `verify` and `use_ssl` are optional.
    - For Azure Blob Storage, provide the fields `container` and `prefix`.
    - For Google Cloud Storage, provide the fields `bucket` and `prefix`.
    UbiOps always makes sure that the prefix ends with a '/'.
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket. It must be a multiple of 604800 (1 week). Pass `null` to keep them forever.

## Request Examples

```
{
  "name": "bucket-1",
  "provider": "ubiops",
  "credentials": {},
  "configuration": {},
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description"
}
```

### Response Structure
Details of the created bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is created
- `provider`: Provider of the bucket
- `credentials`: Credentials to connect to the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "bucket-1",
  "project": "project-1",
  "provider": "ubiops",
  "credentials": {},
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null
}
```

### Example
```R
data <- list(
  name = "name",
  provider = "provider",
  credentials = list(key = "value"),  # (optional)
  configuration = list(key = "value"),  # (optional)
  ttl = 0,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::buckets_create(
  data
)

# Or provide directly
result <- ubiops::buckets_create(
  data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **buckets_delete**
> buckets_delete(bucket.name)

Delete a bucket

## Description
Delete a bucket. If the bucket provider is UbiOps, the files in the bucket will be deleted together with the bucket. For other providers, the files in the bucket are not removed but just the connection from UbiOps to the bucket.

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::buckets_delete(
  bucket.name
)

# Or provide directly
ubiops::buckets_delete(
  bucket.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **buckets_get**
> buckets_get(bucket.name)

Get details of a bucket

## Description
Retrieve details of a bucket in a project

### Response Structure
Details of a bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket
- `size`: Size of the bucket according to the last measurement date
- `size_measurement_date`: Last measurement date of the size of the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "bucket-1",
  "project": "project-1",
  "provider": "ubiops",
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null,
  "size": 2048,
  "size_measurement_date": "2022-05-24T02:23:15.456812Z",
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::buckets_get(
  bucket.name
)

# Or provide directly
result <- ubiops::buckets_get(
  bucket.name,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **buckets_list**
> buckets_list(labels=NULL)

List buckets

## Description
List buckets in a project

### Optional Parameters

- `labels`: Filter on labels of the buckets. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). Buckets that have at least one of the labels in the filter are returned. This parameter should be given as query parameter.

### Response Structure
A list of details of the buckets in the project

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket

## Response Examples

```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "bucket-1",
    "project": "project-1",
    "provider": "ubiops",
    "creation_date": "2022-05-12T16:23:15.456812Z",
    "configuration": {},
    "labels": {
      "type": "bucket"
    },
    "description": "My bucket description",
    "ttl": null
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "bucket-2",
    "project": "project-1",
    "provider": "ubiops",
    "creation_date": "2022-05-12T16:23:15.456812Z",
    "configuration": {},
    "labels": {},
    "description": "My bucket 2 description",
    "ttl": null
  }
]
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::buckets_list(
  
  labels = NULL
)

# Or provide directly
result <- ubiops::buckets_list(
  
  labels = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **buckets_update**
> buckets_update(bucket.name, data)

Update a bucket

## Description
Update a bucket

### Optional Parameters

- `credentials`: Credentials to connect to the bucket
- `configuration`: Additional configuration details for the bucket
- `description`: New description for the bucket
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `ttl`: Time to live for the files in the bucket. It must be a multiple of 604800 (1 week).

## Request Examples

```
{
  "description": "New description for the bucket"
}
```

### Response Structure
Details of the updated bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket
- `size`: Size of the bucket according to the last measurement date
- `size_measurement_date`: Last measurement date of the size of the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-bucket-name",
  "project": "project-1",
  "provider": "ubiops",
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null,
  "size": 2048,
  "size_measurement_date": "2022-05-24T02:23:15.456812Z",
}
```

### Example
```R
data <- list(
  credentials = list(key = "value"),  # (optional)
  configuration = list(key = "value"),  # (optional)
  ttl = 0,  # (optional)
  description = "description",  # (optional)
  labels = list(key = "value")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::buckets_update(
  bucket.name, data
)

# Or provide directly
result <- ubiops::buckets_update(
  bucket.name, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_complete_multipart_upload**
> files_complete_multipart_upload(bucket.name, file, data)

Complete multipart upload

## Description
Complete a multipart upload for a file

### Request Structure
- `parts`: A list of parts that were uploaded

## Request Examples

```
{
  "parts": [
    {
      "ETag": "etag-2",
      "PartNumber": 1
    },
    {
      "ETag": "etag-2",
      "PartNumber": 2
    }
  ]
}
```

### Response Structure

- `upload_id`: ID of the uploaded for the file
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "upload_id": "upload-id",
  "provider": "google_cloud_storage"
}
```

### Example
```R
data <- list(
  upload_id = "upload_id",  # (optional)
  parts = list("value-1", "value-2")  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_complete_multipart_upload(
  bucket.name, file, data
)

# Or provide directly
result <- ubiops::files_complete_multipart_upload(
  bucket.name, file, data,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_delete**
> files_delete(bucket.name, file)

Delete a file

## Description
Delete a file from a bucket

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::files_delete(
  bucket.name, file
)

# Or provide directly
ubiops::files_delete(
  bucket.name, file,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_download**
> files_download(bucket.name, file)

Download a file

## Description
Generate a signed url to download a file. Request body should be an empty dictionary.

### Response Structure

- `url`: A url which can be used to download the file from bucket. Make a GET request to this url to download the file.
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "url": "https://storage.apis.com/my-bucket/my-file.jpg...",
  "provider": "ubiops"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_download(
  bucket.name, file
)

# Or provide directly
result <- ubiops::files_download(
  bucket.name, file,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_get**
> files_get(bucket.name, file)

Get a file

## Description
Get the details of a file in the bucket

### Response Structure

- `file`: Name of the file
- `size`: Size of the file
- `time_created`: The time that the file was created

## Response Examples

```
{
  "file": "my-file-1",
  "size": 123,
  "time_created": "2022-05-12T16:23:15.456812Z"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_get(
  bucket.name, file
)

# Or provide directly
result <- ubiops::files_get(
  bucket.name, file,
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_list**
> files_list(bucket.name, prefix=NULL, delimiter=NULL, continuation.token=NULL, limit=NULL)

List files

## Description
List files in a bucket

### Optional Parameters
The following parameters should be given as query parameters:

- `prefix`: Prefix to filter files
- `delimiter`: Delimiter used with prefix to emulate hierarchy to filter files
- `limit`: The maximum number of files returned, default is 100
- `continuation_token`: A token that indicates the start point of the returned the files

### Response Structure
A dictionary containing the details of files and prefixes in the bucket

- `continuation_token`: Next token to get the next set of files
- `files`: A list of dictionaries containing the details of the files. It contains the file name ('file'), size of the file ('size') and the creation time of the file ('time_created').
- `prefixes`: A list of directories

## Response Examples

```
{
  "continuation_token": "1234",
  "files": [
    {
      "file": "my-file-1",
      "size": 123,
      "time_created": "2022-05-12T16:23:15.456812Z"
    },
    {
      "file": "my-file-2",
      "size": 456,
      "time_created": "2022-06-05T10:56:12.186046Z"
    }
  ],
  "prefixes": [
    "my-dir-1",
    "my-dir-2"
  ]
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_list(
  bucket.name,
  prefix = NULL, delimiter = NULL, continuation.token = NULL, limit = NULL
)

# Or provide directly
result <- ubiops::files_list(
  bucket.name,
  prefix = NULL, delimiter = NULL, continuation.token = NULL, limit = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_start_multipart_upload**
> files_start_multipart_upload(bucket.name, file, data=NULL)

Start multipart upload

## Description
Start a multipart upload for a file

### Response Structure

- `upload_id`: ID of the upload for the file
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "upload_id": "upload-id",
  "provider": "google_cloud_storage"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_start_multipart_upload(
  bucket.name, file,
  data = NULL
)

# Or provide directly
result <- ubiops::files_start_multipart_upload(
  bucket.name, file,
  data = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **files_upload**
> files_upload(bucket.name, file, upload.id=NULL, part.number=NULL, data=NULL)

Upload a file

## Description
Generate a signed url to upload a file. Request body should be an empty dictionary.

Note: When using the url generated by this endpoint for Azure Blob Storage, the following headers must be added to the upload request to Azure Blob Storage:
- `x-ms-version`: '2020-04-08'
- `x-ms-blob-type`: 'BlockBlob'

### Optional Parameters

- `upload_id`: ID of the upload for the file. It should be used with multipart uploads.
- `part_number`: Part number of the upload. It should be used with multipart uploads.

### Response Structure

- `url`: A url which can be used to upload the file to bucket. Make a PUT request to this url with the file content to upload the file.
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "url": "https://storage.apis.com/my-bucket/my-file.jpg...",
  "provider": "ubiops"
}
```

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_PROJECT" = "YOUR PROJECT NAME")
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::files_upload(
  bucket.name, file,
  upload.id = NULL, part.number = NULL, data = NULL
)

# Or provide directly
result <- ubiops::files_upload(
  bucket.name, file,
  upload.id = NULL, part.number = NULL, data = NULL, 
  UBIOPS_PROJECT = "YOUR PROJECT NAME", UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


