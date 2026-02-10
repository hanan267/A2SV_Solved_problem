class Solution:
    def longestConsecutive(self, nums):
        # numSet = set(nums)
        # longest = 0

        # for n in numSet: 
        #     if (n - 1) not in numSet: 
        #         length = 1
        #         while (n + length) in numSet:
        #             length += 1
        #         longest = max(longest, length)

        # return longest


        numSet = set(nums)
        longest = 0

        for i in numSet:
            print(i)
            if (i-1) not in numSet:
                length = 1
                print(length+1)
                while (length+i) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

















