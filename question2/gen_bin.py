from math import factorial
import random
import numpy as np
import matplotlib.pyplot as plot

def main():
    n = 5
    k = 3
    print "a) 5C3"
    print gen_bin(5, 3)  
    #gen_pascal(5)
    print "\nb) print first 5 lines of Pascal's triangle"
    gen_pascal2(5)
    print "\nc) p=0.25, n=4, k=1"
    get_probability(0.25, 4, 1)
    print "\nd) simulating trials, p=0.7 for heads"
    simulate(0.7)

def gen_bin(n, k):
    if k == 0:
        return 1 
    if k < 1:
        #print "Invalid k."
        return
    #if k == 0:
    #    return 1
    else:
        n_fac = factorial(n)
        k_fac = factorial(k)
        nk_fac = factorial(n-k)
        #print n_fac, k_fac, nk_fac
        return int(n_fac / (k_fac*nk_fac))

def gen_pascal2(n_lines):
    for line in xrange(n_lines):
        print "line ", line
        for e in xrange(line+1):
            print(gen_bin(line, e))
       
def gen_pascal(n_lines):
    triangle = [[] for line in xrange(n_lines)]

    for l, line in enumerate(triangle):
        print "line ", l
        for e in xrange(l+1):
            #print l, e
            triangle[l].append(-1)
            if e is 0:
                triangle[l][e] = 1
 	    elif e is l:
                triangle[l][e] = 1
            else:
                #print "indices ", l, e
                triangle[l][e] = triangle[l-1][e-1] + triangle[l-1][e]
            print triangle[l][e] 
        
        #print "\n"

def get_probability(p, n, k):
    print "Probability is ",  gen_bin(n, k)*(p**k)*((1-p)**(n-k))

def flip(n, p):
    if p > 1:
        print "Invalid probability"
        return
    flips = [1 if random.random() <= p else 0 for i in xrange(n)]
    #print len(flips)
    #print flips
    return [flips.count(1), flips.count(0)]
    
def simulate(p):
    flip_10 = flip(10, p)
    success_10 = float(flip_10[0])/10

    flip_100 = flip(100, p)
    success_100 = float(flip_100[0])/100
    
    flip_1000 = flip(1000, p)
    success_1000 = float(flip_1000[0])/1000

    print "10 flips | Heads: {}, Tails: {}".format(flip_10[0], flip_10[1])
    print "100 flips | Heads: {}, Tails: {}".format(flip_100[0], flip_100[1])
    print "1000 flips | Heads: {}, Tails: {}".format(flip_1000[0], flip_1000[1])
    
    x = np.arange(3)
    plot.bar(x, height=[success_10, success_100, success_1000])
    plot.bar(x, color="r", height=[1-success_10, 1-success_100, 1-success_1000], bottom=[success_10, success_100, success_1000])
    plot.xticks([],['10','100','1000'])
    plot.ylabel("Probability of Landing Heads")
    plot.title("d) Percentage of Heads for 10, 100 and 1000 Trials")
    plot.show()

if __name__ == "__main__":
    main()
