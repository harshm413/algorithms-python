import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def closest_pair_2d(points):
    def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
        n = len(points_sorted_by_x)
        
        if n <= 3:
            return brute_force_closest_pair(points_sorted_by_x)
        
        mid = n // 2
        left_half_x = points_sorted_by_x[:mid]
        right_half_x = points_sorted_by_x[mid:]
        
        midpoint = points_sorted_by_x[mid][0]
        left_half_y = list(filter(lambda x: x[0] <= midpoint, points_sorted_by_y))
        right_half_y = list(filter(lambda x: x[0] > midpoint, points_sorted_by_y))
        
        (p1, q1, d1) = closest_pair_recursive(left_half_x, left_half_y)
        (p2, q2, d2) = closest_pair_recursive(right_half_x, right_half_y)
        
        if d1 < d2:
            d = d1
            min_pair = (p1, q1)
        else:
            d = d2
            min_pair = (p2, q2)
        
        (p3, q3, d3) = closest_split_pair(points_sorted_by_x, points_sorted_by_y, d, min_pair)
        
        if d3 < d:
            return (p3, q3, d3)
        else:
            return min_pair[0], min_pair[1], d

    def brute_force_closest_pair(points):
        min_dist = float('inf')
        p1 = None
        p2 = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = distance(points[i], points[j])
                if d < min_dist:
                    min_dist = d
                    p1, p2 = points[i], points[j]
        return p1, p2, min_dist

    def closest_split_pair(points_sorted_by_x, points_sorted_by_y, delta, best_pair):
        n = len(points_sorted_by_x)
        mid_x = points_sorted_by_x[n // 2][0]
        
        Sy = [point for point in points_sorted_by_y if mid_x - delta <= point[0] <= mid_x + delta]
        
        best = delta
        len_Sy = len(Sy)
        for i in range(len_Sy - 1):
            for j in range(i + 1, min(i + 7, len_Sy)):
                p, q = Sy[i], Sy[j]
                dst = distance(p, q)
                if dst < best:
                    best = dst
                    best_pair = (p, q)
        return best_pair[0], best_pair[1], best
    
    points_sorted_by_x = sorted(points, key=lambda x: x[0])
    points_sorted_by_y = sorted(points, key=lambda x: x[1])
    
    p1, p2, min_dist = closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)
    return p1, p2, min_dist

# Example usage
points = [(2, 3), (2,4), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_points = closest_pair_2d(points)
print(f"The closest pair of points is: {closest_points[0]} and {closest_points[1]} with a distance of {closest_points[2]}")
