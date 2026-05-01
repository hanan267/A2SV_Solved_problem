def pickStone(n, s):
  count = 0
  i, j = 0, 1
  if n == 1:
    return 0
  else:
   for i in range(n - 1):
    if s[i] == s[i + 1]:
        count += 1
  return count

print(pickStone(n, s))