#!/usr/bin/env python3

import datetime
import sys, csv, json, sadf, os

class kal_server():
    self.server_name = server_name


def open_sar_file () :
    pass

def get_high_iowait () :
    pass

def get_high_load () :
    pass

def get_high_cpu_util () :
    pass

def get_high_disk_util () :
    pass

def draw_a_graph () :
    """Graph my system stats"""
    # -g - generates a graph
    pass

def sadf_time_window (): #start, end) :
    """Search sysstat for a time period"""
    # sadf /var/log/sysstat/sa23 -s 17:00 -e 17:20
    # -d - comma delimited csv
    # -j - json
    # -- -d - sar options such -d -q -u etc.
    start_time = str(input('Enter start time hh:mm > '))
    end_time = str(input('Enter end time hh:mm > '))
    time_window = ' -s ' + start_time + ' -e ' + end_time
    # print(time_window)
    return time_window

def get_sysstat_day(day) :
    # stat_day = ''
    sysstat_file = '/var/log/sysstat/sa' + str(day)
    sadf_command = 'sadf -j -- -n DEV --iface=wlp1s0 ' + sysstat_file + sadf_time_window()
    my_sadf = os.system(sadf_command)
    # print(sadf_command)
    return my_sadf

def main () :
    day = input('Which day do you want to check stats for :')
    # get_sysstat_day(day)
    for i in str(get_sysstat_day(day)):
        print(i)

if __name__ == '__main__' :
    main()


# cur_day = datetime.date.today().day
# print(cur_day)
# sysstat_file = '/var/log/sysstat/sa' + str(cur_day)
#
# sadf_command = 'sadf -d -- -n DEV --iface=wlp1s0' + sysstat_file
# os.system(sadf_command)

# os.system('sadf -j -- -n DEV --iface=wlp1s0 /var/log/sysstat/sa27')