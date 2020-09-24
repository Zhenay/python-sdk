import unittest

from platron.request.request_builders import DoCaptureBuilder


class DoCaptureBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = DoCaptureBuilder('343242')
        params = builder.get_params()

        self.assertEqual('343242', params.get('pg_payment_id'))
