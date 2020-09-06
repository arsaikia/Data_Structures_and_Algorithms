# O(n) Time || O(n) Space
# NOTE : FOR ALPHABET SIZE > 26 {large alphabet size} the size of alphabet will come into the picture for complexity analysis
def ceaserCypher( string, key ):
    newString = []
    newKey = key % 26
    for ch in string:
        newString.append(getNewLetters(ch, newKey))
    return ''.join(newString)

def getNewLetters( letter, key ):
    letterCode = ord(letter) + key
    return chr(letterCode) if letterCode <= 122 else chr(96 + letterCode % 122)


myString = 'xyz'
myKey = 2

print(f'Using ceaser cypher to encode {myString} by key {myKey} gives us : ', ceaserCypher(myString, myKey))