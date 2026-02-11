class Solution:
    def findValidPair(self, s: str) -> str: 
        count = Counter(s)
        s_list = list(s)
        print(s_list,count)

        for left in range(0,len(s_list)-1):
            right = left+1
            # print( s_list[left], s_list[right] )
            # left_count = count[str(left)]
            # right_count = count[str(right)]
            # print(left_count, right_count)
            if s_list[left] != s_list[right]:
                left_count = count[s_list[left]]
                right_count = count[s_list[right]]

                if left_count == int(s_list[left]) and right_count == int(s_list[right]):
                    return s[left:right+1]
        return ""
                


        

        