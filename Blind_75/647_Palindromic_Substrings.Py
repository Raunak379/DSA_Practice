#optimal solution
class Solution:
    def countSubstrings(self, s: str):
        """ans = 0
        for i in range(len(s)):
            r = l = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                ans +=1
                l -=1
                r +=1
            l=i
            r+=1
            while l>=0 and r<len(s) and s[l] == s[r]:
                ans +=1
                l -=1
                r +=1
            return ans"""
        ans = 0 
        for i in range(len(s)):
            #odd
            ans += self.pcount(s, i, i)
            #even
            ans += self.pcount(s, i, i+1)
        return ans

    def pcount(self,s,l,r):
        ans = 0 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans

s = "aabcd"
obj = Solution()
print(obj.countSubstrings(s))

#time = o(n*2)
#space = o(n)