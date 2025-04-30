class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in num_set: #try to find out the starting point
                current = num
                count = 1

                while current+1 in num_set:
                    current += 1
                    count += 1
                
                longest = max(longest, count)

        return longest