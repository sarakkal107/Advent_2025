count = 0
curloc = 50
prevloc = 50

fileName = "d1_input.txt"
#fileName = "d1_small.txt"

with open(fileName, "r") as file:
    for line in file:
        dir = line[0]
        number = int(line[1:])
        count += number // 100
        if dir == "L":
            prevloc = curloc
            curloc = curloc - number%100
            if curloc < 0:
                curloc += 100
                if prevloc != 0:
                    count +=1
            elif prevloc != 0 and curloc == 0:
                count +=1
        else:
            prevloc = curloc
            curloc = curloc + number%100
            if curloc >= 100:
                curloc -= 100
                count += 1
            elif prevloc != 0 and curloc == 0:
                count +=1
        #print("Current Location: " + str(curloc) +" Previous Location: " + str(prevloc) + " Count: " + str(count))
print(count)