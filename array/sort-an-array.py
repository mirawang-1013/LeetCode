from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            res=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            
            mid=len(nums)//2
            left=merge_sort(nums[:mid])
            right=merge_sort(nums[mid:]) #先切

            return merge(left,right)
        return merge_sort(nums)






























    # def sortArray(self, nums: List[int]) -> List[int]:
    #     def quicksort(l,r):
    #         if l>=r:
    #             return
            
    #         pivot_idx=random.randint(l,r)
    #         nums[l],nums[pivot_idx]=nums[pivot_idx],nums[l]
    #         pivot=nums[l]

    #         i,j=l,r

    #         while i<j:
    #             while i < j and nums[j] >= pivot:
    #                 j-=1
    #             while i < j and nums[i] <= pivot:
    #                 i+=1
                
    #             nums[i], nums[j] = nums[j], nums[i]
    #         nums[l], nums[i] = nums[i], nums[l]
    #         quicksort(l, i - 1)
    #         quicksort(i + 1, r)
    #     quicksort(0,len(nums)-1)
    #     return nums