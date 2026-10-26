#brute force solution
class Solution:
    def merge(self, nums1:list[int], nums2:list[int], m:int, n:int):
        num3 = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i]<=nums2[j]:
                num3.append(nums1[i])
                i += 1
            else:
                num3.append(nums2[j])
                j += 1
        while i < m:
            num3.append(nums1[i])
            i+=1
        while j < n :
            num3.append(nums2[j])
            j+=1
        return num3
                    

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
obj = Solution()
print(obj.merge(nums1, nums2, 3, 3))

#brute force  Solution
class Solution:
    def merge(self, nums1:list[int], nums2:list[int], m:int, n:int):
        index = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -=1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1
        return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
obj = Solution()
print(obj.merge(nums1, nums2, 3, 3))