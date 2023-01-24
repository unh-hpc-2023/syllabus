#! /usr/bin/env python

import numpy
from numpy import *
from pylab import *
import matplotlib as mpl
from matplotlib.collections import LineCollection

def ic_sin(x, y):
    rho = y[:,0]; mom = y[:,1]
    rho[1:-1] = 1. + 1e-3 * sin(2*pi * x[1:-1])
    mom[1:-1] = 0.

def ic_gauss(x, y):
    rho = y[:,0]; mom = y[:,1]; T = y[:,2]
    rho[1:-1] = 1. + 1e-3 * exp(-(x[1:-1]-1.)**2 / (2. * .2**2))
    mom[1:-1] = 0.1 * rho[1:-1]
    T  [1:-1] = 1.

def ic_gauss_adv(x, y):
    rho = y[:,0]; mom = y[:,1]; T = y[:,2]
    rho[1:-1] = 1. + 1e-3 * exp(-(x[1:-1]-1.)**2 / (2. * .2**2))
    mom[1:-1] = rho[1:-1]
    T  [1:-1] = 1. - 1e-3 * exp(-(x[1:-1]-1.)**2 / (2. * .2**2))

def ic_gauss_adv_left(x, y):
    rho = y[:,0]; mom = y[:,1]; T = y[:,2]
    rho[1:-1] = 1. + 1e-3 * exp(-(x[1:-1]-1.)**2 / (2. * .2**2))
    mom[1:-1] = - rho[1:-1]
    T  [1:-1] = 1. - 1e-3 * exp(-(x[1:-1]-1.)**2 / (2. * .2**2))

######################################################################

class Problem:
    pass

######################################################################

def bc(x):
    x[0 ,:] = x[-2,:]
    x[-1,:] = x[1 ,:]
    
def fl_avg(s):
    flux = empty_like(s)
    flux[1:-1] = .5*(s[0:-2] + s[1:-1])
    return flux

def fl_zip(s1, s2):
    flux = empty_like(s1)
    flux[1:-1] = .5*(s1[0:-2] * s2[1:-1] + s1[1:-1] * s2[0:-2])
    return flux

def fl_adv_zip(v, s):
    return fl_zip(v, s)

def fl_adv_upwind(v, s):
    flux = empty_like(s)
    v_face = (v[0:-2] * s[1:-1] + v[1:-1] * s[0:-2]) / (s[0:-2] + s[1:-1])
    flux[1:-1] = v_face * ((v_face > 0) * s[0:-2] + (v_face < 0) * s[1:-1])
    return flux

def fl_adv_upwind2(v, s):
    flux = empty_like(s)
    v_face = .5 * (v[0:-2] + v[1:-1])
    flux[1:-1] = v_face * ((v_face > 0) * s[0:-2] + (v_face < 0) * s[1:-1])
    return flux

def divg(fl, dx):
    fl[-1] = fl[1 ]
    return (fl[2:] - fl[1:-1]) / dx

######################################################################
    
def yderiv(x, y, problem):
    yd = empty_like(y)
    dx = x[1] - x[0]
    
    bc(y)
    rho = y[:,0]; mom = y[:,1]; T = y[:,2]; vel = mom / rho

    fl_rho = problem.fl_adv_rho(vel, rho)
    yd[1:-1,0] = - divg(fl_rho, dx)

    fl_T = problem.fl_adv_T(vel, T)
    fl_vel = fl_avg(vel)
    yd[1:-1,2] = - (divg(fl_T, dx) +
                    (problem.gam - 2.) * T[1:-1] * divg(fl_vel, dx))

    fl_mom = problem.fl_adv_mom(vel, mom) + fl_zip(rho, T)
    yd[1:-1,1] = - divg(fl_mom, dx)

    return yd

######################################################################

def step_euler(x, y, dt, problem):
    yd = yderiv(x, y, problem)
    y += dt * yd

def step_rk2(x, y, dt, problem):
    yd = yderiv(x, y, problem)
    ym = y + .5*dt * yd
    yd = yderiv(x, ym, problem)
    y += dt * yd

def integrate(x, y, dt, step, problem):
    mx, mm = y.shape
    out = empty((mx, mm+1))
    out[:,0] = x
    out[:,1:] = y
    for i, t in enumerate(arange(0, 2., dt)):
        step(out[:,0], out[:,1:], dt, problem)
        numpy.save("data_%d.npy" % i, out)
     
def run(ic, step, problem):
    ion()

    cfl = .25
    mx = 30
    dx = 2. / mx
    dt = cfl * dx
    x = empty((mx+2))
    x[1:] = linspace(0,2.,mx+1)
    x[0] = 2*x[1] - x[2]
    y = empty((mx+2,3))
    ic(x, y)

    integrate(x, y, dt, step, problem)

def test1():
    problem = Problem()
    problem.gam        = 5./3.
    problem.fl_adv_rho = fl_adv_upwind
    problem.fl_adv_T   = fl_adv_upwind
    problem.fl_adv_mom = fl_adv_zip
    run(ic_gauss_adv, step_rk2, problem) 

def test2():
    problem = Problem()
    problem.gam        = 5./3.
    problem.fl_adv_rho = fl_adv_upwind
    problem.fl_adv_T   = fl_adv_upwind
    problem.fl_adv_mom = fl_adv_zip
    run(ic_gauss_adv_left, step_rk2, problem) 

def test3():
    problem = Problem()
    problem.gam        = 1.#5./3.
    problem.fl_adv_rho = fl_adv_zip
    problem.fl_adv_T   = fl_adv_zip
    problem.fl_adv_mom = fl_adv_zip
    run(ic_gauss, step_rk2, problem) 

def test4():
    problem = Problem()
    problem.gam        = 1.#5./3.
    problem.fl_adv_rho = fl_adv_upwind
    problem.fl_adv_T   = fl_adv_upwind
    problem.fl_adv_mom = fl_adv_upwind2
    run(ic_gauss, step_rk2, problem) 

test4()

