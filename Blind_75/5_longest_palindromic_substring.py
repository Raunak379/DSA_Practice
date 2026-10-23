# optimal solution
class Solution:
    def longestPalindrome(self, s: str):
        res = ""
        reslen = 0
        for i in range(len(s)):
            # Odd-length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            # Even-length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
        return res
    
s = "bccdbaab"
obj = Solution()
print(obj.longestPalindrome(s))

# time = o(n*2)
#space = o(n)
