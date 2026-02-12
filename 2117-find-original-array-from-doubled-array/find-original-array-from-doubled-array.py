class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # n = len(changed)
        # if n % 2 != 0:
        #     return []
      
        # half = n//2
        # # changed = sorted(changed)
        
        # sub1 = sorted(changed[0:half])
        
        # sub2 = sorted(changed[half:n])
        # print(sub1, sub2)
        # original = sub1
        # doubled = sub2
        # if sub1[0] > sub2[0]:
        #     original = sub2
        #     doubled = sub1
        # doubled = {value for key, value in enumerate(doubled)}
        # for num in original:
        #     if num*2 not in doubled:
        #         return []
        # return original














        n = len(changed)
       
      
        
        changed = sorted(changed)
        count = Counter(changed)
      
        res = []
      
        for num in changed:
            if count[num] <= 0:

                continue

            count[num] -=1

            if count[num*2] >= 1:
                count[num*2] -=1
                res.append(num)
            else:
                return []

        return res

            # if num == 0:
            #     if num in changed and  c[num] % 2 == 0:
            #         res.append(num)
            #         half -= 1
            #         if c[num*2] > 1:
                    
            #             c[num*2] = c[num*2] -1
            #         else:
            #             del c[num*2]
            # continue
            # if num*2 in c and half > 0 and num in c:
            #     res.append(num)
            #     half -= 1
            #     if c[num*2] > 1:
                   
            #         c[num*2] = c[num*2] -1
            #     else:
            #         del c[num*2]
            # else:
            #     return []
        
            




      
        
        























        
        # n = len(changed)
        # half = n//2
       
        # doubled_hash = {}
        # for idx,num in enumerate(changed[half:]):
        #     doubled_hash[num] = idx
        # print(doubled_hash)
        # original = []
        # for i in range(0,half):
        #     # print(changed[i])
        #     # print(changed[i]*2,changed[i+half],changed[i]//2)

        #     if changed[i]*2 in doubled_hash:
        #         original.append(changed[i])
        #         del doubled_hash[changed[i]]
        #     if changed[i]/2 in doubled_hash:
        #         original.append(changed[i]/2)
        #         del doubled_hash[changed[i]/2]
                
        #         # print(min(changed[i], changed[half+i]))
        #         # original.append(min(changed[i], changed[half+i]))
        # # print(len(original), half)
        # if len(original) == half:
        #     return original
        # else:
        #     return []
        
        # # half = len(changed)//2
        # # original
        # # if changed[0] < changed[half]:
        # #     original = changed[0:half]
        # # doubled = changed[half:]
        # # hash_map = {}
        # # for value in original:
        # #     value *= 2
        # # print(original)
        # # for idx,value in enumerate(doubled):
        # #     hash_map[value] = idx
       
         
                


        