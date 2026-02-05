class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # store each words with their indexx in a hash map the first occurance
        # then after storing check if list one word exists in thr list two
        # if exist add the index track the min as going using new hash map
        # print it at the end

        list1_hash = {}
        for idx, words in enumerate(list1):
            if words not in list1_hash:
                list1_hash[words] = idx
        list2_hash = {}
        for idx, words in enumerate(list2):
            if words not in list2_hash:
                list2_hash[words] = idx

        idx_sum = {}
        for word, idx in list1_hash.items():
            if word in list2_hash:
                idx_sum[word] = idx + list2_hash[word]
        minSum = 10**18
        for value in idx_sum.values():
            if value < minSum:
                minSum = value
        print(minSum)
        result = []
        for key, value in idx_sum.items():
            if value == minSum:
                result.append(key)
        return result




        # min_idx = 0
        # commonString = []
        # for word, idx in list1_hash.items():
        #     if word in list2_hash:
        #         sum_idx = idx + list2_hash[word]
        #     if sum_idx <= min_idx:
        #         min_idx = sum_idx
        #         commonString.append


        # return 

        



        