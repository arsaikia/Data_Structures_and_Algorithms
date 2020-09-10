'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

# O(n) Time || O(n) Space
# To do this is one pass we can traverse through the string backwards and mutate the string
def URLify(string, length):
    charList = list(string[:length])     # O(n) Time | O(n) Space
    for idx, char in enumerate(charList):
        if char == " ":
            if idx == 0:
                charList[idx] = "%20"
            else:
                if charList[idx - 1] == "%20" or charList[idx - 1] == " ":
                    continue
                charList[idx] = "%20"
    return "".join(charList)
            
            
            
if __name__ == "__main__":
    inputString = "Mr John Smith "
    outputString = "Mr%20John%20Smith"
    
    print(URLify(inputString, 13) == "Mr%20John%20Smith")