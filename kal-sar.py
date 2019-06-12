#!/usr/bin/env python3

# debugging stuff
from dis import dis

# functional stuff
import datetime
import sys, csv, json, os, platform
import subprocess
# import paramiko for ssh

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

    start_time = str(input('Enter start time hh:mm > '))
    end_time = str(input('Enter end time hh:mm > '))
    time_window = ' -s ' + start_time + ' -e ' + end_time
    return time_window

def sysstat_file_path():
    """ Sets the OS default path for syssta log file. """
    if 'ubuntu' in (platform.platform().lower()):
        sysstat_file = '/var/log/sysstat/sa'
    elif 'redhat' or 'centos' or 'fedora' in (platform.platform().lower()):
        sysstat_file = '/var/log/sa/sa'
    return sysstat_file

def get_sysstat_day(day,mode='') :
    """ Locates sysstat file and excutes sadf command """
    if len(day) <= 1:
        day = '0' + day
    else:
        day = day
    sysstat_file = sysstat_file_path() + str(day)
    stat_fmt = '-d' # -d is database friendly csv with ';' delimeter
    # stat_opts = ['-d', '--dev=sda']
    sar_opts = ['sadf', stat_fmt, '--', str(sysstat_file), str(sadf_time_window()) ]

    if mode == '':
        mode = str(get_stat_mode())
    else:
        pass

    # try:
    #     if mode not in modes.items:
    #         print(mode, "Is an invalid mode.  Mode options are: \n" )
    #     else:
    #         sar_opts.append(str(mode))


    sar_opts.append(mode)

    sar_opts = [i.center(len(i) + 2, ' ') for i in sar_opts ]
    print('stat mode: ', mode)
    sadf_command = ''
    for i in sar_opts:
        sadf_command += str(i).center(len(str(i))+1,' ')
    # print('I will execute this:', sadf_command)
    my_sadf = subprocess.getoutput(sadf_command)
    # print('My sadf output:\n', my_sadf)

    return my_sadf

def get_stat_mode():
    """ Gets the desired sysstat matric e,g cpu load, diskIO, etc. """
    # This should be the starting point, collected the mode, and time requirements finally doing the analysis.

    modes = {'CPU Load' : '-q', 'CPU Utilization':'-u', 'Disk IO':'-d -p', 'Network IO': '-n DEV'}
    menu_modes = []
    for i in modes:
        menu_modes.append(i)

    print('select a mode index :')
    for i in menu_modes:
        print('\t', menu_modes.index(i), ' : ', i)
    # print(menu_modes)
    mode_index = int(input('Enter a numeric value matching at index above: '))
    mode = modes.get(menu_modes[mode_index])
    return str(mode)

    # get a function to work the netty gretty of the specific device selection bits

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
        [ print(_) for _ in csv_data ]
        csv_list = [ _.split(';') for _ in csv_data ]
        print('b   ugging', csv_list)
    return csv_list

def csv_obj_iter(csv_obj):
    """ I interate a csv formatted obj"""

    stat_list = csv_obj.strip().split('\n')
    count = 0
    header = []
    data_ls = ['']
    for row in stat_list:
        row_ls = (row.split(';'))
        if '#' in row_ls[0]:
            if  len(header) == 0:
                header.append(row_ls)
            else:
                continue
            # print("I modified header :\n", header)
        else:
            print("I am this row: ", row_ls)
            data_ls.append(row_ls)
            for item in row_ls:
                print("splitting this sucker", item.strip())
            print('print row count', data_ls[count])
            count += 1
        # for i in row_ls: # Maybe log this in the future.
        #     print(i, ' : ', type(i))
    # print(header)
    print('will return \n', data_ls)

    return data_ls

def ssh_connector(dest_host):
    pass

def main () :
    """"gets day of the month 01-31 and metric to collect e,g CPU Load stats."""
    # mode = get_stat_mode()

    # mode = 'cpu_util'

    day = str(input('Which day do you want to check stats for :')) # need to add contraints for not accepting invalid days.
    if len(day) <= 1:
        day = '0' + day
    else:
        day = day

    # get_sysstat_day(day)
    print(day)

    stat_info = csv_obj_iter(get_sysstat_day(day))
    # print('Return info : \n', stat_info)
    # for _ in stat_info:
    #      print(_, end='\n')

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