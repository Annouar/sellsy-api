
# sellsy-api
> A tiny client to manage your Sellsy plateform using Python

sellsy-api is a client for the official [Sellsy API](https://api.sellsy.com) in order to allow you to get and manipulate data from [Sellsy plateform](https://welcome.sellsy.com/). The official client was written in PHP, here is a client written in pure python.

### Features
- Allows you to connect with your Oauth private API keys
- Access to all methods listed [here](https://api.sellsy.com/documentation/methods) with only a single function
- Error handler

### Requirements
* [Python 2/3](https://www.python.org/),
* A Python Package Manager ([pip](https://pip.pypa.io/en/stable/installing/), [pipenv](http://pipenv.readthedocs.io/en/latest/), [conda](https://conda.io/docs/), ..)


## Installing

If you are using pip as PM:

```shell
# Connect to your virtualenv
$  workon projectenv

# Use pip to install the package
$  pip install sellsy_api
```

Or if you are using pipenv (pip needs to be installed too):
```shell

$  cd /path/to/my/project
$  pipenv install sellsy_api
```

Verify now if the package as been successfully installed
```shell
$  python
>> import sellsy_api # Should not raise exception
```

## Quick Start

```python
import os
import sellsy_api

client = sellsy_api.Client(
    'my_consumer_token',
    'my_consumer_secret',
    'my_user_token',
    'my_user_secret')

try:
    infos = client.api(method='Infos.getInfos')
    prospect = client.api(method='Prospects.getOne', params={ 'id': 55 })
except sellsy_api.SellsyAuthenticateError as e: # raised if credential keys are not valid
    print('Authentication failed ! Details : {}'.format(e))
except sellsy_api.SellsyError as e: # raised if an error is returned by Sellsy API (
    print(e)
    
prospect_name = prospect['corporation']['name']
         
```

You can access the full Sellsy API [methods](https://api.sellsy.com/documentation/methods) using `client.api(method='', params={})`. 

The function returns a dictionary containing the response:
```json
{
   "corporation":{
      "id":"55",
      "corpid":"644",
      "name":"New Prospect",
      "...":"...",
      "created":"2013-01-31 14:49:35",
      "updated":"2013-01-31 16:41:38"
   },
   "contacts":[
      {
         "id":"44",
         "prospectid":"55",
         "...":"...",
         "sign":"",
         "birthdate":"0000-00-00"
      }
   ]
}
```

For now, two exceptions could be raised by calling the function:
- `SellsyAuthenticateError` : if one of `consumer_key`, `consumer_secret`, `user_token` or `user_secret` is invalid or if authentication failed
- `SellsyError`: Sellsy API could return error depends on unexcistant ressource or method not valid for example. So this exception is raised and you can access the exception infos to have more details or error : `{code} - {detail}` where `code` if one of code error described [here](https://api.sellsy.com/documentation/errors) (in Error Process tab).
- _COMING SOON_: more exceptions to catch precise errors through distinct exceptions (example: SellsyRessourceNotFound if the ressource you asked for does not exists) and not only through a unique `SellsyError` with different messages... 


## Links

- [Sellsy plateform](https://welcome.sellsy.com/)
- [Sellsy API](https://api.sellsy.com)
- [sellsy-api issue tracker](https://github.com/Annouar/sellsy-client/issues)


## License

 - **MIT** : http://opensource.org/licenses/MIT