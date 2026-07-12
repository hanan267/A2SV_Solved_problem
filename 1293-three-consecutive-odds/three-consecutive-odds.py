class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:


        count = 0
        for right in range(len(arr)):
            # print(arr[right])
            # print(arr[right] % 2 != 0)
            if arr[right] % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

            


        