# Determine in which quadrant the point P(x, y) is located

x = int(input("x = "))
y = int(input("y = "))

# Check if point is at origin
if x == 0 and y == 0:
    print("Point P(0,0) is at the origin of the coordinate system")
# Check axes
elif x == 0:
    print("Point P(0,{}) is on the Y axis".format(y))
elif y == 0:
    print("Point P({},{}) is on the X axis".format(x, 0))
# Check quadrants
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
else:  # x > 0 and y < 0
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")