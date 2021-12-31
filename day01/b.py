i, counter, a = (0, 0, [int(i) for i in open('day.txt')])
while True:
    try:
        slide, i = sum((a[i], a[i+1], a[i+2])), i+1
        counter += int(slide < sum((a[i], a[i+1], a[i+2])))
    except:
        print(counter)
        break
