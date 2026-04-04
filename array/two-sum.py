class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in pairs:
                return [i,pairs[diff]]
            if num not in pairs:
                pairs[num]=i
                
                