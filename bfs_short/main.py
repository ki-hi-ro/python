from graph_module import Graph

data = [
    {'node1': 1000, 'node2': 1050, 'direction': 1, 'load': 1, 'unload': 0},
    {'node1': 1050, 'node2': 1200, 'direction': 2, 'load': 1, 'unload': 0},
    {'node1': 1200, 'node2': 1250, 'direction': 1, 'load': 0, 'unload': 1},
    {'node1': 1250, 'node2': 1300, 'direction': 1, 'load': 1, 'unload': 0},
    {'node1': 1100, 'node2': 1000, 'direction': 1, 'load': 0, 'unload': 1},
    {'node1': 1100, 'node2': 1250, 'direction': 1, 'load': 1, 'unload': 0},
]

g = Graph(data)

print("🔹 グラフ構造:")
g.show_graph()

start_node = 1000
goal_node = 1200

print(f"\n🚩 最短経路（{start_node} → {goal_node}）:")
path = g.bfs_shortest_path(start_node, goal_node)
print(path)