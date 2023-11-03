with open('molodoy_white.txt', '+a') as f:
    f.write('\nI SAY')

with open ('molodoy_white.txt', 'r') as f:
    result = f.readlines()
    print(result)