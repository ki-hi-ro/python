from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])  # キューに「経路のリスト」を入れる
    visited = set()           # 訪問済みノード

    while queue:
        path = queue.popleft()  # 現在の経路
        node = path[-1]         # 現在のノード

        if node == goal:
            return path  # 最短経路が見つかった！

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]  # 新しい経路を作成
                queue.append(new_path)

    return None  # 経路が見つからなかった場合

# 元データ
data = [
    {'node1': 1000, 'node2': 1050, 'direction': 1, 'load': 1, 'unload': 0},
    {'node1': 1050, 'node2': 1200, 'direction': 2, 'load': 1, 'unload': 0},
    {'node1': 1200, 'node2': 1250, 'direction': 1, 'load': 0, 'unload': 1},
    {'node1': 1250, 'node2': 1300, 'direction': 1, 'load': 1, 'unload': 0},
    {'node1': 1100, 'node2': 1000, 'direction': 1, 'load': 0, 'unload': 1},
    {'node1': 1100, 'node2': 1250, 'direction': 1, 'load': 1, 'unload': 0},
]

# 元データからgraph作成
def build_graph(data):
    graph = {}

    for edge in data:
        n1, n2, d, l, ul = edge['node1'], edge['node2'], edge['direction'], edge['load'], edge['unload']

        
        if d == 1:  # 片方向
            graph.setdefault(n1, []).append(n2)
            graph.setdefault(n2, [])  # 孤立ノードも確保しておく
        elif d == 2:  # 両方向
            graph.setdefault(n1, []).append(n2)
            graph.setdefault(n2, []).append(n1)
        # 無方向 (d == 0) は無視

    return graph

graph = build_graph(data)
from pprint import pprint
pprint(graph)

start_node = 1000
goal_node = 1200
shortest_path = bfs_shortest_path(graph, start_node, goal_node)

print("最短経路:", shortest_path)