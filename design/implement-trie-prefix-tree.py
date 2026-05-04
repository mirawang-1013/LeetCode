from typing import defaultdict

class Trie:

    def __init__(self):
        self.child=defaultdict(dict)
        

    def insert(self, word: str) -> None:
        node=self.child
        for w in word:
            if w not in node.keys():
                node[w]=defaultdict(dict)
            node=node[w]
        node['#']='#'
        

    def search(self, word: str) -> bool:
        node=self.child
        for w in word:
            if w in node.keys():
                node=node[w]
            else:
                return False
        return '#' in node.keys()
    
        

    def startsWith(self, prefix: str) -> bool:
        node=self.child
        for w in prefix:
            if w in node.keys():
                node=node[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)