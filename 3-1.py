# Advent of Code 2017 - Problem 1, Day 3
########################################
# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
# They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

input = 277678

def find_manhattan_distance(secret_num):
    layer = 0
    side_length = 1
    # find spiral layer that contains secret num
    while secret_num > side_length ** 2:
        layer += 1
        side_length += 2

    if layer == 0:
        return 0
    
    # find corners of the square that contains secret num
    corner_calc = side_length - 1
    corner1 = side_length ** 2 # start with bottom right corner and go clockwise around square
    corner2 = (corner1 - corner_calc)
    # find side of the square that contains secret num
    while secret_num <= corner2:
        corner1 = corner2
        corner2 = (corner1 - corner_calc)
    # find distance from mid point of the square
    mid = corner2 + (side_length//2)
    if secret_num == mid:
        return layer
    dist_from_mid = abs(secret_num - mid)
    
    return layer + dist_from_mid


# For testing:
#################
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
print("Answer: " + str(find_manhattan_distance(1)) + ' - this should be layer 0')
print("Answer: " + str(find_manhattan_distance(12)) + ' - this should be layer 3')
print("Answer: " + str(find_manhattan_distance(23)) + ' - this should be layer 2')
print("Answer: " + str(find_manhattan_distance(input)) + ' - this should be your final answer')
