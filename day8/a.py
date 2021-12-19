counter = 0
with open("day.txt") as f:
    lines = f.readlines()
    for i in lines:
        i.replace("\n","")
        i = i.split(" | ")[1]
        for x in i.split(" "):
            if len(x) in [2, 3, 4, 7]:
                counter += 1
print(counter)