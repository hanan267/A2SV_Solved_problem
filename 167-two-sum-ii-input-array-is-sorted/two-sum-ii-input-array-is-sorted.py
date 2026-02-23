class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # find the difference
        # then search index of the difference
        # if greater that the first print solution other wise continue 
            # Slower

        # n = len(numbers)
        # i = 0
        # diff = 0
        # index2 = 0
        
        # while (i < n):
        #     diff = target - numbers[i]
        #     if (diff in numbers):
        #         index2 = numbers.index(diff)
        #         # if (index2 != i):
                    
        #     if (index2 > i):
        #         return [i+1, index2+1]

            ### Accurate one

        # take two pointers, from the left and from the right
        # add the two opposite indix numbers 
        # if greater than the target move the right one to the left
        # if less than the target move the left one to the left

    #  i, j = 0, len(numbers) - 1
    #  added = 0

    #  while (i<j):
    #     added = numbers[i] + numbers[j]
    #     if (added == target):
    #         return [i+1, j+1]
    #     elif (added > target):
    #         j -= 1
    #     else:
    #         i += 1

        i, j = 0, len(numbers)-1
        while (i<j):
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]

        


           
        