a = [0, 0, 0]
for i in open('day.txt'):
    if 'fo' in i:
        val = int(i.split()[-1])
        a[0] += val
        a[1] += a[2] * val
    elif 'up' in i:
        val = int(i.split()[-1])
        a[2] -= val
    elif 'do' in i:
        val = int(i.split()[-1])
        a[2] += val
print(a[0] * a[1])