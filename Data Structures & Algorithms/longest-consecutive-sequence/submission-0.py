class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        longest=0
        for i in nums:
            if i-1 in nums:
                continue
            min=i
            length=1
            while min+1 in nums:
                min+=1
                length+=1
            longest=max(length,longest)
                
        return longest   