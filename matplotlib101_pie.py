#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

labels = ['Mon', 'Tues','Wed', 'Thur', 'Fri', 'Sat', 'Sun' ]

data = np.random.rand(7) * 100

plt.pie(data, labels=labels , autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

plt.show()