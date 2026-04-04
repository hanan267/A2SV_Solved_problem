class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def feasible(radius):
            house_idx = 0
            heater_idx = 0

            while house_idx < len(houses):
                if heater_idx >= len(heaters):
                    return False

                min_coverage = heaters[heater_idx] - radius
                max_coverage = heaters[heater_idx] + radius

                if houses[house_idx] < min_coverage:
                    return False
                if houses[house_idx] > max_coverage:
                    heater_idx += 1
                else:
                    house_idx += 1

            return True

        left, right = 0, int(1e9)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index