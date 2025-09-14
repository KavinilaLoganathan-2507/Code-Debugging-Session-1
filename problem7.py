# Problem7: Given an array containing n distinct numbers from 0 to n, find the missing number.

def find_missing(nums):
    num = len(nums)
    expected_sum = num * (num + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing([3, 0, 1]))
