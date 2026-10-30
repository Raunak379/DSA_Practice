#optimal solution
class Solution:
    def removeDuplicates(self, nums: list[int]):
        n = len(nums)
        j = 1
        for i in range(1,n):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j+=1
        return j
nums = [0,0,1,1,2,2,2,3,4,4,4,5,5]
obj = Solution()
k = obj.removeDuplicates(nums)
print(nums[:k])

#space = o(1)
#time = o(n)