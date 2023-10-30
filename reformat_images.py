import math
from PIL import Image
import analyze_numbers
from util import findMinBrightness, findMaxBrightness, switch
from FilesIO.file_writer import write_file



im = Image.open("numbers/six.png")


numToColorsList = analyze_numbers.setList()
tempBrightnessList = []

actualNumsList = []



pixels = list(im.getdata())
width, height = im.size
im.close()






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

    actualNumsList.append(switch(tempBrightnessList[i], numToColorsList))



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




