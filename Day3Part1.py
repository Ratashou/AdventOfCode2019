file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2019\Day3.txt", "r")

dirList = file.read()
dirList = dirList.split()

directions1 = dirList[0].split(',')
directions2 = dirList[1].split(',')

snakex1 = []
snakex2 = []
snakey1 = []
snakey2 = []

def snakeIteration(directions,snakex,snakey):
    currentx = 0
    currenty = 0
    for line in directions:
        #Add every integer position the wire goes through
        if line[0] == "U":
            for i in range(1,int(line[1:])+1):
                snakey.append(currenty + i)
                snakex.append(currentx)
            currenty = int(line[1:])

        elif line[0] == "D":
            for i in range(1,int(line[1:])+1):
                snakey.append(currenty - i)
                snakex.append(currentx)
            currenty = int(line[1:])

        elif line[0] == "R":
            for i in range(1,int(line[1:])+1):
                snakex.append(currentx + i)
                snakey.append(currenty)
            currentx = int(line[1:])

        elif line[0] == "L":
            for i in range(1,int(line[1:])+1):
                snakex.append(currentx - i)
                snakey.append(currenty)
            currentx = int(line[1:])

        else:
            print("mistakes have been made")
            exit
#Run function for both wires
snakeIteration(directions1,snakex1,snakey1)

snakeIteration(directions2,snakex2,snakey2)

manhattenDistance = 9999999999
for i in range(0,len(snakex1)):
    for j in range(0,len(snakex2)):
        if snakex1[i] == snakex2[j] and snakey1[i] == snakey2[j] and (abs(snakex1[i]) + abs(snakey1[i])) < manhattenDistance:
            print("here")
            manhattenDistance = (abs(snakex1[i]) + abs(snakey1[i]))

print(manhattenDistance)

file.close()
