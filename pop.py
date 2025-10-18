sample_list = [1, 2, 3, 4, 5]

# 何も指定しない場合、最後の要素が削除される
popped_element = sample_list.pop()
print("Popped element:", popped_element)
print("List after popping the last element:", sample_list)

# インデックスを指定して要素を削除
popped_element_at_index = sample_list.pop(1)
print("Popped element at index 1:", popped_element_at_index)
print("List after popping element at index 1:", sample_list)