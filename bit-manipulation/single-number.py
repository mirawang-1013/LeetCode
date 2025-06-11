class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = Counter(nums)
        # for num,count in result.items(): 这种写法错在了只看第一项
        #     return num if count==1 else null
        for num,count in result.items():
          if count == 1:
            return num

        