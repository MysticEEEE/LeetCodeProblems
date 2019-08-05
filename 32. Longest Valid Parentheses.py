class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用栈的方法，将"("加入栈中，当搜索到")"将栈顶出栈，并用当前Index剪去出栈后的栈顶，得到最大有效长度
        stack = [-1]
        maxLength = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
            #print( i , stack,maxLength)
            maxLength = max(maxLength, i - stack[-1] )

        return maxLength


    # 无额外空间方法：左右各遍历一次，分别给"("和")"计数，从左遍历时，当计数相等时，最大有效长度等于右括号的数字，
    # 反之等于左括号数字，最后比较两个的大小。
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        left1 = 0
        right1 = 0
        maxLength = 0
        maxLength2 = 0
        for i in s:
            if i == "(":
                left += 1
                print(left)
            else:
                right +=1
                print(right)
            if right == left:
                tmp =  right *2
                if tmp > maxLength:
                    maxLength = tmp
                print("maxlength", maxLength)
            elif right >= left:
                left = 0
                right = 0
        print(left,right,maxLength)

        for j in reversed(s):
            if j == ")":
                right1 += 1
            else:
                left1 += 1
            if left1 == right1:
                maxLength2 =  left1 *2
                if tmp > maxLength2:
                    maxLength = tmp
            elif left1 >= right1:
                left1 = 0
                right1 = 0
        print(left1,right1,maxLength2)
        return max(maxLength,maxLength2)
        

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest

if __name__ == "__main__":
    a = Solution()
    m = "(()))())("
    n = a.longestValidParentheses(m)
    l = a.longestValidParentheses1(m)
    p = a.longestValidParentheses2(m)

    print(n,l,p) 