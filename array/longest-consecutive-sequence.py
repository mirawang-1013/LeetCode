class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # Only check sequence starts
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_set = set(nums)
#         longest = 0
#         for num in nums:
#             if num-1 not in num_set: #try to find out the starting point
#                 length = 0

#                 while (num+length) in num_set:
#                     length += 1
#                 longest = max(longest, length)

#         return longest
        