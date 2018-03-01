import pytest
from sellsy_api import SellsyAuthenticateError, SellsyError


def test_raise_SellsyAuthenticateError():
    with pytest.raises(SellsyAuthenticateError):
        raise SellsyAuthenticateError


def test_raise_SellsyError():
    with pytest.raises(SellsyError) as err:
        raise SellsyError('SellsyCodeError', 'message')
    err.match(r'SellsyCodeError - message')
