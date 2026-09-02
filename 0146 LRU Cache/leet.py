class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, n):
        n.prev.next, n.next.prev = n.next, n.prev

    def insert(self, node):
        n, p = self.left.next, self.left
        node.next = n
        node.prev = p
        self.left.next = node
        n.prev = node


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
        else:
            if len(self.dict) == self.capacity:
                node = self.right.prev
                self.remove(node)
                del self.dict[node.key]
        n = Node(key, value)
        self.dict[key] = n
        self.insert(n)

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        n = self.dict[key]
        self.remove(n)
        self.insert(n)
        return n.value





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)