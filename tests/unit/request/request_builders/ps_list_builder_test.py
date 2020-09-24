import unittest

from platron.request.request_builders import PsListBuilder


class PsListBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = PsListBuilder('10.00')
        builder.add_currency('RUB')
        builder.add_testing_mode()

        parameters = builder.get_params()

        self.assertEqual('10.00', parameters.get('pg_amount'))
        self.assertEqual('RUB', parameters.get('pg_currency'))
        self.assertEqual(1, parameters.get('pg_testing_mode'))
