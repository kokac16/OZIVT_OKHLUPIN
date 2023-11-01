def find_employee_entries(data, employee_id):
    if employee_id not in data:

        return ()
    
    first_occurrence = data.index(employee_id)
    if data.count(employee_id) == 1:
        return data[first_occurrence:]
    
    second_occurrence = data.index(employee_id, first_occurrence + 1)
    return data[first_occurrence:second_occurrence + 1]

tuple1 = (1, 2, 3)
element1 = 8
result1 = find_employee_entries(tuple1, element1)
print(result1)  

tuple2 = (1, 8, 3, 4, 8, 8, 9, 2)
element2 = 8
result2 = find_employee_entries(tuple2, element2)
print(result2)  

tuple3 = (1, 2, 8, 5, 1, 2, 9)
element3 = 8
result3 = find_employee_entries(tuple3, element3)
print(result3)  
