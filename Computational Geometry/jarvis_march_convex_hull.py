def gift_wrapping(points):
    hull = []
    start = min(points, key=lambda p: p[0])  # Find the leftmost point
    on_hull = start
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for p in points:
            if (next_point == on_hull) or (orientation(on_hull, next_point, p) == 2):
                next_point = p
        on_hull = next_point
        if on_hull == start:
            break
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
convex_hull = gift_wrapping(points)

# Print the result
print("Convex Hull:", convex_hull)
