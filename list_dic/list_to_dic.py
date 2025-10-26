id_list = [1, 2]
name_list = ["a", "b"]

data_list = [{"id": id_val, "name": name_val} for id_val, name_val in zip(id_list, name_list)]
print(data_list)
# → [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
