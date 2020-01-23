import math

file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2019\Day1.txt", "r")

totalFuel = 0
#Take mass and covert to fuel needed
for mass in file:
    mass = int(mass)
    fuel = mass / 3
    fuel = math.floor(fuel)
    fuel = fuel - 2
    totalFuel += fuel
    #Keep calculating fuel needed for extra fuel until no more needed
    while True:
        fuel = mass / 3
        fuel = math.floor(fuel)
        fuel = fuel - 2
        if fuel > 0:
            totalFuel += fuel
        else:
            break

file.close()

print(totalFuel)

