def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(')')
        elif not stack or stack[-1] != ch:
                return False
        else:
            stack.pop()
    return not stack
print(is_valid("()"))  # True  
print(is_valid("()()"))  # True  
print(is_valid("(())"))  # True  
print(is_valid(")(") ) # False  
print(is_valid("(()"))  # False  
