from xml.etree.ElementTree import fromstring

from platron.request.clients import PostClient
from platron.request.request_builders import (GetStatusBuilder,
                                              InitPaymentBuilder)

from .base_integration_test import BaseIntegrationTest


class GetStatusTest(BaseIntegrationTest):

    def test_create_transaction_chain(self):
        client = PostClient(self.get_merchant_id(), self.get_secret_key())
        builder = InitPaymentBuilder('10.00', 'test')
        result = client.request(builder)
        root = fromstring(result)
        pg_payment_id = root.find('pg_payment_id').text

        builder = GetStatusBuilder(pg_payment_id)

        self.assertIsNotNone(client.request(builder))
