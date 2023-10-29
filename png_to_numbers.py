import math
from PIL import Image
import analyze_numbers


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

def actionOnZero():
    return numToColorsList[0][0]

def actionOnOne():
    return numToColorsList[1][0]

def actionOnTwo():
    return numToColorsList[2][0]

def actionOnThree():
    return numToColorsList[3][0]

def actionOnFour():
    return numToColorsList[4][0]

def actionOnFive():
    return numToColorsList[5][0]

def actionOnSix():
    return numToColorsList[6][0]

def actionOnSeven():
    return numToColorsList[7][0]

def actionOnEight():
    return numToColorsList[8][0]

def actionOnNine():
    return numToColorsList[9][0]

def switch(digit):

    match digit:

        case 0:
            return actionOnZero()

        case 1:
            return actionOnOne()

        case 2:
            return actionOnTwo()

        case 3:
            return actionOnThree()

        case 4:
            return actionOnFour()

        case 5:
            return actionOnFive()

        case 6:
            return actionOnSix()
        
        case 7:
            return actionOnSeven()
        
        case 8:
            return actionOnEight()
        
        case 9:
            return actionOnNine()
        
        case _:
            pass


im = Image.open("numbers/zero.png")


numToColorsList = analyze_numbers.setList()
tempBrightnessList = []

actualNumsList = []



pixels = list(im.getdata())
width, height = im.size







def scaleBrightness(min, max, list):
    #creates ten points evenly spaced out in the interval

    fromNine = 9 / max

    for i in range(len(list)):
        
        list[i] = list[i] - min

        list[i] = list[i] * fromNine

        list[i] = math.floor(list[i])

        #want max value to be nine
        #range is max-min

# minBrightness = 20 # value that is out of bounds for the function for brightness
# maxBrightness = -1
for pixel in pixels:
    r, g, b, a = pixel

    brightness = (r + g + b) / 3
    # brightness = 0.2126*r + 0.7152*g + 0.0722*b

    brightness = brightness / 25.5

    #could find brightest
    #find darkest
    #determine range and set point values evenly spaced within to determine bounds for
    #each digit

    # print(numToColorsList[brightness][0], end=" ")
    # if (brightness < minBrightness):
    #     minBrightness = brightness

    # if (brightness > maxBrightness):
    #     maxBrightness = brightness

    tempBrightnessList.append(brightness)
    # print(actualNumsList)

# print(tempBrightnessList)
scaleBrightness(findMinBrightness(tempBrightnessList),findMaxBrightness(tempBrightnessList), tempBrightnessList)
print(tempBrightnessList)

for i in range(len(tempBrightnessList)):

    actualNumsList.append(switch(tempBrightnessList[i]))



print(actualNumsList)

def outputValues(width, height):
    f = open(r"output.txt","w")



    row = 0
    for i in range(height):

        for j in range(width):
            f.write(actualNumsList[(width * row) + j])
            f.write(' ')

        f.write("\n")
        row = row + 1

    f.close()



    # for digit in actualNumsList:
        # print(switch(digit), end = "")

outputValues(width, height)
    









# analyze the pixels of the image

#determine what number each pixel should be and the height/width of the image

#place the specific digit in the file specified




