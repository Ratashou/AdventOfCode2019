file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2019\Day2.txt", "r")

#Create a list from the file
intList = file.read()
intList = intList.split(',')
intList.pop()[-1]

counter = 0
for line in intList:
    intList[counter] = int(line)
    counter += 1

#The correct position 1 and 2
noun = 0
verb = 0
#Initialising the boolean that tells you if you have the right answer
breaking = False
#Cycling through every valid combination of noun and verb
for i in range(0, 100):
    for j in range(0, 100):
        counter = 0
        tempList = intList[:]
        tempList[1] = i
        tempList[2] = j
        while tempList[counter] != 99:
            if tempList[counter] == 1:
                placeholder = tempList[tempList[counter+1]] + tempList[tempList[counter+2]]
                tempList[tempList[counter+3]] = placeholder
            elif tempList[counter] == 2:
                placeholder = tempList[tempList[counter+1]] * tempList[tempList[counter+2]]
                tempList[tempList[counter+3]] = placeholder
            elif tempList[counter] == 99:
                break
            else:
                break
            counter += 4
        if tempList[0] == 19690720:
            breaking = True
            noun = i
            verb = j
            break
    if breaking == True:
        break

if breaking ==True:
    answer = (100*noun)+verb
    print(answer)
else:
    print("no answer found")

file.close()
