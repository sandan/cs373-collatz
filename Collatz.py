#!/usr/bin/env python3

# ---------------------------
# Copyright (C) 2014
# Mark Sandan
# ---------------------------

# ------------
# The cache implementation is simply an array.
# cache[i] returns the cycle_length of i.
# Since the Collatz inputs are > 0, but the cache 
# is zero-indexed, the nth entry is read[n-1] and
# similarly for write.
#
# see cycle_length for details on usage 
# ------------
class Cache:
    def __init__(self,size):
        self.cache=[0]*size
    # -------------
    # write_cache
    # -------------
    
    def write(self,i,val):
        try:
            assert i > 0
            if (self.cache[i-1] > 0): #then already wrote val
                return
        
            self.cache[i-1]=val
        
        except IndexError:
            pass
    
   
    # -------------
    #  read_cache
    # -------------
    
    def read(self,i):
        try:
            assert i > 0
            return self.cache[i-1]
      
        except IndexError:
            return 0
    
    def size(self):
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
    """
    # <your code>
    assert i > 0
    assert j > 0
   
    c_len=0
    result=0
    k=max(i,j)
    i=min(i,j)
    m=k>>1
    """optimization 2
       let i,j natural numbers
       if i<=j and i < j/2 then 
         collatz_eval(i,j)=collatz_eval(j/2,j)
    """
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
