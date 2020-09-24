import unittest

from platron.request.request_builders import RecurringSetScheduleBuilder
from platron.sdk_exception import SdkException


class RecurringSetScheduleBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RecurringSetScheduleBuilder('12345', '100')
        builder.add_template('2018-01-01 00:00:00', 'week', '10', '100')
        builder.add_dates({'1': '2018-10-10 00:00:00', '2': '2019-10-10 00:00:00'})

        params = builder.get_params()
        template = params.get('pg_template')
        dates = params.get('pg_dates')

        self.assertEquals('12345', params.get('pg_recurring_profile'))
        self.assertEquals('2018-01-01 00:00:00', template.get('pg_start_date'))
        self.assertEquals('week', template.get('pg_interval'))
        self.assertEquals('10', template.get('pg_period'))
        self.assertEquals('100', template.get('pg_max_periods'))
        self.assertEquals('2018-10-10 00:00:00', dates.get('1'));

        with self.assertRaises(SdkException):
            builder.add_template('2018-01-01 00:00:00', 'wrong_interval', '10', '100')
