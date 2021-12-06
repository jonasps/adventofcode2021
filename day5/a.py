import re
from collections import Counter
input = [[int(x) for x in re.split(r" -> |,", x.strip())] for x in open("day.txt").readlines()]
all_coo = []
for a in input:
    x1 = a[0]
    y1 = a[1]
    x2 = a[2]
    y2 = a[3]
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            all_coo.append((x1, i))
                
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            all_coo.append((i, y1))
    
counter = 0
for a, b in Counter(all_coo).most_common():
    if b > 1:
        counter += 1

print(counter)