import math

file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2019\Day1.txt", "r")

totalFuel = 0
for mass in file:
    mass = int(mass)
    fuel = mass / 3
    fuel = math.floor(fuel)
    fuel = fuel - 2
    totalFuel += fuel

file.close()

print(totalFuel)

