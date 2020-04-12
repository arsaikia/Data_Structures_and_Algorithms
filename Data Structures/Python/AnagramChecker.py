'''
🥨
Given two strings check if they are ANAGRAMS of each other or not.
'''


def anagramChecker(str1, str2):

    myDict = {}

    if(len(str1) != len(str2)):
        return False

    for each in str1:
        if myDict.get(each):
            myDict[each] += 1
        else:
            myDict[each] = 1

    for each in str2:
        if myDict.get(each) != 1:
            myDict[each] -= 1
        elif myDict.get(each):
            del(myDict[each])
        else:
            return False

    if(len(myDict.keys()) == 0):
        return True

    return False


if __name__ == "__main__":

    print(anagramChecker('aaabc', 'baaac'))
