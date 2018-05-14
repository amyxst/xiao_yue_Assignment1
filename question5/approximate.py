import numpy as np
import matplotlib.pyplot as plt

def main():
    f = lambda x: x*(x-1)
    df = lambda f, x, delta: (f(x+delta) - f(x)) / delta
    df_1 = lambda delta: df(f, 1, delta)

    # sanity check
    #print f(3)
    #print df(f, 1, 0.001)
    
    # we find that the limit of the difference quotient
    # approaches 1 as delta approaches 0, at x=1
    plot_approximation(df_1, 10**(-4), 10**(-14))

def plot_approximation(df_1, lower_delta, upper_delta):
    vals = np.linspace(lower_delta, upper_delta, 13)
    
    plt.figure()
    plt.plot(vals, df_1(vals), 'bo')
    plt.title("5. Limit of difference quotient as $\delta$ -> 0, at x=1")
    plt.xlabel("$\delta$")
    plt.ylabel("limit as $\delta$ -> 0")
    plt.show()
    
if __name__ == "__main__":
    main()    
