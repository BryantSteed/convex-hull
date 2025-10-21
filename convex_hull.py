# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point
import operator

def compute_hull_dvcq(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    if len(points) <= 1:
        return points
    left_side, right_side = divide_points(points)
    left_hull = compute_hull_dvcq(left_side)
    right_hull = compute_hull_dvcq(right_side)
    assert left_hull
    assert right_hull
    merged_hull = merge_hulls(left_hull, right_hull)
    assert merged_hull
    return merged_hull

def merge_hulls(left_hull: list[tuple[float, float]], 
                right_hull: list[tuple[float, float]]) -> list[tuple[float, float]]:
    left_hull_start_index = left_hull.index(max(left_hull, key=lambda point: point[0]))
    right_hull_start_index = right_hull.index(min(right_hull, key=lambda point: point[0]))
    left_hull_ordered_clockwise = left_hull[left_hull_start_index:] + left_hull[:left_hull_start_index]
    right_hull_ordered_clockwise = right_hull[right_hull_start_index:] + right_hull[:right_hull_start_index]
    left_hull_ordered_counterclockwise = get_counterclockwise(left_hull_ordered_clockwise)
    right_hull_ordered_counterclockwise = get_counterclockwise(right_hull_ordered_clockwise)
    left_upper, right_upper = get_tangent(left_hull_ordered_counterclockwise, 
                                          right_hull_ordered_clockwise, "upper")
    left_lower, right_lower = get_tangent(left_hull_ordered_clockwise, 
                                          right_hull_ordered_counterclockwise, "lower")
    final_hull = extract_new_hull(left_hull_ordered_clockwise, right_hull_ordered_clockwise, 
                                  left_upper, right_upper, left_lower, right_lower)
    return final_hull

def extract_new_hull(left_hull, right_hull, left_upper, right_upper, left_lower, right_lower):
    left_hull_lower_first = left_hull[left_hull.index(left_lower):] + left_hull[:left_hull.index(left_lower)]
    right_hull_upper_first = right_hull[right_hull.index(right_upper):] + right_hull[:right_hull.index(right_upper)]
    spliced_left = left_hull_lower_first[left_hull_lower_first.index(left_lower):left_hull_lower_first.index(left_upper)+1]
    spliced_right = right_hull_upper_first[right_hull_upper_first.index(right_upper):right_hull_upper_first.index(right_lower)+1]
    return spliced_left + spliced_right

def get_tangent(left_hull, right_hull, tangent_type: str):
    left_terminal, right_terminal = get_terminals(tangent_type)
    current_line = (left_hull[0], right_hull[0])
    current_slope = compute_slope(current_line[0], current_line[1])
    left_index, right_index = 0, 0
    changed = True
    while changed:
        changed = False
        current_line, current_slope, left_index, changed = \
            process_rotation(left_hull, current_line, current_slope, 
                             left_index, changed, left_terminal, "left")
        current_line, current_slope, right_index, changed = \
            process_rotation(right_hull, current_line, current_slope, 
                             right_index, changed, right_terminal, "right")
    return current_line

def get_terminals(tangent_type):
    if tangent_type == "upper":
        left_terminal = operator.gt
        right_terminal = operator.lt
    elif tangent_type == "lower":
        left_terminal = operator.lt
        right_terminal = operator.gt
    else:
        raise ValueError("tangent_type must be 'upper' or 'lower'")
    return left_terminal,right_terminal

def process_rotation(hull, current_line, current_slope, index, changed, terminal_case, hull_side: str):
    for i in range(index+1, len(hull)):
        if hull_side == "left":
            new_line = (hull[i], current_line[1])
        else:
            new_line = (current_line[0], hull[i])
        new_slope = compute_slope(new_line[0], new_line[1])
        if terminal_case(new_slope, current_slope):
            break
        current_line = new_line
        current_slope = new_slope
        index = i
        changed = True
    return current_line, current_slope, index, changed

def compute_slope(point1, point2):
    if point2[0] - point1[0] == 0:
        return float('inf')
    return (point2[1] - point1[1]) / (point2[0] - point1[0])

def get_counterclockwise(hull: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(hull) == 1:
        return hull
    return [hull[0]] + list(reversed(hull[1:]))

def is_tangent(tangent_type: str, left_point, right_point, hull):
    assert tangent_type in ("upper", "lower")
    if tangent_type == "upper":
        func = lambda left, right: left > right
    elif tangent_type == "lower":
        func = lambda left, right: left < right
    m = (right_point[1] - left_point[1]) / (right_point[0] - left_point[0])
    b = left_point[1] - (m * left_point[0])
    for point in hull:
        if point == left_point or point == right_point:
            continue
        y_on_line = m * point[0] + b
        if func(point[1], y_on_line):
            return False
    return True


def divide_points(points: list[tuple[float, float]]) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    sorted_points = sorted(points, key=lambda point: point[0])
    mid = len(sorted_points) // 2
    return sorted_points[:mid], sorted_points[mid:]


def compute_hull_other(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    return []
