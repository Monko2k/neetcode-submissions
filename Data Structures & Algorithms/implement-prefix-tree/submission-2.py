class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        i = 0
        node = self.trie
        while i < len(word):
            c = word[i]
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]
            i += 1
        node.word = True

    def search(self, word: str) -> bool:
        i = 0
        node = self.trie
        while i < len(word):
            c = word[i]
            if c not in node.children:
                return False
            node = node.children[c]
            i += 1
        
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        node = self.trie
        while i < len(prefix):
            c = prefix[i]
            if c not in node.children:
                return False
            node = node.children[c]
            i += 1
        
        return True
        
        