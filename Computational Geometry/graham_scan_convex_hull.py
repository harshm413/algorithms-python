import math

def graham_scan(points):
    # Find the point with the lowest y-coordinate, break ties by x-coordinate
    pivot = min(points, key=lambda p: (p[1], p[0]))
    points.remove(pivot)

    # Sort the points based on polar angle with the pivot
    points.sort(key=lambda p: (math.atan2(p[1] - pivot[1], p[0] - pivot[0]), p[1], p[0]))

    # Add the pivot back to the beginning
    points.insert(0, pivot)

    # Initialize the hull with the first two points
    hull = [points[0], points[1]]

    for p in points[2:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)

    return hull

def orientation(p, q, r):
    # Function to find the orientation of the triplet (p, q, r)
    # 0 -> p, q, and r are collinear
    # 1 -> Clockwise
    # 2 -> Counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

# Sample points
points = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2), (0.5, 2.5), (2.5, 2)]

# Call the function
convex_hull = graham_scan(points)

# Print the result
print("Convex Hull:", convex_hull)
