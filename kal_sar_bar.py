#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from kal_sar import main as kal_sar

data_set = kal_sar()
N = 7 # len(data_set[0])
labels = data_set[0]
data = data_set[1]

print(labels)

metric = input("Enter a metric from above list >")


filter = labels.index(metric)
print('#' * 40)

def tseries():
    """Create data series for selected metric"""

    tseries = []
    for _ in data:
        tseries.append(_[2])
    print(tseries)
    return tseries


def dseries():
    """Create data series for selected metric"""

    dseries = []
    for _ in data:
        dseries.append(_[6])
    print(dseries)
    return dseries


plt.title("Weekday Data")
# plt.plot(dseries())
plt.bar(tseries(), dseries(), alpha=0.8, )
plt.show()