def isValid(s):
    myStack = []
    myDict = {
        '(': ')',
        '{': '}',
        '[': ']'}
    
    for each in s:
        if(each == '(' or each =='{' or each =='['): myStack.append(each)
        else:
            if not each == myDict.get(myStack.pop() if myStack else False , None): return False
    
    if len(myStack) > 0 : return False

    return True


print(isValid(")("))

