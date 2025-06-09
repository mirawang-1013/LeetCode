class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[nums[0]]]
        ans = []
        for i in range(len(nums)):
            first = [nums[i]]
            others = nums[:i]+nums[i+1:]
            tmp= self.permute(others)
            for x in tmp:
                ans.append(first+x)
        return ans
            

        