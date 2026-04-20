class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #方法一：set()
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        #方法二：counter
        # count = Counter(nums)
        # for num, count in count.items():
        #     if count>1:
        #         return True
        # return False
        # #hashmap
        # seen={}
        # for num in nums:
        #     seen[nums]=seen.get(nums,0)+1
        # return [num for num, count in seen.items() if count>1]

        # #Counter
        # counts=Counter(nums)
        # return [num for num, count in counts.items() if count>1]