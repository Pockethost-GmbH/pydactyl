import logging
import unittest

from pydactyl.exceptions import ClientConfigError
from pydactyl import api_client


class ApiClientTests(unittest.TestCase):

    def test_pterodactyl_client_raises_without_required_params(self):
        with self.assertRaises(ClientConfigError):
            api_client.PterodactylClient(api_key='key', url=None)
        with self.assertRaises(ClientConfigError):
            api_client.PterodactylClient(api_key=None, url='url')

    def test_pterodactyl_client_debug_param(self):
        logger = logging.getLogger()
        self.assertEqual(logging.ERROR, logger.level)
        api_client.PterodactylClient('foo', 'bar', debug=True)
        self.assertEqual(logging.DEBUG, logger.level)
        api_client.PterodactylClient('foo', 'bar', debug=False)
        self.assertEqual(logging.ERROR, logger.level)

    def test_optional_request_timeout_preserves_default_and_explicit_override(self):
        from unittest.mock import patch
        import requests

        default = api_client.PterodactylClient('https://panel.invalid', 'test')
        self.assertIs(type(default._session), requests.Session)
        bounded = api_client.PterodactylClient('https://panel.invalid', 'test', retries=0, timeout=(5, 30))
        with patch.object(requests.Session, 'request') as request:
            bounded._session.get('https://panel.invalid/api/application/nodes')
            self.assertEqual(request.call_args.kwargs['timeout'], (5, 30))
            bounded._session.get('https://panel.invalid/api/application/nodes', timeout=2)
            self.assertEqual(request.call_args.kwargs['timeout'], 2)
        self.assertEqual(bounded._session.adapters['https://'].max_retries.total, 0)
