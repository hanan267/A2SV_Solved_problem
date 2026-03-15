class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

            diff = []
            for i in range(len(costs)):
                diff.append([costs[i][1]-costs[i][0], costs[i][0], costs[i][1]])
            
            diff.sort()
            cost = 0
            for i in range(len(costs)):
                if i < len(costs) // 2:
                    cost += diff[i][2]
                else:
                    cost += diff[i][1]
            return cost



            

        