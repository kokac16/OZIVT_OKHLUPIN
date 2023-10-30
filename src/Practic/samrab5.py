def generate_sets(input_list):
    result_dict = {}
    for num in input_list:
        if input_list.count(num) > 1:
            if num not in result_dict:
                result_dict[num] = {str(num)}
            result_dict[num].add(str(num) * input_list.count(num))
        else:
            result_dict[num] = {num}
    result_set = set()
    for values in result_dict.values():
        result_set.update(values)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

result_1 = generate_sets(list_1)
result_2 = generate_sets(list_2)
result_3 = generate_sets(list_3)

print(result_1)
print(result_2)
print(result_3)