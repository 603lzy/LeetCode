class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.queue:
            self.queue.remove(self.queue[0])
    

    def peek(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False
