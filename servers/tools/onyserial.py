#!../../venv/bin/python
# -*- coding: iso-8859-1 -*-

import select
import serial
import sys
import os

EXIT = 'exit'


def format_line(line):
    if  type(line) == bytes:
        aux = str(line.decode('utf-8'))
    else:
        aux = line
    return aux.replace('\n', '').replace('\r', '')


def parse_serial(line):
    print('received: ', line)


def parse_stdin(line):
    print('line ', line)
    print('EXIT', EXIT)
    print('line==EXIT', line==EXIT)
    if str(line) == str(EXIT):
        print(EXIT)
        return False
    else:
        sys.stdout.flush()
        print('sending: ', line + '\n')
    return True

def main():
    serial_name = '/dev/ttyUSB0'
    baud_rate = 9600
    conn = serial.Serial(serial_name, baud_rate, timeout=0)
    loop_condition = True
    while loop_condition:
        print('loop_condition', loop_condition)
        [readable, _writalble, _] = select.select([conn, sys.stdin], [], [])
        if conn in readable:
            line = conn.readline()
            parse_serial(format_line(line))
        elif sys.stdin in readable:
            line = sys.stdin.readline()
            loop_condition = parse_stdin(format_line(line))
    return True


if __name__ == "__main__":
    my_error = main()
    if my_error:
        sys.exit(1)
    else:
        sys.exit(0)

