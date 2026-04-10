class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):
            res = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            res.extend(arr1[i:])
            res.extend(arr2[j:])
            return res


        def mergeSort(left, right, nums):
            if left == right:
                return [nums[left]]
            mid = left + (right - left)// 2
            left_half = mergeSort(left, mid, nums)
            right_half = mergeSort(mid+1, right, nums)

            return merge(left_half, right_half)

        return mergeSort(0, len(nums)-1, nums)
        
        