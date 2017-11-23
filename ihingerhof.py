#!/usr/bin/python

import glob
import os
import datetime

def gettemp(latest = '/home/hoe/ih'):
    while not os.path.isfile(latest):
        filelist = glob.glob(latest+'/*')
        latest = max(filelist, key=os.path.getctime)

    with open(latest, 'r') as f:
        lines = f.read().split('\n')

    lastline = lines[-2].split(';')
    temp = lastline[1]

    timestamp = datetime.datetime.fromtimestamp(int(lastline[0])).strftime('%d.%m.%Y, %H:%M')
    return [timestamp, temp]

def main():
    data = gettemp('/home/hoe/ih')
    temp = data[1]
    timestamp = data[0]
    print temp + ' (' + timestamp + ')'

if __name__ == '__main__':
    main()
