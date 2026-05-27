class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer=[]
        for i in range(len(nums)-k+1):
            new_nums=nums[i:i+k]
            max_sum=max(new_nums)
            answer.append(max_sum)
        return answer


        