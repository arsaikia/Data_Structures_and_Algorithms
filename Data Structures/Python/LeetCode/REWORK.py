'''
Contiguous Array : Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
'''
# from typing import List

# class Solution:
#     def findMaxLength(self, nums : List[int]) -> int :
#         totalSum = 0
#         globalMax = 0
#         myDict = {0 : -1}

#         for i in range(len(nums)):
#             totalSum = (totalSum-1) if nums[i]==0 else (totalSum+1)
#             nums[i] = totalSum
#             if(totalSum in myDict.keys()): globalMax = max(globalMax, (i-myDict[totalSum]))
#             else: myDict[totalSum] = i

#         return globalMax





# if __name__ == "__main__":
#     sol = Solution()
#     arr = [0,0,1]
#     print(f'Max Length of the binary array {arr} is : {sol.findMaxLength(arr)}')


from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        rightShift = 0
        leftShift = 0

        for each in shift:
            if( each[0] == 0 ): leftShift += each[1]
            else: rightShift += each[1]

        if leftShift>len(s):
            leftShift %= len(s)
        if rightShift>len(s):
            rightShift %= len(s)

        print(leftShift, rightShift)

        if(leftShift > rightShift): 
            leftShift = leftShift-rightShift
            return s[ leftShift: ] + s[:leftShift]
        elif((leftShift < rightShift)): 
            rightShift = rightShift-leftShift
            return  s[len(s)-rightShift:] + s[:-rightShift]
        return s
    
    def recurFind(self, minVal, maxVal, arr, target):
     
            val = (minVal+maxVal)//2
            print(val, minVal, maxVal, target)
            if arr[val] == target:
                return val
            elif(arr[val] < target):
                self.recurFind( val, maxVal, arr, target )
            else:
                self.recurFind( minVal, val, arr, target )

    def BinarySearch(self, arr, target):

        return self.recurFind( 0, len(arr)-1, arr, target )
        
        






if __name__ == "__main__":
    sol = Solution()
    # print(sol.stringShift("joiazl", [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]))
    print(sol.BinarySearch([0, 1,2,3,4,5], 4))