class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # naive approach
            # iterate over nums1 element
            # for elements find its index in the nums2
            # then iterate from index+1 to last element of nums2
            # find next bigger element 
        
        # for i in range(len(nums1)): # O(n)
        #     next_big = -1
        #     idx = nums2.index(nums1[i]) #O(n)
        #     for j in range(idx+1, len(nums2)):#O(m)
        #         if nums2[j] > nums1[i]:
        #             next_big = nums2[j]
        #             break
        #     nums1[i] = next_big
        # return nums1
        # time complexity: O(n^2)
        # space complexity: O(1)
                # optimized approaxh
                    # store index and value of elements of nums1
                    # iterate over nums2
                    # in the pass store values in to stack if exists in the nums1 hashmap
                    # res[idx] = nums2[i]
                    ## idx = numsIdx[val]
                    # if the stack is not empity and last value is greater than current element put it in the index of nums1


            # numsIdx = { n:i for i, n in enumerate(nums1)}
            res = [-1]*len(nums1)

            stack = []
            hashm = {}
            for i in range(len(nums2)):
                while stack and nums2[i] > stack[-1]:
                    big = stack.pop()
                    hashm[big] = nums2[i]
                stack.append(nums2[i])
                # print(nums2[i], stack)
            for idx, num in enumerate(nums1):
                if num in hashm:
                    res[idx] = hashm[num]
            return res


            
       