import sellsy_api


def test_can_access_to_sellsy_api_package():
    sellsy_api.Client


def test_can_access_to_sellsy_errors():
    sellsy_api.errors
    sellsy_api.errors.SellsyAuthenticateError
    sellsy_api.errors.SellsyError

