class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in pair:
                return [i,nums.index(complement)]
            else:
                pair.append(nums[i])

#记住这个返回index的公式，index()