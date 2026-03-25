class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i,value in enumerate(nums):
            left=i+1
            right=len(nums)-1
            while left<right:
                total = value+nums[left]+nums[right]
                if total==0:
                    if (value,nums[left],nums[right]) not in result:
                        result.append((value,nums[left],nums[right]))
                    left+=1
                    right-=1
                if total>0:
                    right-=1
                if total<0:
                    left+=1
        return result