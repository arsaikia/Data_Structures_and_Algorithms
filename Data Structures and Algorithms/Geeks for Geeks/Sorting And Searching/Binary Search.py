def mySqrt(x: int) -> int:
    left, right = 0, x - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1



if __name__ == "__main__":
    print(mySqrt(6))