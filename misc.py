from errors import HttpError
from utils import URIHandler
from base import base


def subscribe_app():
    subscription_endpoint = '/me/subscription'
    subscribe_uri = URIHandler(subscription_endpoint).configure()
    request = base.exec_request('POST', subscribe_uri)
    if request:
        return request
    else:
        raise HttpError('Unable to complete request.')


def validate_webhook(**kwargs):
    validation_endpoint = 'subscriptions_sample'
    validation_uri = URIHandler(validation_endpoint).configure(uri_format='appIDFirst', request_args=kwargs)
    request = base.exec_request('POST', validation_uri)
    if request:
        return request
    else:
        raise HttpError('Unable to complete request.')