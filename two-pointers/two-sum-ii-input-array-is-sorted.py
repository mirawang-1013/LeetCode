class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs=defaultdict()
        for i,value in enumerate(numbers):
            diff=target-value
            if diff in pairs:
                return [pairs[diff]+1,i+1]
            pairs[value]=i
        return None
        # left, right = 0,len(numbers)-1
        # while left<right:
        #     total=numbers[left]+numbers[right]
        #     if total==target:
        #         return [left+1, right+1]
        #     if total<target:
        #         left+=1
        #     if total>target:
        #         right-=1