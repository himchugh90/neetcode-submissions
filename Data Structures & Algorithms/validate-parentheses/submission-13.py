class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'{' : '}', '[' : ']', '(' : ')'}
        stack = []
        # while stack:
        for i in range(len(s)):
            if stack and stack[-1] in dict1.keys() and dict1[stack[-1]]  == s[i] :
                stack.pop()
            else:
                stack.append(s[i])
                print(stack)
        if len(stack) == 0:
            return True
 
        return False
