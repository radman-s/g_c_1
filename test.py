import math


def qt_side(a,b):

    aa = b/(2 * a) * math.sqrt(4*a**2-b**2)
    return aa

print(qt_side(34, 48))