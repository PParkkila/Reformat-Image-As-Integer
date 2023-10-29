from PIL import Image
import hashlib

numToColorsDict = {}
digitsWeights = []

def ImageID(im):
    return hashlib.md5(im.tobytes()).hexdigest()

def ruleSortAscending(entry):
    return entry[1]


def setList():

    zeroIMG = Image.open("PNG_To_Numbers/numbers/zero.png")
    oneIMG = Image.open("PNG_To_Numbers/numbers/one.png")
    twoIMG = Image.open("PNG_To_Numbers/numbers/two.png")
    threeIMG = Image.open("PNG_To_Numbers/numbers/three.png")
    fourIMG = Image.open("PNG_To_Numbers/numbers/four.png")
    fiveIMG = Image.open("PNG_To_Numbers/numbers/five.png")
    sixIMG = Image.open("PNG_To_Numbers/numbers/six.png")
    sevenIMG = Image.open("PNG_To_Numbers/numbers/seven.png")
    eightIMG = Image.open("PNG_To_Numbers/numbers/eight.png")
    nineIMG = Image.open("PNG_To_Numbers/numbers/nine.png")

    images = [zeroIMG, oneIMG, twoIMG, threeIMG, fourIMG, fiveIMG, sixIMG, sevenIMG, eightIMG, nineIMG]

    numToColorsDict[ImageID(zeroIMG)] = ['0', 0]    
    numToColorsDict[ImageID(oneIMG)] = ['1', 0]
    numToColorsDict[ImageID(twoIMG)] = ['2', 0]
    numToColorsDict[ImageID(threeIMG)] = ['3', 0]
    numToColorsDict[ImageID(fourIMG)] = ['4', 0]
    numToColorsDict[ImageID(fiveIMG)] = ['5', 0]
    numToColorsDict[ImageID(sixIMG)] = ['6', 0]
    numToColorsDict[ImageID(sevenIMG)] = ['7', 0]
    numToColorsDict[ImageID(eightIMG)] = ['8', 0]
    numToColorsDict[ImageID(nineIMG)] = ['9', 0]



    # numToColorsDict = {ImageID(zeroIMG): ["zero", 0], 
    #                 ImageID(oneIMG): ["one", 0], 
    #                 ImageID(twoIMG): ["two", 0], 
    #                 ImageID(threeIMG): ["three", 0], 
    #                 ImageID(fourIMG): ["four", 4], 
    #                 ImageID(fiveIMG): ["five", 0], 
    #                 ImageID(sixIMG): ["six", 0], 
    #                 ImageID(sevenIMG): ["seven", 0], 
    #                 ImageID(eightIMG): ["eight", 0], 
    #                 ImageID(nineIMG): ["nine", 0]}
    

    for img in images:

        pixels = list(img.getdata())
        width, height = img.size

        elementsColorSum = 0


        for element in pixels:
            r, g, b, a = element
            brightness = 0.2126*r + 0.7152*g + 0.0722*b


            elementsColorSum = elementsColorSum + brightness
            

            # brightnessList.append(int(brightness))

            #end of each element iteration

        average = elementsColorSum / (height * width)

        numToColorsDict[ImageID(img)][1] = (average / 25.5) - 1
        #end of each image iteration

    for img in images:
        img.close()
    
    for key in numToColorsDict:
        digitsWeights.append(numToColorsDict[key])

    print(digitsWeights)
    print("\n\n")

    digitsWeights.sort(key=ruleSortAscending)
        
    print(digitsWeights)
    print("\n\n")

    return digitsWeights
    
    # print(numToColorsDict)


def main():
    setList()
    

if __name__ == "__main__":
    main()



