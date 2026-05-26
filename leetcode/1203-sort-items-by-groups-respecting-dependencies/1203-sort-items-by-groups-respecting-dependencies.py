class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        item_graph = defaultdict(list)
        item_indeg = [0] * n
        group_graph = defaultdict(list)
        group_indeg = [0] * group_id
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indeg[v] += 1
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indeg[group[v]] += 1
        def topo_sort(graph, indeg, size):
            q = deque([i for i in range(size) if indeg[i] == 0])
            res = []
            while q:
                node = q.popleft()
                res.append(node)
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return res if len(res) == size else []
        group_order = topo_sort(group_graph, group_indeg, group_id)
        if not group_order:
            return []
        item_order = topo_sort(item_graph, item_indeg, n)
        if not item_order:
            return []
        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)
        result = []
        for g in group_order:
            result.extend(grouped_items[g])
        return result