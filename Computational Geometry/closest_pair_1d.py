def closest_pair_1d(points):
    """
    Find the closest pair of points in a 1-dimensional list of points using divide and conquer approach.
    Parameters:
    points (list): A list of integers representing points on the x-axis.
    Returns:
    tuple: A tuple containing the two closest points.
    """
    def find_closest_pair(sorted_points):
        # Base case: If there are only two points, return them
        if len(sorted_points) == 2:
            return sorted_points[0], sorted_points[1]
        # Base case: If there are three points, return the closest pair
        if len(sorted_points) == 3:
            return min(
                ((sorted_points[0], sorted_points[1]),
                 (sorted_points[1], sorted_points[2]),
                 (sorted_points[0], sorted_points[2])),
                key=lambda pair: abs(pair[1] - pair[0])
            )
        # Divide the points into two halves
        mid = len(sorted_points) // 2
        left_half = sorted_points[:mid]
        right_half = sorted_points[mid:]
        # Find the closest pair in each half
        closest_pair_left = find_closest_pair(left_half)
        closest_pair_right = find_closest_pair(right_half)
        # Find the closest pair across the split
        closest_pair_split = (left_half[-1], right_half[0])
        # Return the overall closest pair
        return min(closest_pair_left, closest_pair_right, closest_pair_split, key=lambda pair: abs(pair[1] - pair[0]))

    if len(points) < 2:
        raise ValueError("At least two points are required")
    # Sort the points
    sorted_points = sorted(points)
    # Find the closest pair using divide and conquer
    return find_closest_pair(sorted_points)

# Example usage
points = [0,1,3,5,7,9,11]
closest_points = closest_pair_1d(points)
print(f"The closest pair of points is: {closest_points}")