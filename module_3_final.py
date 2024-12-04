data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}), "Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

def cal_struct_sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            total_sum += cal_struct_sum(*arg)
        elif isinstance(arg, dict):
            for key, value in arg.items():
                total_sum += cal_struct_sum(key, value)
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif arg is None:
            pass
    return total_sum
print(cal_struct_sum(data_structure))