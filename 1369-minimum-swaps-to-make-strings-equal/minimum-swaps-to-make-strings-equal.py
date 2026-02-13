class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            return -1
        count1 = Counter(s1)
        count2 = Counter(s2)
        # print(count1, count2)
        hash_map = defaultdict(int)
        for i in range(n1):
            if (count1["x"] + count2["x"])% 2 != 0:
                return -1
            if (count1["y"] + count2["y"])% 2 != 0:
                return -1
            
            if s1[i] != s2[i]:
                # print(s2[i], s1[i])
                hash_map[s1[i] + s2[i]] += 1

       
        # print(hash_map)
        oper = 0
        remainder = 0
        for key, value in hash_map.items():
            # print(value)
            oper += value // 2
            remainder += value % 2
        return oper+remainder

