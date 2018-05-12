from math import factorial

def main():
    n = 5
    k = 3
    print "a) 5C3"
    print gen_bin(5, 3)  
    #gen_pascal(5)
    print "b) print first 5 lines of Pascal's triangle"
    gen_pascal2(5)
    print "c) p=0.25, n=4, k=1"
    get_probability(0.25, 4, 1)

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

if __name__ == "__main__":
    main()
