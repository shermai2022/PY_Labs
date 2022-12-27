import math
__default_radius = 5
def circle_perimeter(radius=__default_radius):
    C = 2*math.pi*radius
    print(C)
def circle_area(radius=__default_radius):
    A = math.pi*pow(radius, 2)
    print(A)
