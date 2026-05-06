def sort(list):
  if len(list) == 1:
    return list, 0
  
  mid = len(list)//2
  left_arr, right_arr = list[:mid], list[mid:]
  left, lo = sort(left_arr)
  right, ro = sort(right_arr)

  if left is None or right is None:
    return None, 0
  if max(left) < min(right):
    return left + right, lo + ro
  elif max(right) < min(left):
    return right + left, lo + ro + 1
  else:
    return None, 0
  

for _ in range(t):
  m = int(input())
  p = list(map(int, input().split()))

  res, opr = sort(p)
  if res is None:
    print(-1)
  else:
    print(opr)