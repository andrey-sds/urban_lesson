def calculate_structure_sum(*data):
    total_sum = 0
    total_length = 0
    total_ = 0

    def process(element):
        nonlocal total_sum, total_length
        if isinstance(element, int) or isinstance(element, float):
            total_sum += element
        elif isinstance(element, str):
            total_length += len(element)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                process(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process(key)
                process(value)

    process(data)
    total_ = total_sum + total_length
    return total_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(f'Сумма всех чисел и длин всех строк = {result}')
