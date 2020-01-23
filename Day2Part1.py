file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2019\Day2.txt", "r")

intList = file.read()
intList = intList.split(',')
intList.pop()[-1]

counter = 0
for line in intList:
    intList[counter] = int(line)
    counter += 1

intList[1] = 12
intList[2] = 2

counter = 0
while intList[counter] != 99:
    if intList[counter] == 1:
        placeholder = intList[intList[counter+1]] + intList[intList[counter+2]]
        intList[intList[counter+3]] = placeholder
    elif intList[counter] == 2:
        placeholder = intList[intList[counter+1]] * intList[intList[counter+2]]
        intList[intList[counter+3]] = placeholder
    elif intList[counter] == 99:
        break
    else:
        print("error")
        break
    counter += 4

print(intList[0])

file.close()
