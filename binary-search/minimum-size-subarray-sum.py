class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort()
        answer=float("infinity")
        l=0
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            
            while sum>=target:
                sum-=nums[l]
                answer=min(answer,r-l+1)
                l+=1
        return answer if answer!=float("infinity") else 0
