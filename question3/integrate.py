from scipy import integrate
from scipy.special import jv
import math
import numpy as np

def main():
    print("a) Implementing Bessel function of the first kind of order, x=4")
    print "Implemented routine result: ", bessel(1,4) 
    print "Scipy result: ", jv(1,4)

def bessel(m, x):
    f = lambda theta: math.cos(m*theta - x*math.sin(theta))
    return (1 / math.pi) * integrate.quad(f, 0, math.pi)[0]

if __name__ == "__main__":
    main()
