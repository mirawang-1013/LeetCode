class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]
        for i,v in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[l]+nums[r]+v
                if total==0:
                        answer.append([v,nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r-1]==nums[r]:
                            r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return answer
                    
            




















        # nums.sort()
        # result=[]
        # for i,value in enumerate(nums):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     left=i+1
        #     right=len(nums)-1
        #     while left<right:
        #         total = value+nums[left]+nums[right]
        #         if total==0:
        #             result.append((value,nums[left],nums[right]))
        #             left+=1
        #             right-=1
        #             while left<right and nums[left]==nums[left-1]:
        #                 left+=1
        #             while left<right and nums[right]==nums[right+1]:
        #                 right-=1
        #         elif total>0:
        #             right-=1
        #         elif total<0:
        #             left+=1
        # return list(result)