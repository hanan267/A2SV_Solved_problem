class FrequencyTracker:
    
    def __init__(self):
        self.count = defaultdict(int) # num --> freq
        self.freq_count = defaultdict(int)
    def add(self, number: int) -> None:
        old_count = self.count[number]
        new_count = old_count+1

        self.count[number] = new_count
        if self.freq_count[old_count] > 0:
            self.freq_count[old_count] -= 1
        self.freq_count[new_count] += 1


    def deleteOne(self, number: int) -> None:
        if self.count[number] == 0:
            return
        old_count = self.count[number]
        new_count = old_count-1

        self.count[number] = new_count
        # if self.count[old_count] > 0:
        self.freq_count[old_count] -=1
        self.freq_count[new_count] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return (self.freq_count[frequency]) > 0
        
        # if count[frequency] == 1:
        #     return 
          


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)