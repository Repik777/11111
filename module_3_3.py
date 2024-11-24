def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 1, b = 25, c = [1,2,3])

def print_params(*values_list, **values_dict):
    print(values_list)
    for key, value in values_dict.items():
        print(key, value)


values_list = ['easy', False, 300]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list, **values_dict)

values_list_2 = [100, 1.2]
print_params(*values_list_2, 42)