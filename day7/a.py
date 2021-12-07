with open("day.txt") as f:
    crabs = [int(x) for x in f.readlines()[0].split(',')]
    levels = {}
    for level in range(min(crabs), max(crabs)+1):
        levels[level] = sum([abs(x - level) for x in crabs])

    best = min(levels, key=levels.get)
    print(levels[best])