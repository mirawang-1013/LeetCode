from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l,r):
            if l>=r:
                return
            
            pivot_idx=random.randint(l,r)
            nums[l],nums[pivot_idx]=nums[pivot_idx],nums[l]
            pivot=nums[l]

            i,j=l,r

            while i<j:
                while i < j and nums[j] >= pivot:
                    j-=1
                while i < j and nums[i] <= pivot:
                    i+=1
                
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]
            quicksort(l, i - 1)
            quicksort(i + 1, r)
        quicksort(0,len(nums)-1)
        return nums