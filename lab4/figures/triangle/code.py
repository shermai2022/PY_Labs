import math
__a = 7
__b = 2
__c = 8
def triangle_perimeter(a=__a,b=__b,c=__c):
    P = a + b + c
    print(P)
triangle_perimeter()
def triangle_area(a=__a,b=__b,c=__c):
    p = (__a+__b+__c)/2
    A = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(A)
triangle_area()

