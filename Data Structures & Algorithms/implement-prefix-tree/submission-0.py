class PrefixTree:

    def __init__(self):
        self.root = dict()
        self.termSignal = "TERM"

    def insert(self, word: str) -> None:
        curDict = self.root
        for char in word:
            if char not in curDict:
                curDict[char] = dict()
            curDict = curDict[char]
        curDict[self.termSignal] = dict()


    def search(self, word: str) -> bool:
        curDict = self.root
        for char in word:
            if char not in curDict:
                return False
            curDict = curDict[char]
        return self.termSignal in curDict

    def startsWith(self, prefix: str) -> bool:
        curDict = self.root
        for char in prefix:
            if char not in curDict:
                return False
            curDict = curDict[char]
        return True
        
        