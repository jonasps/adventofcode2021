from collections import Counter

input_a = input_b = open('day.txt').readlines()

def calc(input_list, default):
    l_th = len(input_list[0])-1
    for y in range(0, l_th):
        l = [[] for _ in range(0, l_th)]
        for i in input_list:
            for x in range(0,l_th):
                l[x].append(i[x])
        try:
            look_value = default
            if default == '1':
                look_value = Counter(l[y]).most_common()[0][0]
                if Counter(l[y]).most_common()[0][1] == Counter(l[y]).most_common()[1][1]:
                    look_value = default
                next_a = [v for v in input_list if v[y] == look_value]
                if next_a:
                    input_list = next_a
            else:
                look_value = Counter(l[y]).most_common()[1][0]
                if Counter(l[y]).most_common()[0][1] == Counter(l[y]).most_common()[1][1]:
                    look_value = default
                next_a = [v for v in input_list if v[y] == look_value]
                if next_a:
                    input_list = next_a
        except:
            pass
    return int(input_list[0], 2)

print(calc(input_a, '1') * calc(input_b, '0'))