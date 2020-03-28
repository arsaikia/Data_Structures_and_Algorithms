def sockMerchant(n, arr):

    pairs = 0
    myDict = {}
    for each in arr:
        if myDict.get(str(each)):
            if myDict.get(str(each)) == 1:
                pairs += 1
                myDict[str(each)] = 0

            elif myDict.get(str(each)) == 0:
                myDict[str(each)]= 1
        else:
            myDict[str(each)] = 1
    return pairs


if __name__ == "__main__":
    print(sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
