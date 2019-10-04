# !/usr/bin/env python3
# google pandas-docs getting started 10 min.
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

import pandas as pd

>>> header = ['# hostname', 'interval', 'timestamp', 'runq-sz', 'plist-sz', 'ldavg-1', 'ldavg-5', 'ldavg-15', 'blocked']
>>> data =  [['rhel.mac.local', '600', '2019-10-04 12:15:01 UTC', '0', '547', '0.00', '0.35', '0.46', '0'], ['rhel.mac.local', '600', '2019-10-04 12:25:01 UTC', '0', '617', '0.00', '0.19', '0.38', '1'], ['rhel.mac.local', '600', '2019-10-04 12:35:01 UTC', '1', '612', '0.00', '0.01', '0.18', '0'], ['rhel.mac.local', '600', '2019-10-04 12:45:01 UTC', '0', '613', '0.00', '0.00', '0.08', '0'], ['rhel.mac.local', '600', '2019-10-04 12:55:01 UTC', '0', '612', '0.00', '0.00', '0.03', '0'], ['rhel.mac.local', '600', '2019-10-04 13:05:01 UTC', '0', '614', '0.11', '0.06', '0.01', '0'], ['rhel.mac.local', '600', '2019-10-04 13:15:01 UTC', '0', '612', '0.03', '0.03', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:25:01 UTC', '0', '622', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:35:01 UTC', '0', '621', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:45:01 UTC', '0', '619', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:55:01 UTC', '1', '621', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:05:01 UTC', '0', '621', '0.00', '0.02', '0.02', '0'], ['rhel.mac.local', '600', '2019-10-04 14:15:01 UTC', '0', '615', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:25:01 UTC', '0', '615', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:35:02 UTC', '0', '617', '0.08', '0.04', '0.01', '0'], ['rhel.mac.local', '599', '2019-10-04 14:45:01 UTC', '0', '617', '0.05', '0.03', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:55:01 UTC', '0', '614', '0.00', '0.01', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 15:05:01 UTC', '1', '617', '0.01', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 15:15:01 UTC', '0', '604', '0.04', '0.16', '0.08', '0']]
>>> data
[['rhel.mac.local', '600', '2019-10-04 12:15:01 UTC', '0', '547', '0.00', '0.35', '0.46', '0'], ['rhel.mac.local', '600', '2019-10-04 12:25:01 UTC', '0', '617', '0.00', '0.19', '0.38', '1'], ['rhel.mac.local', '600', '2019-10-04 12:35:01 UTC', '1', '612', '0.00', '0.01', '0.18', '0'], ['rhel.mac.local', '600', '2019-10-04 12:45:01 UTC', '0', '613', '0.00', '0.00', '0.08', '0'], ['rhel.mac.local', '600', '2019-10-04 12:55:01 UTC', '0', '612', '0.00', '0.00', '0.03', '0'], ['rhel.mac.local', '600', '2019-10-04 13:05:01 UTC', '0', '614', '0.11', '0.06', '0.01', '0'], ['rhel.mac.local', '600', '2019-10-04 13:15:01 UTC', '0', '612', '0.03', '0.03', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:25:01 UTC', '0', '622', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:35:01 UTC', '0', '621', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:45:01 UTC', '0', '619', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 13:55:01 UTC', '1', '621', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:05:01 UTC', '0', '621', '0.00', '0.02', '0.02', '0'], ['rhel.mac.local', '600', '2019-10-04 14:15:01 UTC', '0', '615', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:25:01 UTC', '0', '615', '0.00', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:35:02 UTC', '0', '617', '0.08', '0.04', '0.01', '0'], ['rhel.mac.local', '599', '2019-10-04 14:45:01 UTC', '0', '617', '0.05', '0.03', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 14:55:01 UTC', '0', '614', '0.00', '0.01', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 15:05:01 UTC', '1', '617', '0.01', '0.00', '0.00', '0'], ['rhel.mac.local', '600', '2019-10-04 15:15:01 UTC', '0', '604', '0.04', '0.16', '0.08', '0']]

df = pd.DataFrame(data, columns=header)

header[0] = str(header[0]).strip('#')
header[0] = str(header[0]).strip(' ')

