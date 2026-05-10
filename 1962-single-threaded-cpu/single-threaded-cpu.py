class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        res = []
        cpuidl = []
        task_idx = 0
        time = 0
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()

        while task_idx < n or cpuidl:
            if not cpuidl:
                time = max(time, tasks[task_idx][0])
            while task_idx < n and tasks[task_idx][0] <= time:
                heapq.heappush(cpuidl, [tasks[task_idx][1], tasks[task_idx][2]])            
                task_idx += 1
            process_time, idx = heapq.heappop(cpuidl)
            res.append(idx)
            time += process_time
        return res

        