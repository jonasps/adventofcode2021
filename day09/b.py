
def chech_adjacent(x, y):
    yield (min(x + 1, max_x), y)
    yield (max(x - 1, 0), y)
    yield (x, max(y-1, 0))
    yield (x, min(y+1, max_y))

rows = []
coordinates = set()
max_y = None
max_x = None
with open("day.txt") as f:
    values = 0
    rows = [x.strip() for x in f.readlines()]
    max_x = len(rows[0]) - 1
    max_y = len(rows) -1
    for y, row in enumerate(rows, 0):
        for x, char in enumerate(row, 0):
            if char != '9':
                coordinates.add((x, y))

all = []
result = []
for (x,y) in coordinates:
    seen = []
    findings = [(x,y)]
    positive = []
    while findings:
        (x_, y_) = findings.pop()
        for (x1,y1) in chech_adjacent(x_, y_):
            if rows[y1][x1] == '9':
                pass
            elif (x1,y1) not in seen:
                findings.append((x1,y1))
                positive.append((x1,y1))
            seen.append((x1,y1))
    if sorted(positive) not in all:
        all.append(sorted(positive))
        result.append(len(positive))


longest_basins = sorted(result, reverse=True)
print(longest_basins[0] * longest_basins[1] * longest_basins[2])