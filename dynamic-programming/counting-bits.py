class Solution:
    def countBits(self, n: int) -> List[int]:
        ones_count = []
        for i in range(n+1):
            binary = bin(i)[2:] #去掉'0b'作为前缀，得到二进制表达式
            ones = binary.count('1') #数表达式中有多少个1
            ones_count.append(ones) #把1的数量列出来
        return ones_count
        