class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float("infinity")
        sum=0
        l=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>target:
                l+=1
                sum-=nums[l]
                answer=min(answer,r-l+1)
        return 0 if answer ==float("infinity") else answer
