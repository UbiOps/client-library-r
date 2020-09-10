# ubiops
Client Library to interact with the UbiOps API (v2.1).

For more information, please visit [https://docs.ubiops.com/](https://docs.ubiops.com/)

## Requirements.

Python 3.5+

## Installation

```sh
pip install ubiops
```

## Usage
To use the library one has to authenticate to the UbiOps API with an API token. 
Please, visit https://docs.ubiops.com/docs/service-users for more information. 

```python
import ubiops

configuration = ubiops.Configuration()
configuration.api_key['Authorization'] = 'Token <YOUR_API_KEY>'

client = ubiops.ApiClient(configuration)

api = ubiops.api.CoreApi(client)
print(api.service_status())
```

## Documentation
The library is fully documented at https://github.com/UbiOps/client-library-python/tree/master/docs.


## Examples
Jupyter notebook examples can be found at https://github.com/UbiOps/client-library-python/tree/master/examples.

## License
Ubiops is available under the Apache 2.0 license.
