class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self.trie
        for i in range(len(word)):
            if i < len(word) - 1:
                if word[i] not in t:
                    t[word[i]] = {}
                t = t[word[i]]
            else:
                t[word[i] + "="] = None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for i in range(len(word)):
            if i < len(word) - 1:
                if word[i] in t:
                    t = t[word[i]]
                else:
                    return False
            else:
                if word[i] + "=" in t:
                    return True
                else:
                    return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for i in range(len(prefix)):
            if i < len(prefix) - 1:
                if prefix[i] in t:
                    t = t[prefix[i]]
                else:
                    return False
            else:
                if prefix[i] in t:
                    return True
                elif prefix[i] + "=" in t:
                    return True
                else:
                    return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

