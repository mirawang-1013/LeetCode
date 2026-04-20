class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#check if the starting point int the number set first, and then use while to loop through to see how long the consecutive string could be.
        num_set = set(nums)
        longest=0
        for i in nums:
            if i-1 not in num_set:
                count=1
                current=i
                while current+1 in num_set:
                    count+=1
                    current+=1
                longest=max(longest,count)
        return longest







        # num_set = set(nums)
        # longest=0
        # for num in num_set:
        #     if num-1 not in num_set:
        #         current=num
        #         count=1
        #         while current+1 in num_set:
        #             current+=1
        #             count+=1
        #         longest = max(longest,count)
            
        # return longest