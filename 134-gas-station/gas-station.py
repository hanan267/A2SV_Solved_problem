class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        tg = 0
        tc = 0
        cur = 0
        st = 0
        for i in range(len(gas)):
            tg += gas[i]
            tc += cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                st = i + 1
                cur = 0
        if tg < tc:
            return -1
        return st