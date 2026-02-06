class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path = defaultdict(list)

        for path in paths: # ["root/a 1.txt(abcd) 2.txt(efgh)"
            path = path.split() # ["root/a", "1.txt(abcd)"," 2.txt(efgh)"]
            for i in range(1, len(path)): # ["1.txt(abcd)"," 2.txt(efgh)"]
                file_path = path[i].split("(")[0]  # ["1.txt"]
                content = re.findall(r"\((.*?)\)", path[i])[0] #["abcd"]
                # if content not in content_path:
                #     content_path[content] = []
                content_path[content].append(path[0] + "/" + file_path)
                # else:
                #     content_path[content].append(path[0] + "/" + file_path)
        # print(content_path)
        res = []
        for value in content_path.values():
            if len(value) > 1:
                res.append(value)
        return res





        