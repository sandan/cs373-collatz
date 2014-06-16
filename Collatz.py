#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

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
    m=k/2
    """optimization 2
       let i,j natural numbers
       if i<=j and i < j/2 then 
         collatz_eval(i,j)=collatz_eval(j/2,j)
    """
    if (i < m):
        return collatz_eval(m,k)

    assert i <= k

    while( k >= i):
        result=cycle_length(k)
        if (c_len < result) :
            c_len=result
        k-=1
    assert c_len >0
    return c_len

# -------------
# cycle_length
# -------------
def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
            c+=1
        else : #calculates (3n+1)/2
            n = n + (n>>1) + 1
            c += 2
    assert c > 0
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
