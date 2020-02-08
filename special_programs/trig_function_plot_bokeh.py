from bokeh.plotting import figure, output_file, show
import numpy as np

# prepare some data
x = np.linspace(0, 2.0*np.pi, 101)
sine = np.sin(x)
cosine = np.cos(x)

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple sine curve", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, sine, legend="$\sin$", line_width=2, color='red')
p.line(x, cosine, legend="$\cos$", line_width=2, color='green')

# show the results
show(p)
