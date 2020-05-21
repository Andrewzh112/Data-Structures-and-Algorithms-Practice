class node:
    def __init__(self,key=None,val=None,nex=None):
        self.key=key
        self.val=val
        self.next=next


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key2prev={}
        self.dummy=node()
        self.tail=self.dummy
        self.capacity=capacity


    """
    @param: key: An integer
    @return: An integer
    """
    def pop_front(self):
        pop=self.dummy.next
        del self.key2prev[pop.key]
        
        self.dummy.next=pop.next
        self.key2prev[self.dummy.next.key]=self.dummy
        
        
    def add_back(self, node):
        self.tail.next=node
        self.key2prev[node.key]=self.tail
        self.tail=self.tail.next
        
        
    def kick(self, prev):
        curr=prev.next
        if curr==self.tail:
            return
        prev.next=curr.next
        self.key2prev[curr.next.key]=prev
        self.add_back(curr)
        
        
    def get(self, key):
        # write your code here
        if key not in self.key2prev:
            return -1
        prev=self.key2prev[key]
        curr=prev.next
        self.kick(prev)
        return curr.val
        
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key not in self.key2prev:
            new_node=node(key,value)
            self.add_back(new_node)
            if len(self.key2prev)>self.capacity:
                self.pop_front()
            return
        prev=self.key2prev[key]
        curr=prev.next
        curr.val=value
        self.kick(prev)
        