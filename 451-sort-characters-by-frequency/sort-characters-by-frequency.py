class Solution:
    def frequencySort(self, s: str) -> str:
#         # naive approach
#             # create a hash map and count the frequecy
#             # create a dictionary of list and map the character and the count
#             # sort by count
#             # then append it to ann array
#             # the convert the array to a string

#             freq = {}
#             for i in range(len(s)):
#                 if s[i] not in freq:
#                     freq[s[i]] = 1
#                 else:
#                     freq[s[i]] += 1

#             freq_list = []
#             for char in freq:
#                 freq_list.append((char, freq[char]))

#             freq_list.sort(key=lambda x: x[1], reverse=True)

#             result = []
#             for char,cnt in freq_list:
#                 result.append(char*cnt)
#             return "".join(result)
            

#             # optimized approach
#             from collections import Counter, defaultdict

#         def frequencySort(self, s: str) -> str:
#             count = Counter(s)             # char -> frequency
#             buckets = defaultdict(list)   # freq -> list of chars having that freq

#             for char, cnt in count.items():
#                 buckets[cnt].append(char) # group chars by their frequency

#             res = []
#             for i in range(len(s), 0, -1):# iterate possible frequencies from max to 1
#                 for c in buckets[i]:      # for each char that appears exactly i times
#                     res.append(c * i)    # append that char repeated i times
#             return "".join(res)           # join all pieces into final string

        c = Counter(s)
        # print(c)
        Sort = sorted(c, key=c.get, reverse=True)
        # print(Sort)
        res = ""
        for char in Sort:
            # temp = c[char]
            res += (char*c[char])

        return res





            
        