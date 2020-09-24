from platron.request.clients import PostClient
from platron.request.request_builders import PsListBuilder

from .base_integration_test import BaseIntegrationTest


class PsListTest(BaseIntegrationTest):

    def test_ps_list(self):
        builder = PsListBuilder('10.00')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())

        self.assertIsNotNone(client.request(builder))
