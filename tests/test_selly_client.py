import os
import pytest
import sellsy_api

consumer_token = os.environ.get('SELLSY_CONSUMER_TOKEN')
consumer_secret = os.environ.get('SELLSY_CONSUMER_SECRET')
user_token = os.environ.get('SELLSY_USER_TOKEN')
user_secret = os.environ.get('SELLSY_USER_SECRET')


def make_credential_incorrect(credential):
    '''
    Allow you to falsify a credential by adding some characters

    :param credential: The credential to falsify
    '''
    return credential + '__'


@pytest.fixture(params=[
    {
        'consumer_token': make_credential_incorrect(consumer_token),
        'consumer_secret': consumer_secret,
        'user_token': user_token,
        'user_secret': user_secret
    },
    {
        'consumer_token': consumer_token,
        'consumer_secret': make_credential_incorrect(consumer_secret),
        'user_token': user_token,
        'user_secret': user_secret
    },
    {
        'consumer_token': consumer_token,
        'consumer_secret': consumer_secret,
        'user_token': make_credential_incorrect(user_token),
        'user_secret': user_secret
    },
    {
        'consumer_token': consumer_token,
        'consumer_secret': consumer_secret,
        'user_token': user_token,
        'user_secret': make_credential_incorrect(user_token)
    }
])


def bad_client(request):
    return sellsy_api.Client(
        request.param['consumer_token'],
        request.param['consumer_secret'],
        request.param['user_token'],
        request.param['user_secret'])


def test_oauth_bad_credentials(bad_client):
    with pytest.raises(sellsy_api.SellsyAuthenticateError):
        bad_client.api(method='Infos.getInfos')


@pytest.fixture(autouse=True, scope='session')
def client():
    return sellsy_api.Client(
        consumer_token,
        consumer_secret,
        user_token,
        user_secret)


def test_client_is_instantiated(client):
    assert isinstance(client, sellsy_api.Client)


def test_client_is_working_without_error(client):
    try:
        client.api(method='Infos.getInfos')
    except Exception as e:
        error_code, error_message = e.__class__.__name__, e
        pytest.fail('Client has raised an unexcepted error ({}: {})'.format(error_code, error_message))


def test_client_returns_dict(client):
    infos = client.api(method='Infos.getInfos')
    assert isinstance(infos, dict)


def test_client_returns_exception_when_not_valid_method(client):
    not_valid_method = 'NotValid.Method'
    with pytest.raises(sellsy_api.SellsyError) as err:
        client.api(method=not_valid_method)
    err.match(r'E_METHOD_DONT_EXIT - Method {} does not exist'.format(not_valid_method))


def test_client_returns_exception_when_non_existing_item_id(client):
    with pytest.raises(sellsy_api.SellsyError) as err:
        client.api(method='Prospects.getOne', params={
            'id': -1
        })
    err.match(r'E_OBJ_NOT_LOADABLE - Object third not loadable')


def test_client_returns_exception_when_invalid_item_id(client):
    with pytest.raises(sellsy_api.SellsyError) as err:
        client.api(method='Prospects.getOne', params={
            'id': 'rr'
        })
    err.match(r'E_PARAM_INVALID - id is invalid')
