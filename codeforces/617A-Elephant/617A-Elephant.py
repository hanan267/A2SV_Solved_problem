def minStep(x):
  step = x // 5
  if x % 5 == 0:
    return step
  else:
    return step + 1
 

print(minStep(x))