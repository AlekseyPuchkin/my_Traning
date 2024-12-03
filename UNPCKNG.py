def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, b=25)
print_params(b=25, c=[1, 2, 3])
values_list = [3.14, 'строка', False]
values_dict = {'a': 42,'b': 'строка','c': 7.5}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)