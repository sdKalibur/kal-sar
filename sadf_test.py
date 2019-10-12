# import sadf
# from sadf import fieldgroups as fg
#
# cmd = sadf.SadfCommand(start_time='09:00:00', end_time='23:00:00')
#
# cmd.field_groups = [
#     fg.CPULoad(all_fields=True),
#     fg.Queue(),
#     fg.ProcessAndContextSwitch(),
#     fg.IO(),
#     fg.Memory(all_fields=True)
# ]
#
# report = cmd.run()
#
# memory_report = report.reports['memory']\
#     .resample('30T').mean()
#
# ldavg_report = report.reports['queue']\
#     .resample('10T').rolling(window=3).mean()\
#     .dropna()\
#     .loc[:, ['ldavg-1', 'ldavg-5', 'ldavg-15']]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,2,5,'np','nan',6,8])

dates = pd.date_range('20190926', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates,columns=['one','two','three','four'])

df
