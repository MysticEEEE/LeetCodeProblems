class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = ['']
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        for i in digits:
            next_res = []
            lst = dic[i]
            # print('lst:',lst)
            for j in lst:
                # print('j:',j)
                for k in res:
                    # print('k:',k)
                    next_res.append(k + j)
                    # print(next_res)
            res = next_res
        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dct = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 1:
            return dct[digits]
        pre = self.letterCombinations2(digits[:-1])
        post = list(dct[digits[-1]])
        return [s + c for s in pre for c in post]

    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        def traceback(temp, next_digits):
            if len(next_digits) == 0:
                res.append(temp)
            else:
                for character in phone[next_digits[0]]:
                    traceback(temp + character, next_digits[1:])

        if digits:
            traceback("", digits)
        return res


if __name__ == "__main__":
    pass
l = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
     ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'],
     ['w', 'x', 'y', 'z']]
digits = '234'
s = Solution()

print(s.letterCombinations(digits))
