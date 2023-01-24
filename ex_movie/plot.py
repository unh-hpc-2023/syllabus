#! /usr/bin/env python

import numpy
from numpy import *
from pylab import *

def plot_file(filename_in, filename_out):
    data = numpy.load(filename_in)

    plot(data[1:-1,0], data[1:-1,1])
    ylim(1., 1.001)
    savefig(filename_out)

import sys

if len(sys.argv) != 3:
    print("usage: plot.py datafile.npy outputfile.png")
    sys.exit(1)

plot_file(sys.argv[1], sys.argv[2])
