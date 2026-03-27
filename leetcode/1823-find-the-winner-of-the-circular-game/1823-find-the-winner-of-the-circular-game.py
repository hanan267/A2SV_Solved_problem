class Solution:
    def findTheWinner(self, n: int, k: int) -> int:


        # q = deque()

        # for i in range(1, n+1):
        #     q.append(i)

        # while len(q) > 1:
        #     for i in range(k-1):
        #         q.append(q.popleft())
        #     q.popleft()
        # return q[0]

        # def helper(n, k):
        #     if n == 1:
        #         return 0
        #     return (helper(n-1, k) + k) % n
        # return helper(n, k) + 1
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        print(arr)

        def kthNum(idx,arr):
            if len(arr) == 1:
                return arr[0]
            turn = (idx + k-1)%len(arr)
            arr.pop(turn%len(arr))
            return kthNum(turn, arr)
        return kthNum(0, arr)
        