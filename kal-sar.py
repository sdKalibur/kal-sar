#!/usr/bin/env python3

# debugging stuff
from dis import dis

# functional stuff
import datetime
import sys, csv, json, os, platform

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
    # stat_opts = ['-d', '--dev=sda']
    stat_opts = ['-u']
    stat_opts = [i.center(len(i) + 2, ' ') for i in stat_opts ] # clean space the opts

    sadf_command = 'sadf ' + stat_fmt + ' -- ' + str(' '.join(stat_opts)) + sysstat_file + sadf_time_window()

    my_sadf = os.popen(sadf_command).read().strip('\'').strip(' ').split(',') #.split('\n')
    print('my sadf ', my_sadf)
    sadf_list = [(_).split(';') for _ in my_sadf ]
    print('sadf list', sadf_list)
    return my_sadf,

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
        csv_list = [ _ for _ in csv_data ]
        print('bugging', csv_list)
    return csv_list

def csv_obj_iter(csv_obj):
    """ I interate a csv formatted obj"""
    csv_data = csv.reader(csv_obj, delimiter=';')
    csv_obj = str(csv_obj)
    print('csv data:\n', csv_obj)
    count = 0
    stats_data = []
    print('#' * 20)
    # [print(_).split(';') for _ in csv_obj[0] ]
    for data in csv_obj[0]:
        # i = data
        i = [ _.split(';') for _ in data[0][count] if not None ]
        header = []
        print("print i count", i[count])
        stats_data.append(stats_data.append(i[count].strip('\'').strip(' ').split(',')))
        # stats_data.append(stats_data.append(i[count].split(';')))
        # if type(stats_data[count]) == NoneType :
        #     print("I found a NoneType")
        if '#' in stats_data[count]:
            if not stats_data[count] in header:
                header.append(stats_data[count])
                print("I modified header :\n", header)
        else:
            print("Header remains as :\n", header)
        count += 1
    bar = "- + " * 20
    print(bar)
    print('Header :', header )
    print(bar)
    print('Count :',  count)
    print(bar)
    print('Stats :', stats_data)
    # print('processed', sys_info)
    return 1 + 1

def ssh_connector(dest_host):
    pass

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