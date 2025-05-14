class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):# 32 bits for a 
            bit = n & 1 # 1 and number = number itself
          
            # shift last bit to the left bit and leave room for the next bit
            res = (res<<1)|bit

            #shif the n bit to the right and ready for pushing to the result
            n>>=1 
        return res


        