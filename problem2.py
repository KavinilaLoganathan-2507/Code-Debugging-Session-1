# Problem2: Return the second largest unique number in the list.

def second_largest(num):
    num = list(set(num))
    num.sort()
    return num[-2]

print(second_largest([4, 1, 7, 7, 3]))
