swapNum = input()
swapSplit = swapNum.split(" ")
print(str(swapSplit[-1]) + str(swapSplit[1:-1]) + str(swapSplit[0]))

#swapSplit[-1],swapSplit[0] = swapSplit[0],swapSplit[-1]