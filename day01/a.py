counter, pre = 0, False
with open('day.txt') as f:
    for row in f:
        row = int(row)
        if pre is False:
            pre = row
        if row > pre:
            counter += 1
        pre = row
print(counter)