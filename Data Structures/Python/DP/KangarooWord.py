def isSynonym(parent, child):
    if len(parent) < len(child):
        return False
    childSize = len(child)
    childIdx, parentIdx = 0, 0

    while childIdx < len(child) and parentIdx < len(parent):
        if child[childIdx] == parent[parentIdx]:
            if childIdx == 0 and child[childIdx: childIdx + childSize] == parent[parentIdx: parentIdx + childSize]:
                childIdx = childSize - 1
                parentIdx = parentIdx + childSize
                continue
            childIdx += 1
            parentIdx += 1
        else:
            parentIdx += 1

    if childIdx == len(child):
        return True

    return False


def calculateSynonymsCount(words, wordsToSynonyms, wordsToAntonyms):
    wordsToCheck = []
    foundWords = {}
    counter = 0
    populateWordsToCheck(words, wordsToSynonyms, wordsToCheck)
    populateWordsToCheck(words, wordsToAntonyms, wordsToCheck)

    for each in wordsToCheck:
        parent = list(each.keys())[0]
        children = each[parent]
        for child in children:
            if child in foundWords:
                continue
            if isSynonym(parent, child):
                foundWords[child] = True
                counter += 1
    return counter


def populateWordsToCheck(words, check, result):

    for each in check:
        array = each.split(":")

        if array[0] not in words:
            continue
        myDict = {array[0]: []}

        values = array[1].split(",")
        myDict[array[0]] = values
        result.append(myDict)


words = ['illuminated', "animosity", "deoxyribonucleic",
         "container", "lit", "amity", "encourage", "lighted"]
wordsToSynonyms = ["encourage:urge,boost,inspire",
                   "container:tin,can,bag,bottle", "lighted:lit", "illuminated:lit"]
wordsToAntonyms = ["encourage:discourage",
                   "animosity:amity,like", "lighted:dark"]


print(calculateSynonymsCount(words, wordsToSynonyms, wordsToAntonyms))


##############################################################################


def getArrivalTime(time, waitTime):
    if time > 100:
        hours = int(time / 100)
        minutes = int(time % 100)
    else:
        hours = 0
        minutes = time
    timeAfterWait = minutes + waitTime

    if timeAfterWait >= 60:
        additionalHours = int(timeAfterWait / 60)
        additionalMinutes = timeAfterWait % 60
        return ((((hours + additionalHours) % 24) * 100) + additionalMinutes)
    else:
        return ((hours % 24) * 100) + timeAfterWait


def minMeetingRooms(intervals):
    startTimes = sorted([meeting[0] for meeting in intervals])
    endTimes = sorted([getArrivalTime(meeting[1]) for meeting in intervals])
    start, end = 0, 0
    occupiedRooms = 0

    while start < len(startTimes) and end < len(endTimes):
        meetingStarts = startTimes[start]
        meetingEnds = endTimes[end]
        if meetingStarts < meetingEnds:
            occupiedRooms += 1
            start += 1
        else:
            start += 1
            end += 1

    return occupiedRooms


print(getArrivalTime(1259, 60))
