from collections import Counter

input = open('day.txt').readlines()
l_th = len(input[0])-1
l = [[] for _ in range(0, l_th)]
for i in input:
    for x in range(0,l_th):
        l[x].append(i[x])

gamma = epsilon = ''
for y in range(0, l_th):
    gamma += Counter(l[y]).most_common()[0][0]
    epsilon += Counter(l[y]).most_common()[1][0]

print(int(gamma, 2) * int(epsilon, 2))