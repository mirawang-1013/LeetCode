class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        for i in range(0,len(nums)):
            complement = target-nums[i]
            if complement in nums:
              j = nums.index(complement)
              # p = (i,j)
              # p=sorted(p)
              if j!=i and j not in pair:
                pair.append(j)
                pair.append(i)
                pair = sorted(pair)
        return pair