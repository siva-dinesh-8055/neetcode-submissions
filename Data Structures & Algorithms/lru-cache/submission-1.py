class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node() 
        self.tail = Node() 
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.mapp = dict() 
        self.capacity = capacity

    def add(self, node):
        self.mapp[node.key] = node
        headNext = self.head.next 
        node.next = headNext 
        node.prev = self.head 
        headNext.prev = node 
        self.head.next = node 
        
    def remove(self, node):
        node.next.prev = node.prev 
        node.prev.next = node.next 
        self.mapp.pop(node.key) 

    def get(self, key: int) -> int:
        if key in self.mapp:
            node = self.mapp[key]
            self.remove(node) 
            self.add(node) 
            return self.head.next.val

        return -1 

    def put(self, k: int, v: int) -> None:
        if k in self.mapp:
            self.remove(self.mapp[k]) 

        elif len(self.mapp) >= self.capacity:
            self.remove(self.tail.prev) 
            
        newNode = Node(k, v)
        self.add(newNode) 