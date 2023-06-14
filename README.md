# Python SMBC GMO Pay Client Lib
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMonoidDev%2Fsmbc-gp-client.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FMonoidDev%2Fsmbc-gp-client?ref=badge_shield)

An http client to call SMBC GMO Pay APIs. (smbc-gp-client)

## Upload package
```
python3 -m pip install --user --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

## How to use
use pip install package `smbc-gp-client`
```
pip3 install smbc-gp-client
```
in your code:
```python
from smbc_gp_client.smbc_gp_client import SmbcGpClient

client = SmbcGpClient()
client.create_transation(...)
client.execute_transaction(...)
```
for more details, please refer to `SmbcGpClient` class method description.

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMonoidDev%2Fsmbc-gp-client.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FMonoidDev%2Fsmbc-gp-client?ref=badge_large)

## Reference
- SMBC GMO PAYMENT https://www.smbc-gp.co.jp/
