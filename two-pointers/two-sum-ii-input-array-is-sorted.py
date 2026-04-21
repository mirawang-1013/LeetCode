class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #method1
        left,right=0,len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total>target:
                right=right-1
            else:
                left=left+1
            




        #method2
        # pairs=defaultdict()
        # for i,value in enumerate(numbers):
        #     diff=target-value
        #     if diff in pairs:
        #         return [pairs[diff]+1,i+1]
        #     pairs[value]=i
        # return None


        #method3
        # left, right = 0,len(numbers)-1
        # while left<right:
        #     total=numbers[left]+numbers[right]
        #     if total==target:
        #         return [left+1, right+1]
        #     if total<target:
        #         left+=1
        #     if total>target:
        #         right-=1