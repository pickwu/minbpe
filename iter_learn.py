import random
"""
将数据data按照batch分成n份，循环执行epoch次
"""
class MyIter:
    def __init__(self,batch=8):
        self.batch = batch
        self.data = [random.randint(1,100) for _ in range(30)]
        self.index = 0
        self.len = len(self.data) / self.batch

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.len - 1:
            min_data = self.data[self.batch * self.index:self.batch * (self.index + 1)]
            self.index += 1
            return min_data
        else:
            raise StopIteration # 注意是raise 不是return

if __name__=="__main__":
    for epoch in range(2):
        for batch_data in MyIter(batch=7): # 循环的本质：MyIter(batch=7).__next__，等价于next(MyIter(batch=7))
            print(batch_data)

