import utils

DEFAULT_API_VERSION = 2.6


class MessengerGraphAPI:
    def __init__(self, access_token, **kwargs):
        self.api_version = kwargs.get('api_version', DEFAULT_API_VERSION)
        self.app_secret = kwargs.get('app_secret', None)
        self.graph_url = 'https://graph.facebook.com/v{0}'.format(self.api_version)
        self.access_token = access_token

    def check_updates(self):
        pass
