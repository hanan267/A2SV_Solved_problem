class Solution:
    def diffWaysToCompute(self, expression: str):
        memo = {}
        def solve(expr):
            if expr in memo:
                return memo[expr]
            result = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])

                    for l in left:
                        for r in right:
                            if char == "+":
                                result.append(l + r)
                            elif char == "-":
                                result.append(l - r)
                            else:
                                result.append(l * r)
            if not result:
                result.append(int(expr))

            memo[expr] = result
            return result
        return solve(expression)