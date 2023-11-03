
import os

def print_docs (directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Пanka {catalog[0]} содержит:')
    print (f'Диpekтоpии: {", ".join([folder for folder in catalog [1]])}') 
    print(f'aйлы: {", ".join([file for file in catalog[2]])}') 
    print('-'* 40)
    
print_docs('C:\ProjectWorkProgram\GAME\Wolf')