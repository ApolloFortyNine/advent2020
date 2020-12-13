f = open('input.txt')
lines = f.readlines()
forest = []

for line in lines:
    line = line.strip()
    forest.append(line)

forest_width = len(line)
y = 0
x = 0
trees = 0


# Modulo this
while y < len(forest) - 1:
    x += 3
    y += 1
    fitted_x = x % forest_width
    if (forest[y][fitted_x] == '#'):
        trees += 1
print(trees)



