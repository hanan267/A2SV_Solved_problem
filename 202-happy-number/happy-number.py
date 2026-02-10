class Solution:
    def isHappy(self, n: int) -> bool:
        # change to string check the length
            # if len 1 check not
            # else
                # suare each idx
                # convert to int and add
                # convert to string and check
        # seen = set() 
        
        
        
        # if n == 1:
        #     return True
        # n_string = str(n)
        
        # while n_string != "1" and (n_string not in seen):
        #     Sum = 0
        #     for char in n_string:
        #         square = int(char) ** 2
        #         Sum += square
            
        #     seen.add(n_string)
        #     n_string = str(Sum)
            


        # return n_string == "1"
      
       
      
      # create a set to track added numbers
      # add square of each numbers till the number is 0
      # do that until n is not 1

      seen = set()

      while n != 1:
        if n in seen:
            return False
        seen.add(n)
        Sum = 0
        while n > 0:
            digit = n % 10
            Sum += digit**2
            n //= 10

        n = Sum
      return True






















