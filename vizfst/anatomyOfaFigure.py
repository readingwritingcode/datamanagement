#!/usr/bin/python3

# MATPLOTLIB INTRO
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

# SIMPLE EXAMPLE
fig, ax = plt.subplots() # creting figure containing a single axes

ax.plot([1,2,3,4],[1,4,2,3]) # plot some data on the axes

# ANATOMY OF A FIGURE

# tile
ax.set_title

# legen
ax.legend

# grid
ax.grid

# axes
fig.subplot

#line
ax.plot

# markers
ax.scatter

# x axis
ax.xaxis

# y axis
ax.yaxis

# x label
ax.set_xlabel

# y label
ax.set_ylabel

# minor tick label    -> ?
ax.xaxis.set_minor_formatter

# major tick label   -> ?
ax.yaxis.set_major_formatter

# major tick -> ?
ax.yaxis.set_major_locator

# minor tick -> ?
ax.yaxis.set_minor_locator

