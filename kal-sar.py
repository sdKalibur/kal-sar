#!/usr/bin/env python3

# debugging stuff
from dis import dis

# functional stuff
import datetime
import sys, csv, json, sadf, os, platform

class kal_server():
    pass
    # server_name = self.server_name
    # server_address = server_addr


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
    # os.system('ssh kalibur-mce sadf /var/log/sysstat/sa01')
    start_time = str(input('Enter start time hh:mm > '))
    end_time = str(input('Enter end time hh:mm > '))
    time_window = ' -s ' + start_time + ' -e ' + end_time
    # print(time_window)
    return time_window

def sysstat_file_path():
    if 'ubuntu' in (platform.platform().lower()):
        sysstat_file = '/var/log/sysstat/sa'
    elif 'redhat' or 'centos' or 'fedora' in (platform.platform().lower()):
        sysstat_file = '/var/log/sa/sa'
    print(sysstat_file)
    return sysstat_file

def get_sysstat_day(day) :
    """Locates sysstat file and excutes sadf command"""
    if len(day) <= 1:
        day = '0' + day
    else:
        day = day
    sysstat_file = sysstat_file_path() + str(day)
    stat_fmt = '-d' # -d is database friendly csv with ';' delimeter
    stat_opts = ['-d', '--dev=sda']
    stat_opts = [i.center(len(i) + 2, ' ') for i in stat_opts ] # clean space the opts

    sadf_command = 'sadf ' + stat_fmt + ' -- ' + str(' '.join(stat_opts)) + sysstat_file + sadf_time_window()

    my_sadf = os.system(sadf_command)
    return my_sadf

def csv_stat_w(csv_obj):
    """give me a csv formatted object to write"""
    with open('sample_out.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile,end='')

def csv_file_r(csv_file):
    """give me a csv formatted object to read"""

    with open(csv_file, 'r', newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=';')
        # header = next(csv_data)
        # print('csv data contains ' + header, '\n', csv_data)
        [ print(_0) for _ in csv_data ]
        csv_list = [ _ for _ in csv_data ]
        print('bugging', csv_list)
    return csv_list

def csv_obj_iter(csv_obj):
    """ I interate a csv formatted obj"""
    for i in csv_obj:
        if '#' in csv_obj[i][0]:
            continue
        else:
            print(csv_obj[i])
    return


def main () :
    """"gets day of the month 01-31"""
    day = str(input('Which day do you want to check stats for :')) # need to add contraints for not accepting invalid days.
    if len(day) <= 1:
        day = '0' + day
    else:
        day = day

    # get_sysstat_day(day)
    print(day)

    csv_obj_iter(get_sysstat_day(day))
    # z = []
    # for i in str(get_sysstat_day(day)):
    #     # look to work with csv, json, or list
    #     print(i)
    #     z = z.append(i)
    # return z
    # sys.exit()

if __name__ == '__main__' :
    main()

# @csv_obj_iter
# main()
# cur_day = datetime.date.today().day
# print(cur_day)
# sysstat_file = '/var/log/sysstat/sa' + str(cur_day)
#
# sadf_command = 'sadf -d -- -n DEV --iface=wlp1s0' + sysstat_file
# os.system(sadf_command)

# os.system('sadf -j -- -n DEV --iface=wlp1s0 /var/log/sysstat/sa27')