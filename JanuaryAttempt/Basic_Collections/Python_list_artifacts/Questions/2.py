def is_valid_brackets(string):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
    return not stack

string = '{()]}'
print(is_valid_brackets(string)) # True