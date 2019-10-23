#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

data = np.arange(100, 201)
plt.subplot(2,1,1) # show multi graphs
plt.plot(data)

data2 = np.arange(200, 301)
# plt.figure()
plt.subplot(2,1,2) # show multi graphs
plt.plot(data2
        )

plt.show()
