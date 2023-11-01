#Перед вами стоит задача создать программу для исследования семейного архива, который представлен в виде списка кортежей. Каждый кортеж представляет информацию о членах семьи, включая имя, возраст и место рождения. Ваша цель - создать функцию для поиска членов семьи, удовлетворяющих определенным условиям.

def explore_family_archive(family_data, min_age, birthplace):
    matching_members = []
    for member in family_data:
        name, age, place_of_birth = member
        if age >= min_age and place_of_birth == birthplace:
            matching_members.append(name)
    
    return matching_members


family_data = [
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 40, "Chicago"),
    ("David", 28, "New York"),
    ("Eve", 35, "Chicago"),
]

min_age = 30
birthplace = "New York"

result = explore_family_archive(family_data, min_age, birthplace)
print("Соответствующие члены семьи:", result)
