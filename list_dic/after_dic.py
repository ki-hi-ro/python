# === After ===
data_list = [
    {"id": 1, "name": "a"},
    {"id": 2, "name": "b"}
]

# idとnameをまとめて処理
for item in data_list:
    print(f"id: {item['id']}, name: {item['name']}")

# nameだけ取り出す
for item in data_list:
    print(item["name"])

# idをキーに高速アクセスしたい場合は辞書の辞書も可
data_dict = {item["id"]: {"name": item["name"]} for item in data_list}
print(data_dict[1]["name"])  # → "a"