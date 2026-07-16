class trieNode:
    def __init__(self):
        self.is_word = False
        self.child = dict()

class PrefixTree:

    def __init__(self):
        self.root = trieNode()        

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                new = trieNode()
                cur.child[ch] = new
            cur = cur.child[ch]
        cur.is_word = True



    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                return False
            #so in cur
            cur = cur.child[ch]
        return cur.is_word
        


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.child:
                return False
            #so in cur
            cur = cur.child[ch]
        return True
        