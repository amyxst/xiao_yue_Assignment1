from math import factorial

def main():
    n = 5
    k = 3
    #print gen_bin(5, 3)  
    gen_pascal(5)

def gen_bin(n, k):
    if k < 1:
        print "Invalid k."
    if k == 0:
        return 1
    else:
        n_fac = factorial(n)
        k_fac = factorial(k)
        nk_fac = factorial(n-k)
        #print n_fac, k_fac, nk_fac
        return int(n_fac / (k_fac*nk_fac))

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

if __name__ == "__main__":
    main()
