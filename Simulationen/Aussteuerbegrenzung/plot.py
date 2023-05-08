# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:35:41 2023

@author: David
"""

import matplotlib.pyplot as plt
import tikzplotlib
import pandas as pd
import numpy as np



def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols, which breaks tikzplotlib
    """
    if hasattr(obj, "_ncols"):
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)



plt.style.use("custom.mplstyle")


#---------------------------------------------

data = pd.read_csv("Aussteuerbegrenzung.log.txt",sep='\t')
#limit time 

#set base unit
time_unit = ""
time_fact = 10**6
#remove offset
time_offset = 3505



fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
for i,deadtime in enumerate(np.linspace(10,50,5,endpoint=True)):
    x = data.loc[21*i:21*(i+1)-1,"duty"]
    y = data.loc[21*i:21*(i+1)-1,"u_cap"]
    plt1 = ax1.plot(x, y, label = f"deadtime = {deadtime}")
#ax2.grid(False)

ax1.set_ylabel('Bootstrap Kondensator Spannung/V')
ax1.set_xlabel(f"Tastgrad")


#Generate legend
# plots = plt1+plt2+plt3   #entry needs to be added for every plot
# labels = [l.get_label() for l in plots]
# ax1.legend(plots, labels, loc=0)
ax1.legend()
#ax2.legend()

ax1.get_xaxis().get_major_formatter().set_useOffset(True)

tikzplotlib_fix_ncols(fig)

# tikzplotlib.save('NoDiode.tex',
#     float_format = ".10g",
#     axis_width=r'\textwidth',
#     axis_height=r'0.3\textwidth')
  #  figure_width=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
  #  figure_height=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
#    extra_tikzpicture_parameters={'trim axis group left', 'trim axis group right'},
#    extra_axis_parameters={"xtick={-0.5,-0.25,0,0.25,0.5}"},
#    extra_groupstyle_parameters={f'vertical sep={sep}em'})
plt.savefig("Aussteuerbegrenzung.eps")
plt.show()


