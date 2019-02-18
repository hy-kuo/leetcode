class Node:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.nxt = next_node
        
class LRUCache:

    def __init__(self, capacity: 'int'):
        self.prev_add = {}
        self.cap = capacity
        self.cache = {}
        self.lru = None 
        self.tail = None 
        
    def get(self, key: 'int') -> 'int':
        if key in self.cache:
            if self.tail.key == key:
                return self.cache[key]
            if self.lru.key == key:
                node = self.lru
                self.lru = node.nxt
                self.prev_add[node.nxt.key] = None
                
            else:
                node = self.prev_add[key].nxt
                self.prev_add[key].nxt = node.nxt
                self.prev_add[node.nxt.key] = self.prev_add[key]
            
            # set node to tail
            tail = self.tail
            tail.nxt = node
            self.tail = node
            self.tail.nxt = None
            self.prev_add[key] = tail
            return self.cache[key]
        else:
            return -1
            
            
                


    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.cache:
            if self.tail.key == key:
                self.cache[key] = value
                return
            if self.lru.key == key:
                node = self.lru
                self.lru = node.nxt
                self.prev_add[node.nxt.key] = None
                
            else:
                node = self.prev_add[key].nxt

                self.prev_add[key].nxt = node.nxt
                self.prev_add[node.nxt.key] = self.prev_add[key]
        else:
            node = Node(key, value, None)
        
        # set node to tail
        if len(self.cache) == 0:
            self.lru = node
            self.tail = node
            self.prev_add[key] = None
        else:
            tail = self.tail
            tail.nxt = node
            self.tail = node
            self.tail.nxt = None
            self.prev_add[key] = tail
        self.cache[key] = value
        
        if len(self.cache) > self.cap:
            node_to_del = self.lru
            self.lru = self.lru.nxt if self.lru.nxt else None
            if self.tail.key == node_to_del.key:
                self.tail = None
            del self.cache[node_to_del.key]
            del self.prev_add[node_to_del.key]
            del node_to_del
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)