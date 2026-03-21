class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for a in range(len(numbers)):
            
            b=target -numbers[a]
            if b in numbers:
                b_index=numbers.index(b)
                return [a+1,b_index+1]
        