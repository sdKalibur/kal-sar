#!/usr/bin/env python3

# debugging stuff
from dis import dis

# functional stuff
import datetime
from datetime import date
import sys, csv, json, os, platform
import subprocess
# import ssh_klient from ssh_klient as ssh
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
    sar_opts = ['sadf', stat_fmt, '--', str(sysstat_file), str(sadf_time_window())]

    if mode == '':
        mode = str(get_stat_mode())
    else:
        pass

    sar_opts.append(mode)

    sar_opts = [i.center(len(i) + 2, ' ') for i in sar_opts ]
    print('DEBUG: stat mode: ', mode)
    sadf_command = ''
    for i in sar_opts:
        sadf_command += str(i).center(len(str(i))+1,' ')
    print('DEBUG will execute:', sadf_command)

    try:
        my_sadf = subprocess.getoutput(sadf_command)
    except Exception as e:
        print('Errer getting the sysstat file : \n {}'.format(e))
        sys.exit(1)

#    try:
#        sar_data_file = open(str(str(day)+str(mode)+'_sys_stat_data.csv'), 'a')
#        print(sar_data_file)
#        sar_data_file.write(my_sadf)
#        sar_data_file.close()
#        print(my_sadf)
#    except Exception as e:
#        print("There is an issue getting the sysstat file: \n {}".fromat(e))
#        sys.exit(2)
    return my_sadf

def get_stat_mode(mode='-q'):
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
    mode_index = int(input('Enter a numeric value matching an index above:'))

    print('My mode', mode_index)
    mode = modes[menu_modes[mode_index]]

    return str(mode)

    # get a function to work the netty gretty of the specific device selection bits iface=DEV

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
    """ I iterate a sysstat csv obj and return a header\
        and body list of lists
    """

    stat_list = csv_obj.strip().split('\n')
    count = 0
    header = []
    data_ls = []
    for row in stat_list:
        row_ls = (row.split(';'))
        if '#' in row_ls[0]:
            if len(header) == 0:
                header.append(row_ls)
            else:
                continue
            # print("I modified header :\n", header)
        elif row_ls[0] == 'End of system activity file unexpected':
            continue
        elif len(row_ls) <= 4:
            # print("skipping :", row_ls)
            continue
        else:
            # print("I am this row: ", row_ls)
            data_ls.append(row_ls)
        count += 1
    print(data_ls)

    if len(header) > 0:
        print('header', len(header))
        header[0][0] = header[0][0].strip('#').strip(' ').capitalize()  # Remove the # from headers
        header = header[0]
        print("Header length", len(header[0]), 'Header values', header)
        print("")
        print("Data list length ", len(data_ls), len(data_ls[0]))
    else:
        print("Nothing in that row")
    ## data_info = header + data_ls
    # print("Header \n", header)
    # print("Data List\n", data_ls)
    # print('This is my data: ', data_info)
    # return data_info

    return header, data_ls

def ssh_connector(dest_host):
    pass

def main () :
    """"gets day of the month 01-31 and metric to collect e,g CPU Load stats."""
    # mode = get_stat_mode()

    # mode = 'cpu_util'

    day = str(input('Which day do you want to check stats for :')) # need to add contraints for not accepting invalid days.
    if len(day) == 1:
        day = '0' + day
    if not day:
        day = date.today().strftime("%d")
    else:
        day = day

    # get_sysstat_day(day)
    print(day)

    stat_info = csv_obj_iter(get_sysstat_day(day))
    print("DEBUG:  stat info.", stat_info)

    return stat_info

if __name__ == '__main__' :
    main()
    # call ssh client

# os.system('sadf -j -- -n DEV --iface=wlp1s0 /var/log/sysstat/sa27')
