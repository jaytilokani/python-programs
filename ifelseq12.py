x = int(input("Enter x-coordinate of center: "))
y = int(input("Enter y-coordinate of center: "))
r = int(input("Enter radius: "))

px = int(input("Enter x-coordinate of point: "))
py = int(input("Enter y-coordinate of point: "))

d = (px - x) ** 2 + (py - y) ** 2
r2 = r ** 2

if d < r2:
    print("Point lies inside the circle")
elif d == r2:
    print("Point lies on the circle")
else:
    print("Point lies outside the circle")