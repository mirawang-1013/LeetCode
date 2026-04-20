class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoder=''
        for s in strs:
            length =str(len(s))
            encoder+=length
            encoder+='#'
            encoder+=s
        return encoder

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i=0
        decoder=[]
        
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            decoder.append(s[j+1:j+1+length])
            i=j+1+length
        return decoder
            

    




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


#encoder
        # encode=''
        # for i in strs:
        #     length = len(i)
        #     encode+=str(length)+'#'+i
        # return encode

#decoder
        # res=[]
        # i=0
        # while i<len(s):
        #     j=i
        #     while s[j] !='#':
        #         j+=1
        #     length = int(s[i:j])
        #     res.append(s[j+1:j+1+length])
        #     i=j+1+length
        # return res