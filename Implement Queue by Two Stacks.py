class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1=[]
        self.stack2=[]
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.transfer(self.stack1, self.stack2)
        pop = self.stack1.pop()
        self.move(self.stack2, self.stack1)
        return pop
        
    def transfer(self, stack1, stack2):
        while len(stack1) > 1:
            stack2.append(stack1.pop())
            
    def move(self, stack1, stack2):
        while len(stack1) > 0:
            stack2.append(stack1.pop())
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.transfer(self.stack1, self.stack2)
        top = self.stack1[-1]
        self.move(self.stack2, self.stack1)
        return top
