class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        my_set = set()
        n = len(nums)
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                n = num
                count = 1
                while n + 1 in my_set:
                    count+=1
                    n+=1
                longest = max(longest,count)
        return longest
nums = [100, 4, 200, 1, 3, 2]

obj = Solution()
print(obj.longestConsecutive(nums))