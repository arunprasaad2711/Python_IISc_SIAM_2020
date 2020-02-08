#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 07:29:41 2020

@author: arun
"""

import numpy as np
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.embed import components

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

show(plot)
script, div = components(plot)

print(div)
print(script)
# html = file_html(plot, CDN, "my plot")