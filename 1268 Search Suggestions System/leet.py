class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode():
            def __init__(self):
                self.children = {}
                self.word = False

        def build_tire(words):
            root = TrieNode()
            for word in words:
                curr = root
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                curr.word = True
            return root

        def search_trie(trie, prefix):
            a = []

            def dfs(node, word, i):
                if node.word and i >= len(prefix):
                    a.append(word)
                for ch, n in sorted(node.children.items()):
                    if i < len(prefix):
                        if prefix[i] == ch:
                            dfs(n, word + ch, i + 1)
                    else:
                        dfs(n, word + ch, i + 1)

            dfs(trie, "", 0)

            return a[:3]



        trie = build_tire(products)

        ans = []
        for i in range(len(searchWord)):
            ans.append(search_trie(trie, searchWord[:(i + 1)]))

        return ans