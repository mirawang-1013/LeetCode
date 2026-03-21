class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums.sort()
        print(nums)
        left,right=0,len(nums)-1
        for i,value in enumerate(nums):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                if total>0:
                    right-=1
                if total==0:
                    result.add(tuple([value,nums[left],nums[right]]))
                    left+=1
                    right-=1
        return [list(t) for t in result]


        
        