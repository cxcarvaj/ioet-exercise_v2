import sys
from functions import *


def main(argv):
    if len(argv) < 2 or argv[1] == '-h':
        help_message()
        sys.exit()

    schedules = []
    file_name = argv[1]
    file = open(file_name, 'r')
    for line in file:
        try:
            employee, schedule_data = line.strip().split('=')
            schedules.append(build_employee_schedule_struct(employee, schedule_data))
        except Exception:
            print('Incorrect format of the document')

    compare_schedules(schedules)


main(sys.argv)
