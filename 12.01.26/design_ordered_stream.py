class OrderedStream(object):

    def __init__(self, n):
        self.n = n
        self.stream = [None] * (n +1)
        self.ptr = 1      
        

    def insert(self, idKey, value):
        self.stream[idKey] = value
        res = []
        while self.ptr <= self.n and self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
