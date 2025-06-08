class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = []
        for i in range(len(nums)):
            com_value = target-nums[i]
            if com_value in nums and i not in pairs:
                j=nums.index(com_value)
                if i!=j:
                  pairs.append(i)
                  pairs.append(j)
        return pairs



#nums.index(i)