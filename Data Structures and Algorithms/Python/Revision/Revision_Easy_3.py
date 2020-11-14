# --------------------------------------<  Two Sum  >---------------------------------

# O(n) Time | O(n) Space
def twoSum(array, target):

    visited = {}

    for idx, num in enumerate(array):
        required = target - num
        if required in visited:
            return True
        else:
            visited[num] = idx
    return False


# O(n) Time | O(1) Space
def validateSubsequence(array, sequence):
    arrayIdx = sequenceIdx = 0

    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)


def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))


def findClosestValueHelper(node, target, closest):
    if node is None:
        print(node, closest)
        return closest
    if abs(node.value - target) < abs(target - closest):
        closest = node.value
    if target > node.value:
        return findClosestValueHelper(node.right, target, closest)
    elif target < node.value:
        return findClosestValueHelper(node.left, target, closest)
    else:
        return closest


if __name__ == "__main__":
    from binarytree import bst as tree
    bstTree = tree(is_perfect=True)
    print(bstTree)
    print(findClosestValueInBst(bstTree, 17))
