def personal_info(name, age, company=' unnamed'):
    print(f"Иmя: {name} Boзpacт: {age} Koмпaния: {company}")
tom = ("Григорий", 22) 
personal_info(*tom)
bob = ("гeopгий", 41, "Yandex") 
personal_info(*bob)