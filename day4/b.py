from copy import deepcopy
class Board:
    def __init__(self, values):
        self.playing = True
        self.static_values = deepcopy(values)
        self.values = deepcopy(values)
    
    def updateBoard(self, val):
        for y in range(0, 5):
            for x in range(0, 5):
                if self.values[y][x] == val:
                    self.values[y][x] = "x"
    
    def calc_value(self, last_num):
        self.playing = False
        _sum = 0
        for i in self.values:
            _sum += sum([int(x) for x in i if x != 'x'])
        return _sum * int(last_num)

    def checkBingo(self, val):
        check = ['x','x','x','x','x']
        for x in range(0, 5):
            if [self.values[0][x], self.values[1][x], self.values[2][x], self.values[3][x], self.values[4][x]] == check:
                return self.calc_value(val)
        
        for x in range(0, 5):
            if self.values[x] == check:
                return self.calc_value(val)
        return False

fp = open("day.txt")
numbers = []
counter = 0
values =[]
boards = []
for i, line in enumerate(fp):
    if i == 0:
        numbers = line.strip('\n').split(',')
    else:
        counter += 1
        _line = line.strip('\n').split(',')[0]
        if _line:
            a = []
            for l in _line.split(' '):
                if l:
                    a.append(l)
            values.append(a)
        if counter == 6:
            counter = 0
            boards.append(Board(values))
            values = []
fp.close()

found = False
for i in numbers:
    counter += 1
    for board in boards:
        board.updateBoard(i)
        got_bingo = board.checkBingo(i)
        if len([b for b in boards if b.playing == True]) == 0:
            print(got_bingo)
            found = True
            break
    if found:
        break
            
