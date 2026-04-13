class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()

        def feseabible(radius):

            house_idx = 0
            heater_idx = 0
            
            while house_idx < len(houses):
                if heater_idx >= len(heaters):
                    return False
                
                min_range = heaters[heater_idx] - radius
                max_range = heaters[heater_idx] + radius


                if houses[house_idx] < min_range:
                    return False
                if houses[house_idx] > max_range:
                    heater_idx += 1
                else:
                    house_idx += 1
            return True
        
        feasible_idx = -1
        left, right = 0, int(1e9) 

        while left <= right:
            mid = (left+right) // 2
            if feseabible(mid):
                feasible_idx = mid 
                right = mid - 1
            else:
                left = mid + 1

        return feasible_idx

                    
                