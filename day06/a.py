with open("day.txt") as f:
    fish = [int(x) for x in f.readlines()[0].split(',')]
    counter = -1
    day = 0
    _max = len(fish)
    while day != 80:
        counter += 1
        if counter == _max:
            _max = len(fish) 
            counter = -1
            day += 1
        elif fish[counter] == 0:
            fish[counter] = 6
            fish.append(8)
        else:
            fish[counter] = fish[counter]-1
    print(_max)