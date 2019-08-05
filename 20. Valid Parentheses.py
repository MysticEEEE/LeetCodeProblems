class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}
        for i in s:
            if not stack or i in parentheses:
                stack.append(i)
                print(stack)
            elif stack[-1] in parentheses and parentheses[stack[-1]]== i:
                stack.pop()
            else:
                return False
        return not stack

    def isValid1(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        # if s and s[0] not in dic: 
        #     return False
        stack = []
        for c in s:
            if not stack or c in dic: 
                stack.append(c)
            elif stack[-1] in dic and dic[stack[-1]] == c: 
                stack.pop()
            else: 
                return False  
        return not stack


        