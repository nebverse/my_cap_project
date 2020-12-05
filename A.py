import math

print("Enter radius")
r=float(input())

print("Radius of the circle:" + str(r))

b=math.pi

area = b*(r**2)

print("The area of circle with radius {} is:{}".format(r,area))