#!/usr/bin/env python3.7
####################################################
#
# Author: M Joyce
# For use with ASTR3007/6007 MESA-based assignments
#
####################################################
import numpy as np
import pandas as pd
import bokeh
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file 

MESA_file = '10.iso'

log_Teff, log_g= np.loadtxt(MESA_file, usecols=(10,12), unpack=True)


## the dictionary
star_features ={
	 'log_Teff': log_Teff,
	 'log_g': log_g
	 }

df = pd.DataFrame(data=star_features)
source = ColumnDataSource(data=df)

TITLE = "Interactive HR"
TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS, toolbar_location="above")#, plot_width=600, plot_h%pip install -U numpyeight=800, title=TITLE)
p.toolbar.logo = "grey"
p.background_fill_color = "#dddddd"
p.xaxis.axis_label = "log Teff"
p.yaxis.axis_label = "log g"
p.grid.grid_line_color = "white"

## the labels 
#p.hover.tooltips = 
#    ("star age (Gyr):", "@star_age"),
#    ]#("model number", "@model_number"),
	#]

p.circle('log_Teff', 'log_g', size=5, source = source, 
         color='green',  fill_alpha=0.8) #line_color="black",
p.x_range.flipped = True

output_file("log_teff.html", title="log g-Teff")#, mode='inline')
show(p)