# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:35:41 2023

@author: David
"""

import matplotlib.pyplot as plt
import tikzplotlib
import pandas as pd



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

noDiode = pd.read_csv("NoDiode.txt",sep='\t')
#limit time 
noDiode = noDiode[noDiode["time"]>3.50492e-3]
noDiode = noDiode[noDiode["time"]<3.50536e-3]

#set base unit
time_unit = "us"
time_fact = 10**6
#remove offset
time_offset = 3505



fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
plt1 = ax2.plot(noDiode["time"]*time_fact-time_offset, noDiode["Id(M4)"], label = "Id(M4)",color = 'C4')
plt2 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(N004,Load)"],label = "Vgs(M3)")
plt3 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(load)"],label = "V(Load)")
ax2.grid(False)

ax1.set_ylabel('V/V')
ax2.set_ylabel('I/A')
ax1.set_xlabel(f"t/{time_unit}")


#Generate legend
# plots = plt1+plt2+plt3   #entry needs to be added for every plot
# labels = [l.get_label() for l in plots]
# ax1.legend(plots, labels, loc=0)
ax1.legend()
ax2.legend()

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
plt.savefig("NoDiode.eps")
plt.show()


#---------------------------------------------

noDiode = pd.read_csv("NoDiodeResistor.txt",sep='\t')
#limit time 
noDiode = noDiode[noDiode["time"]>3.5048e-3]
noDiode = noDiode[noDiode["time"]<3.5064e-3]

#set base unit
time_unit = "us"
time_fact = 10**6
#remove offset
time_offset = 3504.8



fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
plt1 = ax2.plot(noDiode["time"]*time_fact-time_offset, noDiode["Id(M4)"], label = "Id(M4)",color = 'C4')
plt2 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(N005,Load)"],label = "Vgs(M3)")
plt3 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(load)"],label = "V(Load)")
ax2.grid(False)

ax1.set_ylabel('V/V')
ax2.set_ylabel('I/A')
ax1.set_xlabel(f"t/{time_unit}")


#Generate legend
# plots = plt1+plt2+plt3   #entry needs to be added for every plot
# labels = [l.get_label() for l in plots]
# ax1.legend(plots, labels, loc=0)
ax1.legend()
ax2.legend()

ax1.get_xaxis().get_major_formatter().set_useOffset(True)

tikzplotlib_fix_ncols(fig)

# tikzplotlib.save('NoDiodeResistor.tex',
#     float_format = ".10g",
#     axis_width=r'\textwidth',
#     axis_height=r'0.3\textwidth')
  #  figure_width=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
  #  figure_height=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
#    extra_tikzpicture_parameters={'trim axis group left', 'trim axis group right'},
#    extra_axis_parameters={"xtick={-0.5,-0.25,0,0.25,0.5}"},
#    extra_groupstyle_parameters={f'vertical sep={sep}em'})
plt.savefig("NoDiodeResistor.eps")
plt.show()

#---------------------------------------------

noDiode = pd.read_csv("Diode.txt",sep='\t')
#limit time 
noDiode = noDiode[noDiode["time"]>3.50492e-3]
noDiode = noDiode[noDiode["time"]<3.50536e-3]

#set base unit
time_unit = "us"
time_fact = 10**6
#remove offset
time_offset = 3505



fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
plt1 = ax2.plot(noDiode["time"]*time_fact-time_offset, noDiode["Id(M4)"], label = "Id(M4)",color = 'C4')
plt2 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(N004,Load)"],label = "Vgs(M3)")
plt3 = ax1.plot(noDiode["time"]*time_fact-time_offset, noDiode["V(load)"],label = "V(Load)")
ax2.grid(False)

ax1.set_ylabel('V/V')
ax2.set_ylabel('I/A')
ax1.set_xlabel(f"t/{time_unit}")


#Generate legend
# plots = plt1+plt2+plt3   #entry needs to be added for every plot
# labels = [l.get_label() for l in plots]
# ax1.legend(plots, labels, loc=0)
ax1.legend()
ax2.legend()

ax1.get_xaxis().get_major_formatter().set_useOffset(True)

tikzplotlib_fix_ncols(fig)

# tikzplotlib.save('Diode.tex',
#     float_format = ".10g",
#     axis_width=r'\textwidth',
#     axis_height=r'0.3\textwidth')
  #  figure_width=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
  #  figure_height=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
#    extra_tikzpicture_parameters={'trim axis group left', 'trim axis group right'},
#    extra_axis_parameters={"xtick={-0.5,-0.25,0,0.25,0.5}"},
#    extra_groupstyle_parameters={f'vertical sep={sep}em'})
plt.savefig("Diode.eps")
plt.show()

#---------------------------------------------

deadtime = pd.read_csv("DeadtimeStepped.txt",sep='\t')
#limit time 
#noDiode = noDiode[noDiode["time"]>3.50492e-3]
#noDiode = noDiode[noDiode["time"]<3.50536e-3]

#set base unit
time_unit = "ns"
time_fact = 10**9
#remove offset
time_offset = 0



fig, ax1 = plt.subplots()

#ax2 = ax1.twinx()
plt1 = ax1.plot(deadtime["dead"]*time_fact-time_offset, deadtime["i_max"], label = "max. Id(M4)",color = 'C4')

ax2.grid(False)

#ax1.set_ylabel('V/V')
ax1.set_ylabel('I/A')
ax1.set_xlabel(f"t/{time_unit}")


#Generate legend
# plots = plt1+plt2+plt3   #entry needs to be added for every plot
# labels = [l.get_label() for l in plots]
# ax1.legend(plots, labels, loc=0)
ax1.legend()
#ax2.legend()

ax1.get_xaxis().get_major_formatter().set_useOffset(True)

tikzplotlib_fix_ncols(fig)

# tikzplotlib.save('Diode.tex',
#     float_format = ".10g",
#     axis_width=r'\textwidth',
#     axis_height=r'0.3\textwidth')
  #  figure_width=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
  #  figure_height=fR'\linewidth/{n} - {n-1}/{n}*{sep}',
#    extra_tikzpicture_parameters={'trim axis group left', 'trim axis group right'},
#    extra_axis_parameters={"xtick={-0.5,-0.25,0,0.25,0.5}"},
#    extra_groupstyle_parameters={f'vertical sep={sep}em'})
plt.savefig("DeadtimeStepped.eps")
plt.show()