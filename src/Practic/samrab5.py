values = [0, 2, 4, 6, 8, 10]
memory = ' world'
string = 'hello'
counter = 0

if counter in values:
    counter = 10

string = memory
string = 'world'

if counter > 7:
    print(string + memory)
print(string)

while counter != 10:
    if counter < 10:
        counter += 1
    print(memory)
memory = string