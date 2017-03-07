class QueueNG(object):

    def __init__(self):
        #pop from beginning of the queue
        #push to end of the queue
        self.list = []

    #push
    def add(self, value):
        self.list.append(value)

    #pop
    def remove(self):
        if not self.isEmpty():
            value = self.list[0]
            del self.list[0]
            return value

    #peek
    def peek(self):
        if not self.isEmpty():
            return self.list[0]

    #tail
    def tail(self):
        return self.list[-1]

    def length(self):
        return len(self.list)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def contains(self, value):
        if value in self.list:
            return True
        return False