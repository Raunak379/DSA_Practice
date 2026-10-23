#brute solution :-------- solve throug Set, Dict
class Sloution:
    def substring(self, s:str):
        maxi = 0
        for i in range(0,len(s)):
            my_set = set()
            for j in range(i,len(s)):
                if s[j] in my_set:
                    break
                maxi = max(maxi, j-i+1)
                my_set.add(s[j])
        return maxi

s = "abcdaba"
obj = Sloution()
print(obj.substring(s))

# time = o(n*2)
# space  = o(n)

#optimal Solution :-------- solve through sliding windows and two pointers
class Sloution:
    def substring(self, s:str):
        my_dict = {}
        left = 0 
        right = 0 
        maxi = 0
        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]]+1) ##max(0,1+1)= (0,2)---> left = 2
            maxi = max(maxi, right-left+1)
            my_dict[s[right]] = right
            right += 1  
        return maxi

s = "abcdaba"
obj = Sloution()
print(obj.substring(s))

# time = o(n)
#space = o(n)
