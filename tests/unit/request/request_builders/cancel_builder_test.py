import unittest

from platron.request.request_builders import CancelBuilder


class CancelBuilderTest(unittest.TestCase):

    def test_get_parameters(self):
        builder = CancelBuilder('363654')
        params = builder.get_params()

        self.assertEqual('363654', params.get('pg_payment_id'))
