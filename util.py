
def findMinBrightness(blist):
    min = blist[0]

    for entry in blist:
        if (entry < min):
            min = entry

    return min




def findMaxBrightness(blist):
    
    max = blist[0]

    for entry in blist:
        if (entry > max):
            max = entry

    return max

def actionOnZero(numColorList):
    return numColorList[0][0]

def actionOnOne(numColorList):
    return numColorList[1][0]

def actionOnTwo(numColorList):
    return numColorList[2][0]

def actionOnThree(numColorList):
    return numColorList[3][0]

def actionOnFour(numColorList):
    return numColorList[4][0]

def actionOnFive(numColorList):
    return numColorList[5][0]

def actionOnSix(numColorList):
    return numColorList[6][0]

def actionOnSeven(numColorList):
    return numColorList[7][0]

def actionOnEight(numColorList):
    return numColorList[8][0]

def actionOnNine(numColorList):
    return numColorList[9][0]

def switch(digit, numColorList):

    match digit:

        case 0:
            return actionOnZero(numColorList)

        case 1:
            return actionOnOne(numColorList)

        case 2:
            return actionOnTwo(numColorList)

        case 3:
            return actionOnThree(numColorList)

        case 4:
            return actionOnFour(numColorList)

        case 5:
            return actionOnFive(numColorList)

        case 6:
            return actionOnSix(numColorList)
        
        case 7:
            return actionOnSeven(numColorList)
        
        case 8:
            return actionOnEight(numColorList)
        
        case 9:
            return actionOnNine(numColorList)
        
        case _:
            pass
