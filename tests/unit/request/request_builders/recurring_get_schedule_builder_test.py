import unittest

from platron.request.request_builders import RecurringGetScheduleBuilder


class RecurringGetScheduleBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RecurringGetScheduleBuilder('12345')

        params = builder.get_params()
        self.assertEquals('12345', params.get('pg_recurring_profile'))
