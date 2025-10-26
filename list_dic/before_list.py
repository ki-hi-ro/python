# === Before ===
id_list = [1, 2]
name_list = ["a", "b"]

# idだけ処理
for id_val in id_list:
    print(f"id: {id_val}")

# nameだけ処理
for name_val in name_list:
    print(f"name: {name_val}")

# idとnameを一緒に使いたいとき（zipで頑張る必要あり）
for id_val, name_val in zip(id_list, name_list):
    print(f"id: {id_val}, name: {name_val}")