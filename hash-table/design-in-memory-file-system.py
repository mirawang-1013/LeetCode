from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()

    def _walk(self, path, create=False):
        node = self.root
        if path == "/":
            return node

        parts = path.strip("/").split("/")
        for part in parts:
            if part not in node.children:
                if not create:
                    return None
                node.children[part] = Node()
            node = node.children[part]

        return node

    def ls(self, path: str) -> List[str]:
        node = self._walk(path)

        if node.is_file:
            return [path.split("/")[-1]]

        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._walk(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath, create=True)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._walk(filePath)
        return node.content