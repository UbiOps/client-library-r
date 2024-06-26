# User

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create**](user.md#user_create) | **POST** /user | Create a new user
[**user_delete**](user.md#user_delete) | **DELETE** /user | Delete user


# **user_create**
> user_create(data)

Create a new user

## Description
Create a new user with the given details. After creation, an email is send to the email address to activate the account. The password needs to be at least 8 characters long.

### Required Parameters

- `email`: Email of the user
- `password`: Password of the user

### Optional Parameters

- `name`: Name of the user
- `surname`: Surname of the user
- `phone`: Phone number of the user

## Request Examples

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
  "phone": "+999999999"
}
```


```
{
  "email": "test@example.com",
  "password": "secret-password"
}
```

### Response Structure
Details of the created user

- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user
- `phone`: Phone number of the user

## Response Examples

```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname",
  "phone": "+999999999"
}
```

### Example
```R
data <- list(
  email = "email",
  password = "password",
  name = "name",  # (optional)
  surname = "surname",  # (optional)
  phone = "phone"  # (optional)
)

# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
result <- ubiops::user_create(
  data
)

# Or provide directly
result <- ubiops::user_create(
  data,
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

print(result)

# Or print in JSON format
print(jsonlite::toJSON(result, auto_unbox=TRUE))

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```

# **user_delete**
> user_delete()

Delete user

## Description
Delete the user that makes the request

### Example
```R
# Use environment variables
Sys.setenv("UBIOPS_API_TOKEN" = "YOUR API TOKEN")
ubiops::user_delete()

# Or provide directly
ubiops::user_delete(
  UBIOPS_API_TOKEN = "YOUR API TOKEN"
)

# The default API url is https://api.ubiops.com/v2.1
# Want to use a different API url? Provide `UBIOPS_API_URL`, either directly or as environment variable.
```


