"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
       
        n = len(employees)
        sub = defaultdict(list)

        for i in range(n):
         sub[employees[i].id].append(employees[i].importance)
         sub[employees[i].id].append(employees[i].subordinates)

    
        res = 0
        def dfs(id, res):
           res = sub[id][0] 
           if sub[id][1] != []:
               for ids in sub[id][1]:
                  res += dfs(ids, res)
           return res
        return dfs(id, res)

         
         
        