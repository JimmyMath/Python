def arrayMaxConsecutiveSum2(inputArray):
    currmax,m=inputArray[0],inputArray[0]
    for i in range(1,len(inputArray)):
        currmax=max(inputArray[i],currmax+inputArray[i])
        m=max(currmax,m)
    return m