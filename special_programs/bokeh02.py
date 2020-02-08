#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 07:33:38 2020

@author: arun

Credits: Brad Traversy
"""

# Import figure - to create a figure object
# Import output_file - to create a html file
# Import show - to render the plot
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
# This is used to implement colourmaps based on certain factors.
from bokeh.transform import factor_cmap
#  A sample blue palette
from bokeh.palettes import Blues8
# This is used to extract script and div components
from bokeh.embed import components

# Import numpy and pandas for creating data sets
import numpy as np
import pandas as pd

# Read in CSV
df = pd.read_csv('cars.csv')
source = ColumnDataSource(df)

car_list = source.data['Car'].tolist()
# this is needed as y_range in figure accepts list or arrays.
# Make a figure object
plot = figure(
    title="Price of Cars with Horsepower",
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    x_axis_label="Horse power",
    y_axis_label="Car name",
)

# Create an output html to render the plot.
output_file("Figure_sample2.html")

# note that instead of the variable "car", now you are using the column 'Car' from
# the variable "source". Same with 'Horsepower'
plot.hbar(y='Car', right='Horsepower', left=0, height=0.4,
            fill_color=factor_cmap('Car', palette=Blues8, factors=car_list),
            fill_alpha=0.9, source=source, legend='Car')
# For comparison, this is the old line
# plot.hbar(y=car, right=hp, left=0, height=0.4, color='orange', fill_alpha=0.5)

# Add hover details to the tool-tip
hover = HoverTool()
hover.tooltips = [
    ("Car", "@Car"),
    ("HP", "@Horsepower"),
    ("Price", "@Price"),
    ("Image", "<div><img src=\"@Image\" alt=\"\" width=\"200\"/></div>"),
]
# hover.tooltips = """
# <div>
#   <h3>@Car</h3>
#   <div><strong>Price:</strong>@Price</div>
#   <div><strong>Horse Power:</strong>@Horsepower</div>
#   <div><img src="@Image" alt="" width="200"/></div>
# </div>
# """
plot.add_tools(hover)

# Show results
show(plot)

# Save results
save(plot)

# Extract components
script, div = components(plot)
print(script)
print(div)