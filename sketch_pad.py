import csv, platform, subprocess

def sysstat_file_path():
    if 'ubuntu' in (platform.platform().lower()):
        sysstat_file = '/var/log/sysstat/sa'
    elif 'redhat' or 'centos' or 'fedora' in (platform.platform().lower()):
        sysstat_file = '/var/log/sa/sa'
    print(sysstat_file)
    return sysstat_file


def get_sysstat_day() :
    """Locates sysstat file and excutes sadf command"""
    day = '7'
    if len(day) <= 1:
        day = '0' + day
    else:
        day = day
    sysstat_file = sysstat_file_path() + str(day)
    stat_fmt = '-d' # -d is database friendly csv with ';' delimeter
    # stat_opts = ['-d', '--dev=sda']
    stat_opts = ['-u']
    stat_opts = [i.center(len(i) + 2, ' ') for i in stat_opts ] # clean space the opts

    sadf_command = 'sadf ' + stat_fmt + ' -- ' + str(' '.join(stat_opts)) + sysstat_file, "-s 12:00 -e 13:00"

    my_sadf = subprocess.getoutput(sadf_command)

    print('my sadf ', my_sadf)
    # sadf_list = [(_).split(';') for _ in my_sadf ]
    # print('sadf list', sadf_list)
    return my_sadf

csv_object = get_sysstat_day()

stat_list = csv_object.strip().split('\n')


for row in stat_list:
    print(row.split(';'))

"""

>>> c_ls =  [ str(_) for _ in row_ls[1:4] ]
>>> c_ls
['2', '3', '4']
>>> c_ls = row_ls[0] 
>>> c_ls


"""