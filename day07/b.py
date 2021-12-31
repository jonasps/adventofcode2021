with open("day.txt") as f:
    crabs = [int(x) for x in f.readlines()[0].split(',')]
    levels = {}
    for level in range(min(crabs), max(crabs)+1):
        levels[level] = sum([sum([x for x in range(0, abs(x - level)+1)]) for x in crabs])

    best = min(levels, key=levels.get)
    print(levels[best])