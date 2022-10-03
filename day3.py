# Slope is actually backwards
def check_slope(grid, slope):
    gridSize = len(grid[0])
    posX = posY = 0
    trees = 0

    for row in grid:
        if posY >= len(grid):
            break

        if grid[posY][posX % gridSize] == "#":
            trees += 1

        posX += slope if slope > 1 else 1
        posY += 1 if slope > 1 else int(1 / slope)

    return trees


grid = []

with open("inputs/day3.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

total = 1
slopes = [1, 3, 5, 7, 0.5]

for slope in slopes:
    total *= check_slope(grid, slope)

print(total)
