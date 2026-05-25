k, n, w = map(int, input().split())


res = k * (w*(w+1))//2

print(max(0, res-n))