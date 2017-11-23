#!/usr/bin/python

import re
import os
import time
import glob
import datetime

def read_sensor(path, retry = 3):
    value = 'U'
    try:
        while True:
            f = open(path, "r")
            lines = f.read().split('\n')
            f.close()
            if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", lines[0]):
                m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", lines[1])
                if m:
                    value = str(float(m.group(2)) / 1000.0)
                    if value == '85':
                        value = 'U'
            if not value == 'U':
                break
            retry = retry - 1
            if retry < 0:
                break
    except (IOError), e:
        print time.strftime("%x %X"), "Error reading", path, ": ", e
    return value

def logstring():
    now = datetime.datetime.now()
    dtstr = now.strftime("%Y-%m-%d;%H:%M")
    log = dtstr
    sensors = glob.glob('/sys/bus/w1/devices/28*')
    for sensor in sensors:
        log = log + ';' + read_sensor(sensor + '/w1_slave')
    print log

def printstring():
    sensors = glob.glob('/sys/bus/w1/devices/28*')
    for sensor in sensors:
        val = read_sensor(sensor + '/w1_slave')
        return val

def main():
    logstring()

if __name__ == '__main__':
    main()
