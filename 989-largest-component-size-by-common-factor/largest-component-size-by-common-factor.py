class UnionFind:
  
  
    def __init__(self, n: int) -> None:
      
        self.parent = list(range(n))
  
    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)       
        if root_a != root_b:
            self.parent[root_a] = root_b
  
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_value = max(nums)
        union_find = UnionFind(max_value + 1)
        for num in nums:
            factor = 2
            while factor * factor <= num:
                if num % factor == 0:
                    union_find.union(num, factor)
                    union_find.union(num, num // factor)
                factor += 1
        component_sizes = Counter(union_find.find(num) for num in nums)
        return max(component_sizes.values())