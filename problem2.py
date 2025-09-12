# Problem2: Return the second largest unique number in the list.

def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

print(second_largest([4, 1, 7, 7, 3]))
