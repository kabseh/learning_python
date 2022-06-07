
from math import sqrt


print(" (a * x ^ 2) + b*2 + c")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + (r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("we have two solutions: %f and %f" % (x1, x2))
elif r == 1:
    num_roots = 1
    x = ((-b) / 2*a)
    print("we have solution: ", x)
else:
    num_roots = 0
    print("No solutions, because < 0")
    exit()
