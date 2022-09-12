class MyQueue:

    def __init__(self):
        self.__queue = []
        
    def push(self, x):
        self.__queue.append(x)
        

    def pop(self):
        return self.__queue.pop(0)
        

    def peek(self):
        return self.__queue[0]
        

    def empty(self):
        if len(self.__queue) > 0:
            return False
        return True

obj = MyQueue()
obj.push(1)
print(obj.pop())
print(obj.queue)