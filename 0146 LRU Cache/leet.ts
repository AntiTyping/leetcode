class Node {
    key: number
    value: number
    next: Node
    prev: Node

    constructor(key: number, value: number) {
        this.key = key
        this.value = value
    }
}

class LRUCache {
    capacity: number
    cache: Map<number, Node>
    head: Node
    tail: Node

    constructor(capacity: number) {
        this.capacity = capacity
        this.cache = new Map<number, Node>()
        this.head = new Node(0, 0)
        this.tail = new Node(0, 0)
        this.head.next = this.tail
        this.tail.prev = this.head
    }


    get(key: number): number {
        if (this.cache.has(key)) {
            const node = this.cache.get(key)
            this.remove(node)
            this.insert(node)
            return node.value
        }
        return -1
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            const node = this.cache.get(key)
            this.remove(node)
        } else {
            if (this.cache.size == this.capacity) {
                const node = this.tail.prev
                this.remove(node)
                this.cache.delete(node.key)
            }
        }
        const node = new Node(key, value)
        this.insert(node)
        this.cache.set(key, node)
    }

    insert(node: Node) {
        const n = this.head.next
        const p = this.head
        p.next = node
        n.prev = node
        node.next = n
        node.prev = p
    }

    remove(node: Node) {
        const n = node.next
        const p = node.prev
        p.next = n
        n.prev = p
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */