import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=Counter(nums)
        a=list(count.items())
        output=[]
        for i in range(k):
            output.append(a[i][0])
        return output

        
        