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

log_Teff, log_L= np.loadtxt(MESA_file, usecols=(10,7), unpack=True)


select = np.where ((log_Teff < 3.8) & (log_Teff > 3.5) & (log_L < 3.4)) #& (log_L > 0))
log_Teff = log_Teff[select]
log_L = log_L[select]


## the dictionary
star_features ={
	 'log_Teff': log_Teff,
	 'log_L': log_L
	 }

df = pd.DataFrame(data=star_features)
source = ColumnDataSource(data=df)

TITLE = "Interactive HR"
TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS, toolbar_location="above")#, plot_width=600, plot_h%pip install -U numpyeight=800, title=TITLE)
p.toolbar.logo = "grey"
p.background_fill_color = "#dddddd"
p.xaxis.axis_label = "log Teff"
p.yaxis.axis_label = "log L"
p.grid.grid_line_color = "white"


p.circle('log_Teff', 'log_L', size=5, source = source, 
         color='green',  fill_alpha=0.8) #line_color="black",
p.x_range.flipped = True

output_file("LT.html", title="L - Teff")#, mode='inline')
show(p)
