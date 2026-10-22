#brute solution
class Solution:
    def twoSum(self, nums: list[int], target: int):
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
nums = [3,6,8,4,6,4,2,9]
target = 10
obj = Solution()
print(obj.twoSum(nums, target))

#time =  o(n*2)


#optimal Solution :- solve throug hash_map, dict
class Solution:
    def twoSum(self, nums: list[int], target: int):
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return[hash_map[remaining],i]
            hash_map[nums[i]] = i
            
nums = [3,6,8,4,6,4,2,9]
target = 10
obj = Solution()
print(obj.twoSum(nums, target))

#time c = o(n)
#space c = o(n)