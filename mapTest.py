def getPos(x):
    temp = x / 180
    temp -= 0.5
    temp = temp * 2000
    return temp

print(getPos(0))
print(getPos(90))
print(getPos(180))
