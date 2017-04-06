import os

print('Catalog: ')
catalog = input()
listdir = os.walk(catalog)
print(listdir)
