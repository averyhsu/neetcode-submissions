# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, key =0,next=None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} #creates hash dictionary
        self.size = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        else:
            node = self.cache.get(key)
            # remove in chain
            node.prev.next = node.next #change prev ptr
            node.next.prev =node.prev #change next ptr
            #add to tail
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            #edit node's ptr
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:#key doesn't exist
            self.size = self.size+1
            if(self.size>self.capacity):#oversize, delete first
                del self.cache[self.head.next.key]
                # remove head from chain
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                #reset size
                self.size = self.size-1
            # add to chain end
            node = ListNode(value,key, next = self.tail)
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            # add to cache
            self.cache[key] = node
         
        else:#key exist
            node = self.cache.get(key)
            node.val = value
            # move the to most recent
            self.get(key)



            
        
