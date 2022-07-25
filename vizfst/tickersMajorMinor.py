#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator,FormatStrFormater,
                               AutoMinorLocator)

# data

t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * n.exp(-t * 0.01)

# plot
fig, ax = plt.subplots()
ax.plots(t,s)

# make a plot with major ticks that are multiplies of 20 and minor
# ticks that are multiples of 5. laber major ticks with '%d' formatting
# but dont label minor ticks
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

# For the minor ticks, use no labels; default NullFormatter.
ax.xaxis.set_minor_locator(MultipleLocator(5))

plt.show()
