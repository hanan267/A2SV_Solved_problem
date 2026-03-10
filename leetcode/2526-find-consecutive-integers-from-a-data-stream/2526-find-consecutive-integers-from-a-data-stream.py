class DataStream:

    def __init__(self, value: int, k: int):
        self.data = [value, k]       
        self.count = 0
    def consec(self, num: int) -> bool:
        
        if num != self.data[0]:
            self.count = 0
            
        elif num == self.data[0]:
            self.count += 1
        
        
        return self.count >= self.data[1]
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)