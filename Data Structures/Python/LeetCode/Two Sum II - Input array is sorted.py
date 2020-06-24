from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    start, end = 0, len(numbers)-1
    while start<end:
        if numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return [start+1, end+1]
    return -1

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
