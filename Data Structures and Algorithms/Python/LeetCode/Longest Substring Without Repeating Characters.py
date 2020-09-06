def longestSubstringWithouRepeatingCharacters( string ):
    if len(string) < 1: return 0
    
    start, end, maxlen = 0, 0, 0
    charSet = set()
    
    while start < len(string) and end<len(string):
        if string[end] in charSet:
            
            charSet.remove(string[start])
            start += 1   
        else:
            charSet.add( string[end] )
            end += 1
            maxlen = max( maxlen, end-start )    
    return maxlen



myString = "pwwkew"
print(longestSubstringWithouRepeatingCharacters( myString ))
    
    
    
