from collections import defaultdict


def spruce(n):
  nodes = {}
  parents = set()
  for i in range(n-1):
    root = int(input())
    nodes[i+2] = root
    parents.add(root)
    
  
  for val in parents:
    if val in nodes:
       del nodes[val]
  
  

  counter = defaultdict(int)

  for value in nodes.values():
      counter[value] += 1
  
  for parent in parents:
     if counter[parent] < 3:
        return "No"
  return "Yes"

 

n = int(input())
print(spruce(n))