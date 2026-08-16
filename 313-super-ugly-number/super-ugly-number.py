class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        

        ugly = [1]
        indexes = [0]*len(primes)
        while len(ugly)<n:
                values = []
                
                for i in range(len(primes)):
                    # print(primes[i])
                    values.append(primes[i] * ugly[indexes[i]])
                next = min(values)
                ugly.append(next)
                for i in range(len(primes)):
                    if values[i] == next:
                        indexes[i] += 1
            
        return ugly[-1]