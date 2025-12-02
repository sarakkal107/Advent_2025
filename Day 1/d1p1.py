count = 0
loc = 50

fileName = "d1_input.txt"
#fileName = "small.txt"

with open(fileName, "r") as file:
    for line in file:
        dir = line[0]
        number = int(line[1:])
        if dir == "L":
            loc = loc - number%100
            if loc < 0:
                loc += 100
            elif loc == 0:
                count +=1
        else:
            loc = loc + number%100
            if loc >= 100:
                loc -= 100
            if loc == 0:
                count +=1
        #print("Location: " + str(loc) + " Count: " + str(count))
print(count)