class NumArray:

    def __init__(self, nums: List[int]):
       self.pref = [0]*(len(nums)+1) 
       self.temp = self.pref[0]
       for i in range(len(nums)):
            self.temp += nums[i]
            self.pref[i] = self.temp
       print(self.pref)

    def sumRange(self, left: int, right: int) -> int:
        self.range = self.pref[right]-self.pref[left-1]

        # print(self.pref[right+1])
        # print(self.pref[left])
        return self.range
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)