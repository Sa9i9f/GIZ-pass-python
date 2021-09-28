

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        def check(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        newString = ""
        for c in range(len(s)):
            temp = check(c, c)
            if len(temp) > len(newString):
                newString = temp
            temp = check(c, c+1)
            if len(temp) > len(newString):
                newString = temp
        return print("Output:", newString)


s = input("Input: s = ")
Solution.longest_palindromic(s)
