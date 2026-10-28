#Brute Force Solution
class Soultion:
    def removeElement(self, nums: list[int], val: int):
        n = len(nums)
        freq = {}
        for i in range(0,n):
            freq[nums[i]]=0
        j=0
        for k in freq:
            nums[j] = k
            j+=1
        return j

nums = [0,0,1,1,2,2,3,3,4,4,5]
val = 2
obj = Soultion()
print(obj.removeElement(nums,val))

# time = o(n)
# space = o(n)


#Optimal Solution
class Soultion:
    def removeElement(self, nums: list[int], val: int):
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        j = i+1
        while j<n:
            if nums[j] != nums[i]:
                i += 1
                nums[i],nums[j] == nums[j],nums[i]
            j += 1
        return i + 1

nums = [0,0,1,1,2,2,3,3,4,4,5]
val = 2
obj = Soultion()
print(obj.removeElement(nums,val))

# time = o(n)
# space = o(1)