import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank = defaultdict(list)
        freq = Counter(nums)
        result = []
        for i in range(k):
          a=list(freq.keys())[i]
          result.append(a)
        return result
        

        
        