import unittest

from platron.request.request_builders import GetBinInfoBuilder


class GetBinInfoBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = GetBinInfoBuilder('444555')
        params = builder.get_params()

        self.assertEqual('444555', params.get('pg_bin'))
