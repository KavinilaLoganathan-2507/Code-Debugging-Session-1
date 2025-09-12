# Problem6: Given a string containing '(', ')', '{', '}', '[' and ']', determine if the input is valid (all brackets are closed properly).

def is_balanced(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack.pop() != mapping[char]:
                return False
    return True

print(is_balanced("()[]{}"))
print(is_balanced("(]"))
