result = 0
def chech_adjacent_x(line, char_index, char):
    compare = []
    if char_index > 0:
        compare.append(int(line[char_index-1]))
    if char_index < len(line) -1:
        compare.append(int(line[char_index+1]))
    return int(char) < min(compare)

def chech_adjacent_y(rows, row_index, char_index, char):
    compare = []
    if row_index > 0:
        compare.append(int(rows[row_index-1][char_index]))
    if row_index < len(rows) -1:
        compare.append(int(rows[row_index+1][char_index]))
    return int(char) < min(compare)

with open("day.txt") as f:
    values = 0
    rows = [x.strip() for x in f.readlines()]
    for row_index, row in enumerate(rows):
        for char_index, char in enumerate(row):
            if chech_adjacent_x(row, char_index, char) and chech_adjacent_y(rows, row_index, char_index, char):
                result += int(char) + 1
print(result)