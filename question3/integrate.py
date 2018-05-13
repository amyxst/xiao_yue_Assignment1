from scipy import integrate
from scipy.special import jv
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Part a)
    print("a) Implementing Bessel function of the first kind of order, x=4")
    print "Implemented routine result: ", bessel(1,4) 
    print "Scipy result: ", jv(1,4)

    plot_bessel()

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

if __name__ == "__main__":
    main()
