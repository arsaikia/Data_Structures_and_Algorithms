'''
Longest Mountain in Array : https://leetcode.com/problems/longest-mountain-in-array/

'''
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


def longestPeak(array):
    if len(array) < 3:
        return 0
    peaks = []
    currMax = globalMax = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peaks.append(i)

    for peak in peaks:
        left = peak
        while left-1 >= 0 and array[left] > array[left-1]:
            left = left-1

        right = peak
        while right+1 < len(array) and array[right] > array[right+1]:
            right = right+1

        currMax = right-left

        globalMax = max(currMax, globalMax)

    return globalMax+1


def efficientLongestPeak(array):
    longest = float("-inf")
    i = 1
    while i < len(array) - 1:
        if not isPeak(i, array):
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        i = right
        longest = max(longest, right - left - 1)
    return longest


def isPeak(idx, arr):
    return arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]


if __name__ == "__main__":
    print(longestPeak(array))
    print(efficientLongestPeak(array))
