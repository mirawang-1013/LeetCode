

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False

class TrieTree:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        node = self.root
        for w in word:#构造词典
            node = node.children[w]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = TrieTree()
        node = trie.root
        for word in words:
            trie.insert(word)
        direcs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,"",i,j,res,direcs)
        return res
    
    def dfs(self,board,node,path,i,j,res,direcs):
        if node.isWord:
            res.append(path)
            node.isWord = False
        #不合法的直接返回
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp,None) #不存在就返回None
        if not node:
            return 
        #合法路径，继续搜索
        board[i][j]= '#'
        for dx,dy in direcs:
            self.dfs(board,node,path+tmp,i+dx,j+dy,res,direcs)
        board[i][j] = tmp

        