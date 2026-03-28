from collections import defaultdict
#思路是，找出频率最高的count, 然后窗口长度减count，得到差值，
#如果差值=k,那最长的窗口长度可以等于max_count+k
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        left=0
        max_count=0
        result=0
        for right in range(len(s)):
            count[s[right]]+=1
            max_count=max(count[s[right]],max_count)
            while (right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
            result=max(right-left+1,result)
        return result
                


















        # #count: 保存当前窗口中每个字符出现的次数
        # #max_count: 当前窗口中出现次数最多的某个字符的频率
        # count = defaultdict(int)
        # max_count=0
        # left=0
        # result=0

        # for right in range(len(s)):
        #     #每次向右扩大窗口，把 s[right] 加进来，更新它在窗口中的频率，并更新 max_count
        #     count[s[right]] +=1
        #     #计算最大的count,either是历史有过更大的，或者是目前窗口里
        #     max_count = max(max_count, count[s[right]])
        #    # 窗口长度-最高频的次数
        #     while(right-left+1)-max_count>k:
        #         count[s[left]] -=1
        #         left+=1

        #     result=max(result,right-left+1)

        # return result


        