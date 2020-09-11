'''
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''


def oneAway(s1, s2) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return replaceChar(s1, s2)
    if len(s1) + 1 == len(s2):
        return insertChar(s1, s2)
    if len(s2) + 1 == len(s1):
        return insertChar(s2, s1)


def replaceChar(s1, s2):
    isReplaced = False

    idx = 0
    while idx < len(s1):
        if s1[idx] != s2[idx]:
            if isReplaced:
                return False
        isReplaced = True
    return True


def insertChar(stringOne, stringTwo):
    idxOne, idxTwo = 0, 0
    while idxOne < len(stringOne) and idxTwo < len(stringTwo):
        if stringOne[idxOne] != stringTwo[idxTwo]:
            if idxOne != idxTwo:
                return False
            idxOne += 1
        else:
            idxOne += 1
            idxTwo += 1
    return True


if __name__ == "__main__":
    s1, s2 = "pale", "bae"

    print(oneAway(s1, s2))
