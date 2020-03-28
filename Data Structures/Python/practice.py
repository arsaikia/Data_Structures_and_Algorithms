

def twoSum(arr, target):

    i = 0
    j = len(arr)-1
    arr.sort()
    while(i < j):
        if((arr[i] + arr[j]) == target):
            return (i, j)

        if((arr[i] + arr[j]) > target):
            j -= 1
        elif((arr[i] + arr[j]) < target):
            i += 1

    return "Not Found"


if __name__ == "__main__":
    arr = [1, 2, 6, 4, 8, 10]
    target = [10, 12, 14]
    for each in target:
        print(twoSum(arr, each))
