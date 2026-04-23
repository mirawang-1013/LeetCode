#前缀树： 树的每个节点储存一个字符，进行树的叶子结点不断地增加
#       root
#      a    w
#      p    o
#      p    r
#     l     d
#     e    #
      #


class Trie:
    def __init__(self):
        self.child = collections.defaultdict(dict)

    
    def insert(self, word:str) -> None:
        node = self.child
        for w in word:
            if w not in node.keys():
                node[w] = collections.defaultdict(dict)
            node = node[w]
        node['#'] = '#'
        
    def search(self,word:str)-> bool:
        node = self.child
        for w in word:
            if w in node.keys():
                node = node[w]
            else:
                return False
        return '#' in node.keys() 


    def startsWith(self, prefix:str) -> bool:
        node = self.child
        for w in prefix:
            if w in node.keys():
                node = node[w]
            else:
                return False
        return True




