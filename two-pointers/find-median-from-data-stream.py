class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num) #把数先加到small堆的堆顶
        heappush(self.large, -heappop(self.small)) #把数加到大堆的堆顶

        if len(self.large)>len(self.small)+1:
            #如果大堆的数比小堆的多，那就把大堆的数移到小堆
            heappush(self.small, -heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/ 2.0
        return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()