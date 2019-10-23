#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

N = 20

plt.scatter(np.random.rand(N) * 100, # Y axis
            np.random.rand(N) * 100, # X acis
            c='r', s=100, alpha=0.5,  # colour size and transparency
            )

plt.scatter(np.random.rand(N) * 100, # Y axis
            np.random.rand(N) * 100, # X acis
            c='g', s=200, alpha=0.5,  # colour size and transparency
            )

plt.scatter(np.random.rand(N) * 100, # Y axis
            np.random.rand(N) * 100, # X acis
            c='b', s=300, alpha=0.5,  # colour size and transparency
            )

plt.show()