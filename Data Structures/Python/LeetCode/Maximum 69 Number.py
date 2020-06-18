import math

def maximum69Number (num: int) -> int:
    numStr = (str(num))
    for idx, each in enumerate(numStr):
        if each == '6':
            print('here')
            return int(numStr[:idx]+'9'+numStr[idx+1:])
    return num


print(maximum69Number(9966))

        