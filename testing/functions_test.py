from unittest import TestCase, main, mock
from parameterized import parameterized
import datetime as dt
import src.functions as util
import sys
import os

sys.path.append(os.pardir)
sys.path.append(os.path.join(os.pardir, os.pardir))


# Use of a built-in testing library of python


# Author: Carlos Carvajal


# Unit testing of classes and function written in this project

class TestParseTimeStringToDatetime(TestCase):
    @mock.patch('src.functions.parse_time_string_to_datetime')
    def test_parse_time_string_to_datetime(self, mock_parse_time_string_to_datetime):

        mock_parse_time_string_to_datetime.return_value = dt.datetime.now()

        time_string = '10:00'

        time_datetime = util.parse_time_string_to_datetime(time_string)

        self.assertTrue(isinstance(time_datetime, dt.datetime))

    def test_random(self):

        time_string = '10:00'

        time_datetime = util.parse_time_string_to_datetime(time_string)

        self.assertTrue(isinstance(time_datetime, dt.datetime))


class TestParseScheduleToDict(TestCase):
    # Test parametrizado:
    # cada lista va a ser un record (input, output)
    @parameterized.expand([
        ['TH10:00-16:00,WE10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
         {'TH': {'start_time': '01:00', 'end_time': '03:00'},
          'WE': {'start_time': '10:00', 'end_time': '12:00'},
          'SA': {'start_time': '14:00', 'end_time': '18:00'},
          'SU': {'start_time': '20:00', 'end_time': '21:00'}}
         ],
        ['TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
         {'TH': {'start_time': '01:00', 'end_time': '03:00'},
          'SA': {'start_time': '14:00', 'end_time': '18:00'},
          'SU': {'start_time': '20:00', 'end_time': '21:00'}}]
    ])
    def test_parse_schedule_to_dict(self, schedule_string, schedule_dict):

        dict_parsed_from_string = util.parse_schedule_string_to_dict(
            schedule_string)

        self.assertEqual(dict_parsed_from_string,
                         schedule_dict, 'They should be the same!')


class TestCompareSchedules(TestCase):
    @parameterized.expand([
        [{'TH': {'start_time': '01:00', 'end_time': '03:00'},
          'WE': {'start_time': '10:00', 'end_time': '12:00'},
          'SA': {'start_time': '14:00', 'end_time': '18:00'},
          'SU': {'start_time': '20:00', 'end_time': '21:00'}},
         {'TH': {'start_time': '02:00', 'end_time': '04:00'},
          'WE': {'start_time': '09:00', 'end_time': '12:00'}},
          2
         ],
        [{'TH': {'start_time': '02:00', 'end_time': '04:00'},
          'WE': {'start_time': '09:00', 'end_time': '12:00'}},
         {'SA': {'start_time': '09:00', 'end_time': '18:00'},
          'SU': {'start_time': '09:00', 'end_time': '21:00'}},
          0
         ]
    ])

    def test_calculate_times_coincided(self, schedule, other_schedule, coincided):

        # schedule1 = {'TH': {'start_time': '01:00', 'end_time': '03:00'},
        #              'WE': {'start_time': '10:00', 'end_time': '12:00'},
        #              'SA': {'start_time': '14:00', 'end_time': '18:00'},
        #              'SU': {'start_time': '20:00', 'end_time': '21:00'}}
        # schedule2 = {'TH': {'start_time': '02:00', 'end_time': '04:00'},
        #              'WE': {'start_time': '09:00', 'end_time': '12:00'}}
        # schedule3 = {'SA': {'start_time': '09:00', 'end_time': '18:00'},
        #              'SU': {'start_time': '09:00', 'end_time': '21:00'}}
        times_coincided = util.calculate_times_coincided(schedule, other_schedule)

        self.assertEqual(times_coincided, coincided,
                         'There are {} times that employees are at the '
                         'same time in the office'.format(coincided))

    # def test_compare_with_one_empty_schedule(self):
    #     schedule = {}
    #     schedule2 = {'TH': {'start_time': '02:00', 'end_time': '04:00'},
    #                  'WE': {'start_time': '09:00', 'end_time': '12:00'}}

    #     self.assertEqual(util.calculate_times_coincided(schedule, schedule2), 0,
    #                      'There are 0 times that employees are at the '
    #                      'same time in the office')


# class TestIsAMatchTime(TestCase):
#     def test_hour_range_is_a_match_hour_range(self):
#         first_hr = {'start_time': '10:00', 'end_time': '12:00'}
#         second_hr = {'start_time': '10:15', 'end_time': '12:00'}
#         third_hr = {'start_time': '13:00', 'end_time': '16:00'}

#         self.assertTrue(util.is_a_coincided_hour_range(first_hr, second_hr), 'Is a match hour range (True)')
#         self.assertFalse(util.is_a_coincided_hour_range(first_hr, third_hr), 'Is not a match hour range (False)')


# class BuildEmployeeScheduleStruct(TestCase):
#     def test_build_employee_schedule_struct(self):
#         # final_struc --> fake data
#         final_struc = {'employee_name': 'CARLOS', 'data': {'TH': {'start_time': '01:00', 'end_time': '03:00'},
#                                                            'WE': {'start_time': '10:00', 'end_time': '12:00'},
#                                                            'SA': {'start_time': '14:00', 'end_time': '18:00'},
#                                                            'SU': {'start_time': '20:00', 'end_time': '21:00'}}}

#         employee_sch_struc = util.build_employee_schedule_struct('CARLOS', 'TH10:00-16:00,WE10:00-12:00,'
#                                                                            'TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')

#         self.assertEqual(employee_sch_struc, final_struc, 'They are the same!')

#     def test_build_employee_schedule_struct_with_empty_data(self):
#         employee_sch_struc = util.build_employee_schedule_struct('CARLOS', '')

#         final_struc = {'employee_name': 'CARLOS', 'data': {}}

#         self.assertEqual(employee_sch_struc, final_struc, 'They are the same!')


if __name__ == "__main__":
    main()
