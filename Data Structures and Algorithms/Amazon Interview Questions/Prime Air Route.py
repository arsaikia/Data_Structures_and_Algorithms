#----------- https://leetcode.com/discuss/interview-question/373202

'''
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id 
and the second integer represents a value. Your task is to find an element from a and an element form b 
such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
'''
# O(m log m) + O(n log n) Time | O( max(m, n))
def optimalUtilization( a, b, target ):
    sortedA = sorted(a, key = lambda a : a[1])
    sortedB= sorted(b, key = lambda b : b[1])
    firstIdx = 0
    secondIdx = len(sortedB) - 1
    results = []
    difference = float("inf")
    potential = []

    while firstIdx < len(sortedA) and secondIdx >= 0:
        

        difference = sortedA[firstIdx][1] + sortedB[secondIdx][1] - target


        if difference == 0:
            results.append([sortedA[firstIdx][0], sortedB[secondIdx][0]])
            firstIdx += 1
            secondIdx -= 1
        else:
            potential = [sortedA[firstIdx][0], sortedB[secondIdx][0]]
            if difference < 0:
                firstIdx += 1
            else:
                secondIdx -= 1
            

    if len(results) == 0:
        return [potential]
    return results



if __name__ == "__main__":
    a = [[1, 8], [2, 15], [3, 9]]
    b = [[1, 8], [2, 11], [3, 12]]
    target = 20
    print(optimalUtilization(a,b,target))