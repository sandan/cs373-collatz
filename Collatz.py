#!/usr/bin/env python3

# ---------------------------
# Copyright (C) 2014
# Mark Sandan
# ---------------------------
class Cache:

    """
    The Cache object is initialized with an integer that
    determines the size of the cache.

    The cache is an object that keeps a list.
    It has basic read and write functions as well
    as a size function.

    Since the Collatz inputs are > 0, but the cache 
    is zero-indexed, the nth entry is read[n-1] and
    similarly for write.
       

    see cycle_length and collatz_eval for details on usage 
    """ 
    def __init__(self,size):
        self.cache=[0]*size
    # -------------
    # write_cache
    # -------------
    
    def write(self,i,val):
	"""
	The write method takes an index i as input as 
	well as value val to write in index i.
	
	An assertion is placed to make sure i > 0.
	
	A try block is used in case an IndexError exception
	is raised. In case it is raised, the write to the
	cache fails and the cache is not modified and no 
	value is returned.
	
	Otherwise, the cache is modified by writing val to 
	cache[i-1]. Again, no value is returned.
	"""
	

        assert i > 0
        try:
            if (self.cache[i-1] > 0): #then already wrote val
                return
        
            self.cache[i-1]=val
        
        except IndexError:
            pass
    
   
    # -------------
    #  read_cache
    # -------------
    def read(self,i):

    	"""
    	The read method takes an index i as input.
    	An assertion is placed to make sure i > 0.
        A try block is used to return whatever is
        in the ith index of the cache. Since the cache
        is implemented as a list, the i-1 th element
        is indexed and returned.

        If an IndexError exception is raised,
        it is caught and the value 0 is returned instead.
        """

        assert i > 0
        try:
            return self.cache[i-1]
      
        except IndexError:
            return 0
   
    def size(self):

        """
    	The size method takes no arguments and simply returns
    	the length of the cache (i.e. len(cache))
    	"""
    
        return len(self.cache)
                

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """

    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    
    implements optimization 2 which halves the space
    of cycle_length calculations:
       let i,j natural numbers
       if i<=j and i < j/2 then 
         collatz_eval(i,j)=collatz_eval(j/2,j)

    cache usage:
      An empty cache is instantiated here with size k
      which is the maximim of the inputs i,j given.
      Thus the cache will contain indices from 0 to k-1. 
      The cache is passed to the cycle_length function
      which uses it to look up and write to the cache.
    """
    # <your code>
    assert i > 0
    assert j > 0
   
    c_len=0
    result=0
    k=max(i,j)
    i=min(i,j)
    m=k>>1

    if (i < m):
        return collatz_eval(m,k)

    assert i <= k

    #initialize a cold cache
    cache = Cache(k)
    assert cache.size() == k

    while( k >= i):
        result=cycle_length(k,cache)
        if (c_len < result) :
            c_len=result
        k-=1
    assert c_len > 0
    return c_len

# -------------
# cycle_length
# -------------
def cycle_length (n,cache) :

    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros

    implements optimization 1 which combines two steps of the 
    collatz algorithm into one whenever n is odd by
    calculating n = n + (n>>1) +1. The cycle length c_len
    is incremented accordingly.

    cache usage:
     Before the cycle length is actually calculated,
     it will first read the cache to obtain the value in 
     the nth index. If there is no such value, 0 is returned
     since the cache is intialized to 0.
     Otherwise if there is a cache hit then the cycle length
     is adjusted accordingly and the cache is written to 
     accordingly with that value. The value is then returned.

     In any case once the cycle_length calculation is done,
     the cache is written to.
    """


    assert n > 0
    c = 1
    m = n
    
    while n > 1 :
        x = cache.read(n)
        if (x > 0):
            c = (c + x) - 1
            assert c > 0
            cache.write(m,c)
            return c

        if (n % 2) == 0 :
            n = (n >> 1)
            c+=1
        else : #calculates (3n+1)/2
            n = n + (n>>1) + 1
            c += 2
    assert c > 0
    cache.write(m,c)
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
