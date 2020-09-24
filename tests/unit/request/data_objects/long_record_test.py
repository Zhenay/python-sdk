import unittest
from unittest.mock import MagicMock, Mock

from platron.request.data_objects import LongRecord, TripLeg


class LongRecordTest(unittest.TestCase):

    def test_get_parameters(self):
        data_object = LongRecord('alexey lashnev', 'FFF666', '1')
        data_object.set_agency_code('F')
        data_object.set_ticket_system('GAT')

        tripleg_stub = Mock(spec=TripLeg)
        tripleg_stub.get_params = MagicMock(return_value={'long_record_test': 'long_record_test'})

        data_object.add_tripleg(tripleg_stub)

        params = data_object.get_params()

        self.assertEqual('alexey lashnev', params.get('pg_ticket_passenger_name'))
        self.assertEqual('FFF666', params.get('pg_ticket_number'))
        self.assertEqual('1', params.get('pg_ticket_restricted'))
        self.assertEqual('F', params.get('pg_ticket_agency_code'))
        self.assertEqual('GAT', params.get('pg_ticket_system'));
        self.assertEqual('long_record_test', params.get('long_record_test'));
