# 🐲🐲🐲
'''
Kadane's Algorithm for finding maximum subarray sum.
APPROACH:
    Traverse the array and for each iteration keep the 
    local and global maximum sum.
    Return the global sum.
'''


def kadane_max_subArray(arr):

    max_local = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_local = max(arr[i], (arr[i]+max_local))
        max_global = max(max_global, max_local)

    return max_global


if __name__ == "__main__":
    print(kadane_max_subArray([-2, -3, 4, -1, -2, 1, 5, -3]))
