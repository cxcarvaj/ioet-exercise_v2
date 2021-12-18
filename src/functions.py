# Functions used to solve this problem

from datetime import datetime as dt


def help_message():
    """
    This function prints out a help message in order to run this program correctly
    """
    print('In order to use this program you should run the following commands:\n'
          'For Windows: py main.py <inputfile_path>\n'
          'For Linux or Mac: python3 main.py <inputfile_path>\nAtt: Carlos Carvajal')


def build_employee_schedule_struct(employee: str, schedule_data: str) -> dict:
    """
    This function process employee's name and their schedule sent as parameter in order to build a data structure
    which contains the employee name and the data from their schedule

    :parameters

    employee: str
        The name of the employee.

    schedule_data: str
        The schedule data of the employee

    :return
        The data structure that links each employee with their own schedule
    """
    schedule = dict()
    schedule['employee_name'] = employee
    schedule['data'] = parse_schedule_string_to_dict(schedule_data)
    return schedule


def parse_time_string_to_datetime(time_string: str, time_format="%H:%M") -> dt:
    """
    This function parse the time string sent as a parameter, to a datetime object according to a time format.
    Default time format es %H:%M

    :parameters

    time_string: str
        The time of the schedule as a string.

    time_format: str
        The format of the time that the function will parse the string.

    :return
        The datetime object of the string
    """
    return dt.strptime(time_string, time_format)


def parse_schedule_string_to_dict(schedule_string: str) -> dict:
    """
    This function parse the schedule string sent as a parameter, to a dictionary.

    :parameters

    schedule_string: str
        The time of the schedule as a string.

    :return
        A schedule dictionary with a day code as a key and a range of time as the value.
    """
    schedule_dic = {}
    if schedule_string and len(schedule_string) > 0:
        for day in schedule_string.split(','):
            day_code = day[:2]
            start_time, end_time = day[2:].split('-')
            schedule_dic[day_code] = {'start_time': start_time.strip(),
                                      'end_time': end_time.strip()}
    return schedule_dic


def is_a_coincided_hour_range(hour_range: dict, other_hour_range: dict) -> bool:
    """
    This function decides if the hour ranges sent as a parameter match, if they are, that means that the employees
    have coincided at that range of time in the office.

    :parameters

    hour_range: dict
        The start time and end time (hour range) of a schedule saved in a dictionary.

    other_hour_range: dict
        The start time and end time (hour range) of a different schedule from the other saved in a dictionary.

    :return
        A Boolean value that determines whether the ranges of hours coincided
    """
    if hour_range is not None and other_hour_range is not None:
        start_time = parse_time_string_to_datetime(hour_range['start_time'])
        end_time = parse_time_string_to_datetime(hour_range['end_time'])
        other_start_time = parse_time_string_to_datetime(other_hour_range['start_time'])
        other_end_time = parse_time_string_to_datetime(other_hour_range['end_time'])
        return start_time <= other_end_time and end_time >= other_start_time


def calculate_times_coincided(schedule: dict, other_schedule: dict) -> int:
    """
    This function compares different schedules in order to calculate how many times these schedules have coincided.

    :parameters

    schedule: dict
        The schedule object from an employee that contains the days and the hours they have worked.

    other_schedule: dict
        The schedule object from a different employee that contains the days and the hours they have worked.

    :return
        The times that this employee's schedules have coincided
    """
    times_coincided = 0
    for day in list(schedule.keys()):
        if is_a_coincided_hour_range(schedule.get(day), other_schedule.get(day)):
            times_coincided += 1
    return times_coincided


def compare_schedules(schedules: list):
    """
    This function process all the schedules data in a list sent as a parameter and compare them.
    Finally, it prints out a table containing pairs of employees and how often they have coincided in the office.

    :parameters
    schedules : list
        A list that contains all employee's schedules.
    """
    for i in range(len(schedules)):
        for j in range(i + 1, len(schedules)):
            matches = calculate_times_coincided(schedules[i]['data'], schedules[j]['data'])
            if matches > 0:
                print('{}-{}: {}'.format(schedules[i]['employee_name'], schedules[j]['employee_name'], matches))
