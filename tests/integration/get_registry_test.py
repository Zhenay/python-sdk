from platron.request.clients import PostClient
from platron.request.request_builders import GetRegistryBuilder

from .base_integration_test import BaseIntegrationTest


class GetStatusTest(BaseIntegrationTest):

    def test_create_transaction_chain(self):
        client = PostClient(self.get_merchant_id(), self.get_secret_key())
        builder = GetRegistryBuilder('2017-01-01')

        self.assertIsNotNone(client.request(builder))
