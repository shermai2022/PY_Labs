A = [1,0,4,7,1,9,5,3]

def swap_min(A):
    a = max(A)
    b = min(A)
    A[A.index(a)] = b
    A[A.index(b)] = a
    
    print (A)
    
    
swap_min(A)
