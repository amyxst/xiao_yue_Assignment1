from scipy import integrate
from scipy.special import jv
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Part a)
    #print("a) Implementing Bessel function of the first kind of order, x=4")
    #print "Implemented routine result: ", bessel(1,4) 
    #print "Scipy result: ", jv(1,4)
    
    #plot_bessel()

    # Part b)
    #print point_spread_x(np.linspace(-1,1), 0.3)
    #print point_spread_x(-1, 0.3)
    #plot_point_spread()
    #show_point_spread_img()

    # Part c)
    #convolve_img("proxima_centauri.jpg")
    pass

def bessel(m, x):
    f = lambda theta: math.cos(m*theta - x*math.sin(theta))
    return (1 / math.pi) * integrate.quad(f, 0, math.pi)[0]

def plot_bessel(m_range=[0,5], x_range=[-10,10]):
    plt.figure()

    x = np.linspace(x_range[0], x_range[1], 500)
    y_f = np.vectorize(bessel)
    
    for m in xrange(m_range[0], m_range[1]+1):
        plt.plot(x, y_f(m, x), label="m = {0}".format(m))

    plt.title("a) Bessel function behaviour of the first kind of order m for selected x")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("$J_m(x)$")
    plt.show()

def ps_x(q, a=0.1, lmda=0.1, R=0.7):
    return (2*math.pi*a*q)/(lmda*R)

def point_spread(q, Inaut=40):
    x = ps_x(q)
    return Inaut*((2*bessel(1,x))/x)**2

def plot_point_spread():
    q = np.linspace(-0.3, 0.3, 300)
    ps_y = np.vectorize(point_spread)

    x = ps_x(q)
    y = ps_y(x)

    plt.figure()
    plt.title("b) Point Spread Function")
    plt.xlabel("x")
    plt.ylabel("I(x)")
    plt.plot(x, y)
    plt.show()

def point_spread_img_vals():
    q = np.linspace(-0.3, 0.3, 300)
    x = ps_x(q)

    xv, yv = np.meshgrid(x, x)

    # combine xv, yv and convert to positive values
    grid = xv**2 + yv**2

    ps_vec = np.vectorize(point_spread)
    return ps_vec(grid)

def show_point_spread_img():
    img_vals = point_spread_img_vals()

    plt.figure()
    plt.title("b) Point Spread Function Rendering")
    plt.imshow(np.sqrt(img_vals), cmap='binary', extent=(-0.3, 0.3, -0.3, 0.3))
    plt.show()    

if __name__ == "__main__":
    main()
