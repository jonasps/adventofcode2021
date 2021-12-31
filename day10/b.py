matches = {'<':'>','(':')','[':']','{':'}'}
points = {'>':4,')':1,']':2,'}':3}
score_list = []
def swapp(char):
    return matches[char]

for line in [x.strip() for x in open("day.txt").readlines()]:
    stack = []
    incomplete = True
    for index, char in enumerate(line, 0):
        if char not in matches.keys():
            left = stack.pop()
            if char != matches[left]:
                incomplete = False
                break
        else:
            stack.append(char)
    if incomplete:
        counter = 0
        stack.reverse()
        for c in list(map(swapp, stack)):
            counter = counter * 5 + points[c]
        score_list.append(counter)
score_list.sort()
print(score_list[len(score_list)//2])
