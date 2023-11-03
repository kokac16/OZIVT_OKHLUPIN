lines = ['one', 'two', 'three']
with open('molodoy_white.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')