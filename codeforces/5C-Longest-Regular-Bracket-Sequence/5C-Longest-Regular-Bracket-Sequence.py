# brackets = input()

# stack = []
# subString = 0
# maxSubString = 0
# count = []

# for idx, bracket in enumerate(brackets):
#   if bracket == "(":
#     stack.append("(")
#   elif bracket == ")" and stack:
#      if stack[-1] == "(":
#        stack.pop()
#        subString += 2
#   else:
#     maxSubString = max(maxSubString, subString)
#     count.append(maxSubString)
#     # print(maxSubString, subString, brackets[0:idx])
   
#     subString = 0
  
# print("0 1" if maxSubString == 0 else (str(maxSubString) + " " + str(count.count(maxSubString)+1)))

  
brackets = input()

stack = [-1]  
max_len = 0
count = 0

for i, ch in enumerate(brackets):
    if ch == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

if max_len == 0:
    print("0 1")
else:
    print(max_len, count)