a = [0, 0]
for i in open('day.txt'):
    if 'fo' in i:
        a[0] += int(i.split()[-1])
    if 'up' in i:
        a[1] -= int(i.split()[-1])
    if 'do' in i:
        a[1] += int(i.split()[-1])
print(a[0] * a[1])