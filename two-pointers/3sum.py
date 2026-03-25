class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        for i,value in enumerate(nums):
            left=i+1
            right=len(nums)-1
            while left<right:
                total = value+nums[left]+nums[right]
                if total==0:
                    result.add((value,nums[left],nums[right]))
                    left+=1
                    right-=1
                if total>0:
                    right-=1
                if total<0:
                    left+=1
        return list(result)