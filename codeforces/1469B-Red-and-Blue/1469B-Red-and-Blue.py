# compute maximum sum of a and b
  # reurn their sum
  def prefixSum(arr):
    total = 0
    res = [0]
    for i in range(len(arr)):
      total += arr[i]
      res.append(total)
    return res
  max_a = max(prefixSum(a))
  max_b = max(prefixSum(b))

  print(max_b+max_a)