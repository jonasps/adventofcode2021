matches = {'<':'>','(':')','[':']','{':'}'}
points = {'>':25137,')':3,']':57,'}':1197}
result = 0
for line in [x.strip() for x in open("day.txt").readlines()]:
    stack = []
    for index, char in enumerate(line, 0):
        if char not in matches.keys():
            left = stack.pop()
            if char != matches[left]:
                result += points[char]
                break
        else:
            stack.append(char)
print(result)