class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#准备是用先排序，按次序固定住，然后再用指针去做二分查找，最后返回
        answer=[]
        nums.sort() #[-4,-1,-1,0,1,2]
        gap=0
        for i,v in enumerate(nums):
            gap=0-v #2
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r=i+1,len(nums)-1 #1,2
            while l<r:
                if nums[l]+nums[r]==gap: #-1+2=1
                    ans=[v,nums[l],nums[r]]
                    answer.append(ans)
                    l+=1
                    r-=1
                    #接下来两句很关键，就是要保证能一直跳过重复项
                    while l<r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l]+nums[r]<gap:   
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