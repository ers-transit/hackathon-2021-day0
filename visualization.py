import batman
import numpy as np
import matplotlib.pyplot as plt

def plot_lightcurve(rp=0.1, a=15.0, inc=87.0, **kw):
    params = batman.TransitParams()
    params.t0 = 0.                       #time of inferior conjunction
    params.per = 1.                      #orbital period
    params.rp = rp                      #planet radius (in units of stellar radii)
    params.a = a                       #semi-major axis (in units of stellar radii)
    params.inc = inc                     #orbital inclination (in degrees)
    params.ecc = 0.                      #eccentricity
    params.w = 90.                       #longitude of periastron (in degrees)
    params.u = [0.1, 0.3]                #limb darkening coefficients [u1, u2]
    params.limb_dark = "quadratic"       #limb darkening model

    t = np.linspace(-0.05, 0.05, 1000)

    m = batman.TransitModel(params, t)    #initializes model
    flux = m.light_curve(params)          #calculates light curve

    # plot the light curves
    plt.plot(t, flux, **kw)
    plt.xlabel("Time from central transit")
    plt.ylabel("Relative flux")
