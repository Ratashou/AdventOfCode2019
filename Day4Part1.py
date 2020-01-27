low = 256310
high = 732736

passwords = 0
for i in range(low,high+1):
    passwordAscending = 0
    passwordDouble = False
    for j in range(0,len(str(i))-1):
        if str(i)[j] <= str(i)[j+1]:
            passwordAscending += 1
        if str(i)[j] == str(i)[j+1]:
            passwordDouble = True
    if passwordDouble == True and passwordAscending == 5:
        passwords += 1

print(passwords)
        
