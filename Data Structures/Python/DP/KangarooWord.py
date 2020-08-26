def isSynonym(parent, child):
    if len(parent) < len(child):
        return False

    childIdx, parentIdx = 0, 0

    while childIdx < len(child) and parentIdx < len(parent):
        if child[childIdx] == parent[parentIdx]:
            childIdx += 1
            parentIdx += 1
        else:
            parentIdx += 1

    if childIdx == len(child):
        return True

    return False


wordsToCheck = ["illuminated", "animosity"]
wordsToSynonyms = ["illuminated:lit,ted,xyzz,id"]
checkSynonym = []
for each in wordsToSynonyms:
    words = each.split(':')
    if words[0] not in wordsToCheck:
        continue
    checkSynonym = words[1].split(',')

currMax, globalMax = 0, 0
for each in checkSynonym:
    if isSynonym(words[0], each):
        currMax += 1
    globalMax = max(currMax, globalMax)

print(globalMax)


# print(isSynonym('animosity', 'amity'))
