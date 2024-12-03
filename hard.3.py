data_structure = [[1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data):
    total = 0
    if isinstance(data, int):
            return data
    if isinstance(data, str):
            return len(data)
    if isinstance(data, dict):
        data = list(data.items())
    for i in data:
        total += + calculate_structure_sum(i)
    return total

result = calculate_structure_sum(data_structure)
print(result)




