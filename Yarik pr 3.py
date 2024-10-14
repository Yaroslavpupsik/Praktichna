def remove_duplicates_and_sort(input_list):
    unique_list = list(set(input_list))

    numbers = [x for x in unique_list if isinstance(x, (int, float))]
    strings = [x for x in unique_list if isinstance(x, str)]

    numbers.sort(reverse=True)

    strings.sort()

    return numbers + strings

input_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Hello']
result = remove_duplicates_and_sort(input_list)
print(result)
