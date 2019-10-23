#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

N = 7

x = np.arange(N)

data = np.random.randint(low=0, high=100, size=N)
colors = np.random.rand(N * 3).reshape(N, -1)
labels = ['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.title("Weekday Data")
plt.bar(x, data, alpha=0.8, color=colors, )
plt.show()