class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,value in enumerate(nums):
            gap=target-value
            if gap in nums and gap!= target:
                j = nums.index(gap)
                if i!=j:
                    return [i,j]
                