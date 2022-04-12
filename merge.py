def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'x': 10, 'y':19}
dict2 = {'a': 34, 'b':45}
print(Merge(dict1, dict2))
print(dict2)