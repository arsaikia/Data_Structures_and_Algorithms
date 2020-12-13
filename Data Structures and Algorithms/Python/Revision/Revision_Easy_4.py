'''
Two Sum
'''
# O(n) Time | O(n) Space


def twoSum(array, target):
    visited = {}
    result = []
    for idx, num in enumerate(array):
        required = target - num
        if required in visited:
            result.append({num: idx, required: visited[required]})
        else:
            visited[num] = idx
    return result


'''
Validate Subsequence
'''

# O(n) Time | O(1) Space


def validateSubsequence(arr, seq):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(arr) and seqIdx < len(seq):
        arrVal = arr[arrIdx]
        seqVal = seq[seqIdx]

        if arrVal == seqVal:
            arrIdx += 1
            seqIdx += 1
        else:
            arrIdx += 1
    return seqIdx == len(seq)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree : BST, target: int) -> int:
    return closestInBst(tree, float('inf'), target)

def closestInBst(node, closest, target):
    
    if node is None:
        return closest

    if abs(node.value - target) < abs(target - closest):
        closest = node.value
    
    if closest < node.value:
        closestInBst(node.left)
    elif closest > node.value:
        closestInBst(node.right)
    else:
        return closest





if __name__ == "__main__":
    # arr = [3, 5, -4, 8, 11, 1, -1, 6, 9]
    # print(twoSum(arr, 10))

    # arr = [5, 1, 22, 25, 6, -1, 8, 10]
    # seq = [1, 6, -1, 10]
    # print(validateSubsequence(arr, seq))
