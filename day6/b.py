with open("day.txt") as f:
    fish = [x for x in f.readlines()[0].split(',')]
    fish_ages = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    for _ in fish:
        fish_ages[_] = fish_ages[_] + 1
    for i in range(0, 256):
        eight = fish_ages['8']
        seven = fish_ages['7']
        six = fish_ages['6']
        five = fish_ages['5']
        four = fish_ages['4']
        three = fish_ages['3']
        two = fish_ages['2']
        one = fish_ages['1']
        zero = fish_ages['0']

        fish_ages['8'] = zero
        fish_ages['7'] = eight
        fish_ages['6'] = seven + zero
        fish_ages['5'] = six
        fish_ages['4'] = five
        fish_ages['3'] = four
        fish_ages['2'] = three
        fish_ages['1'] = two
        fish_ages['0'] = one

print(sum(fish_ages.values()))