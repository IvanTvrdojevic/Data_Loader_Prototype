import os
import random
from PIL import Image
import numpy

def main():
    data = getData("Data/Animals/")
    dataSplitFromDir = getDataFromSplit("Data/SplitData/")
    dataSplit = getSplitData("Data/Animals/")

   
def getData(dataPath):
    data = []
    for className in os.scandir(dataPath):
        pathToImages = dataPath + className.name
        data += getDataFromDir(pathToImages, className.name)
    random.shuffle(data)
    
    return data
    
def getDataFromSplit(dataPath):
    data = []
    splits = ["train", "test", "validation"]
    for split in splits:
        dirData = []
        for className in os.scandir(dataPath + split):
            pathToImages = dataPath  + split + "/" + className.name
            dirData += (getDataFromDir(pathToImages, className.name))
            random.shuffle(dirData)
        data.append(dirData)
    
    return data

def getSplitData(dataPath):
    data = getData(dataPath)
    numOfImages = getNumOfImages(dataPath)
    numOfTrainImages = int(0.7 * numOfImages)
    numOfTestImages = int(0.2 * numOfImages)
    numOfValidationImages = numOfImages - (numOfTrainImages + numOfTestImages)
    usedIndexes = []
    trainData, usedIndexes = getPartOfData(data, numOfTrainImages, numOfImages, usedIndexes)
    testData, usedIndexes = getPartOfData(data, numOfTestImages, numOfImages, usedIndexes)
    validationData, usedIndexes = getPartOfData(data, numOfValidationImages, numOfImages, usedIndexes)

    return [trainData, testData, validationData]
    
def getDataFromDir(pathToImages, className):
    data = []
    for imageName in os.scandir(pathToImages):
        fullPath = pathToImages + "/" + imageName.name
        classImage = (numpy.array(Image.open(fullPath)))
        labeledImage = (className, classImage)
        data.append(labeledImage)
    return data
    
def getNumOfClasses(dataPath):
    cnt = 0
    for dataClass in os.scandir(dataPath):
        if dataClass.is_dir():
            cnt += 1

    return cnt

def getNumOfImages(dataPath):
    cnt = 0
    for dataClass in os.scandir(dataPath):
        if dataClass.is_dir():
            for _ in os.scandir(dataClass):
                cnt += 1

    return cnt

def getPartOfData(data, numOfImagesPart, numOfImages, usedIndexes):
    dataPart = []
    i = 0
    while(i < numOfImagesPart):
        randomIndex = random.randint(0, numOfImages - 1)
        if randomIndex not in usedIndexes:
            usedIndexes.append(randomIndex)
            dataPart.append(data[i])
            i += 1
    random.shuffle(dataPart)
    
    return dataPart, usedIndexes

if __name__ == "__main__":
    main()



