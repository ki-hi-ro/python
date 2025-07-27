from collections import deque
from typing import List, Dict, Optional


class Graph:
    def __init__(self, data: List[Dict]):
        """初期化時にグラフを構築する"""
        self.graph = self._build_graph(data)

    def _build_graph(self, data: List[Dict]) -> Dict[int, List[int]]:
        """元データからグラフを構築する"""
        graph = {}
        for edge in data:
            n1, n2 = edge['node1'], edge['node2']
            direction = edge['direction']

            if direction == 1:  # 片方向
                graph.setdefault(n1, []).append(n2)
                graph.setdefault(n2, [])  # 孤立ノードも確保
            elif direction == 2:  # 双方向
                graph.setdefault(n1, []).append(n2)
                graph.setdefault(n2, []).append(n1)
        return graph

    def bfs_shortest_path(self, start: int, goal: int) -> Optional[List[int]]:
        """幅優先探索で最短経路を返す"""
        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    queue.append(path + [neighbor])
        return None

    def show_graph(self):
        """内部のグラフ構造を出力する"""
        from pprint import pprint
        pprint(self.graph)