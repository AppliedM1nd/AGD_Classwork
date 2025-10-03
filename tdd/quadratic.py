import cmath
import math

def solve_quadratic(a, b, c):
    if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
        return 'Please enter a number for a,b and c'
    if a == 0:
        return 'a must not equal 0 in a quadratic'
    dis = (b ** 2) - (4 * a * c)
    if dis < 0:
        root1 = (-b - cmath.sqrt(dis)) / (2 * a)
        root2 = (-b + cmath.sqrt(dis)) / (2 * a)
        return root1, root2
    elif dis == 0:
        root = (-b) / (2 * a)
        return root
    else:
        root1 = (-b - math.sqrt(dis)) / (2 * a)
        root2 = (-b + math.sqrt(dis)) / (2 * a)
        return root1, root2
print(solve_quadratic(1,4,5))