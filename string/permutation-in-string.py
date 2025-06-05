class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1如果比s2长，那就不行
        if len(s1)>len(s2):
            return False

        #给s1计数
        s1_count = Counter(s1)
        window_count=Counter()

        for i in range(len(s2)):
            # Add current character to the window
            window_count[s2[i]]+=1

             # Shrink window from the left if window size exceeds s1
            if i>= len(s1):
                left_char = s2[i-len(s1)]
                #如果该字符在窗口中只出现 1 次，我们就直接删除它（del），这样可以减少字典的空间占用
                if window_count[left_char] == 1:
                    del window_count[left_char]
                #如果该字符出现了不止一次，就把它的计数减 1
                else:
                    window_count[left_char] -= 1
            #当前滑动窗口中字符的计数是否和 s1 中字符计数完全一致。
            if window_count == s1_count:
                return True
        
        return False

            
        