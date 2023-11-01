def find_string_indices(input_list):
    indices = [str(i) for i, item in enumerate(input_list) if isinstance(item, str)]
    return ''.join(indices)

input_list = ['Ramu', 98, 'Chamu', 'Manoj', 'Tarun', 78, 90, "Jamun"]
output = find_string_indices(input_list)
print(output)
