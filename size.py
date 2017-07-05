import sys
import os


def get_terminal_size():
    for i in range(0, 3):
        try:
            columns, rows = os.get_terminal_size(i)
        except OSError:
            continue
        break
    else:
        columns, rows = (80, 24)  # set default in case all fail
    return columns, rows


sys.stdout.write('cols:{}\nrows:{}\n'.format(*get_terminal_size()))
