class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.size = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)


        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            del self.queue[self.Front()]

        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        front = self.queue[0]
        return front
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        rear = self.queue[-1]
        return rear
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.Rear() == self.Front():
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.Rear()+1) % self.size == self.Front():
            return True

    def ShowQueue(self):
        for i in range(self.size):
            print(self.queue[i], end=',')
        print(' ')

if __name__ == '__main__':
    a = MyCircularQueue(9)
    for i in range(8):
        a.enQueue(i)
    a.ShowQueue()





# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()