class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.trie

        for ch in word:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
        if curr.word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for ch in prefix:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)