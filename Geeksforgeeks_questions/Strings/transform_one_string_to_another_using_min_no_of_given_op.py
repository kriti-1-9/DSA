# brute force

def transform(A, B):
    if len(A) != len(B):
        return -1
    m = {}
    n = len(A)
    for i in range(n):
        if A[i] in m:   
            m[A[i]] += 1  
        else:
            m[A[i]] = 1   
    for i in range(n):
        if B[i] in m:
            m[B[i]] -= 1
    for key in m:
        if m[key] != 0:  
            return -1
    i, j = n-1, n-1
    res = 0
    while i >= 0 and j >= 0:
        while i >= 0 and A[i] != B[j]:
            res += 1  
            i -= 1    
        i -= 1
        j -= 1
    return res

# Another approach

def minOps(A, B):
    m = len(A)
    n = len(B)
    if n != m:
        return -1
    count = [0] * 256
    for i in range(n):        
        count[ord(B[i])] += 1
    for i in range(n):        
        count[ord(A[i])] -= 1
    for i in range(256):    
        if count[i]:
            return -1
    res = 0
    i = n-1
    j = n-1    
    while i >= 0:
        while i>= 0 and A[i] != B[j]:
            i -= 1
            res += 1
        if i >= 0:
            i -= 1
            j -= 1
    return res