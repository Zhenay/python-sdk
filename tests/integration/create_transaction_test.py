from platron.request.clients import PostClient
from platron.request.request_builders import InitPaymentBuilder

from .base_integration_test import BaseIntegrationTest


class CreateTransactionTest(BaseIntegrationTest):

    def test_create_transaction(self):
        builder = InitPaymentBuilder('10.00', 'test')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())

        self.assertIsNotNone(client.request(builder))
