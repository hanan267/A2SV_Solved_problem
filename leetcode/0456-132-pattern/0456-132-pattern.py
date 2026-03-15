class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        # stack = []
        # for i in range(len(nums)):
        #     while stack and stack[-1] > nums[i]:
        #         if len(stack) >= 2 and stack[0] < nums[i]:
        #             return True
        #         stack.pop()    
                
                   

        #     stack.append(nums[i])
        # return False

        stack = []
        smaller = nums[0]

        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num < stack[-1][0] and num > stack[-1][1]:
                return True
            
            stack.append([num, smaller])
            smaller = (min(num, smaller))
        return False




        