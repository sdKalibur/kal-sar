import sadf
from sadf import fieldgroups as fg

cmd = sadf.SadfCommand(start_time='09:00:00',
                       end_time='18:00:00')

cmd.field_groups = [
    fg.CPULoad(all_fields=True),
    fg.Queue(),
    fg.ProcessAndContextSwitch(),
    fg.IO(),
    fg.Memory(all_fields=True),
]

report = cmd.run()

memory_report = report.reports['memory']\
    .resample('30T').mean()

ldavg_report = report.reports['queue']\
    .resample('10T').rolling(window=3).mean()\
    .dropna()\
    .loc[:, ['ldavg-1', 'ldavg-5', 'ldavg-15']]