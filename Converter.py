
def convertToMin(inputString):
    inputHHMM = float(inputString)
    outputMIN = 0
    tmpStr = ""
    if inputHHMM <= 99:
        outputMIN = inputHHMM
    elif inputHHMM <= 999:
        tmp = list(str(inputHHMM))
        newHR = int(tmp.pop(0)) * 60
        tmpStr = tmpStr.join(tmp)
        outputMIN = float(newHR + float(tmpStr))
    else:
        tmp = list(str(inputHHMM))
        newHR = int(tmp.pop(0)+tmp.pop(0)) * 60
        tmpStr = tmpStr.join(tmp)
        outputMIN = float(newHR + float(tmpStr))
    return outputMIN
