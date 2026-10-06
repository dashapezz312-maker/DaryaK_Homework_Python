def square(side):
    area = side * side
    if side % 1 != 0:
        area = int(area) + 1
    return area


side = 4.6
print(square(side))
