class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
            ## first solution
        # outPut = {}
        # for i in range(len(nums1)):
        #     if nums1[i] in nums2 and nums1[i] not in outPut:
        #         outPut.append(nums1[i])
        # return outPut

              ## second solution 
        
        # mySet = set(nums1)
        # outPut = []

        # for i in range(len(nums2)):
        #     if nums2[i] in mySet:
        #         outPut.append(nums2[i])
        #         mySet.remove(nums2[i])

        # return outPut

        nums1set = set(nums1)
        res = []
        for num in nums2:
            if num in nums1set:
                res.append(num)
                nums1set.remove(num)
        return res




        