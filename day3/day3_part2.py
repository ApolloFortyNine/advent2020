f = open('input.txt')
lines = f.readlines()
forest = []

for line in lines:
    line = line.strip()
    forest.append(line)

def traverse_forest(right, down):
    forest_width = len(line)
    y = 0
    x = 0
    trees = 0


    # Modulo this
    while y < len(forest) - 1:
        x += right
        y += down
        fitted_x = x % forest_width
        if (forest[y][fitted_x] == '#'):
            trees += 1
    return(trees)

x1 = traverse_forest(1, 1)
x2 = traverse_forest(3, 1)
x3 = traverse_forest(5, 1)
x4 = traverse_forest(7, 1)
x5 = traverse_forest(1, 2)
print(x1*x2*x3*x4*x5)


