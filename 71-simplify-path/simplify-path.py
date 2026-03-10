class Solution:
    def simplifyPath(self, path: str) -> str:
        
        pathlist = path.split("/")
        # print(pathlist)
        stack = []
        for path in pathlist:
            if path == "" or path == ".":
                continue
            elif path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return "/"+"/".join(stack)
     