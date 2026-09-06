class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
       
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        seen = {"0000"}

        while q:
                s, steps = q.popleft()
                if s == target:
                    return steps
                    
                for i in range(4):
                    n = int(s[i])
                    for x in [-1, 1]:
                        d = (n + x) % 10
                        ns = s[:i] + str(d) + s[i+1:]
                        if ns not in dead and ns not in seen:
                            seen.add(ns)
                            q.append((ns, steps + 1))

        return -1