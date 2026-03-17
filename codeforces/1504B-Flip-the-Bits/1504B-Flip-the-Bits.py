from collections import Counter
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input())) 
  b = list(map(int, input()))

  pref = [0]*n
  zero = one = 0
  for i in range(n):
    if a[i] == 0:
      zero += 1
    else:
      one += 1
    if zero == one:
      pref[i] = 1
  flipped = False
  possible = True
  for i in range(n-1, -1, -1):
    curr = a[i]
    if flipped:
      curr = 1- curr
    if curr == b[i]:
      continue
    
    if pref[i] == 1:
      flipped = not flipped
    else:
      possible = False
      break
  print("YES" if possible else "NO")