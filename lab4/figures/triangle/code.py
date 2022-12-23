def triangle_perimeter(a = 7, b = 2, c = 8):
    peri = a + b + c
    print(peri)
    return
    
    
    
def triangle_area(a = 7, b = 2, c = 8):
    S = (a + b + c)/2
    A = (S - a) * (S - b) * (S - c) * S
    A = A**0.5
    print(A)
    return
