import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #方法一：heap
        count = Counter(nums)
        heap=[]
        for num, freq in count.items():
            heapq.heappush(heap,(freq, num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]




    #方法二：最快的方法是这个most_common 
        # count=Counter(nums)
        # return [num for num,freq in count.most_common(k)]
    
        
        