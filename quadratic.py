# quadratic_weather_modeling
import math

a = 1
b = -3
c = 2

d = b**2 - 4*a*c
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", x1, "and", x2)
else:
    print("No real roots")
