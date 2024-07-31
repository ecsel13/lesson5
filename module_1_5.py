immutable_var = 1, 'cherry', 3, 45, True
print(immutable_var)
# immutable_var[0] = 200 сам объект кортежа не изменяем, изменение могут происходить только внутри объекта
mutable_list = ['apple', 'cherry', 2, 34, False]
print(mutable_list)
mutable_list.append(1)
print(mutable_list)
mutable_list.remove('apple')
print(mutable_list)
