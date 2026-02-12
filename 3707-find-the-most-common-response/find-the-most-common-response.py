class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        # remove the duplicate
        # count
        remove_dup = set()
        


        for i in range(len(responses)):
            responses[i] = list(set(responses[i]))
            remove_dup.clear()
        merged = [item for row in responses for item in row]
        c = Counter(merged)
        Max = 0
        freq = ""
        for key, value in c.items():
            if value == Max:
                freq = min(freq, key)
            if value > Max:
                Max = value
                freq = key
            
        return freq

        # print(merged)
        

        # i = 0
        # for response in responses[i]:
        #     # responses[i]=
        #     remove_dup.add(response)
        #     response = list(remove_dup)
        #     remove_dup.clear()
        #     if i < len(responses):
        #         i+=1
        #     print(responses)

        
        