import sys
input = sys.stdin.readline
def func(): return int(input())
def numbers(): return map(int, input().split())
def lists(): return list(map(int, input().split()))

class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.size = [1] * n
    self.experience = [0] * n
  
  def find(self, x):
    while x != self.parent[x]:
      x = self.parent[x]
    return x
  
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return False
    if self.size[y] > self.size[x]:
      x, y = y, x
    self.parent[y] = x
    self.size[x] += self.size[y]
    self.experience[y] -= self.experience[x]
    return True

  def add(self, x, v):
    r = self.find(x)
    self.experience[r] += v
  
  def get(self, x):
    res = 0
    while x != self.parent[x]:
      res += self.experience[x]
      x = self.parent[x]
    res += self.experience[x]
    return res

n, m = numbers()
dsu = UnionFind(n + 1)
for _ in range(m):
  info = input().split()
  if info[0] == 'add':
    x = int(info[1])
    v = int(info[2])
    dsu.add(x, v)
  elif info[0] == 'join':
    x = int(info[1])
    y = int(info[2])
    dsu.union(x, y)
  else:
    x = int(info[1])
    res = dsu.get(x)
    print(res)