import os 
from file_reader import FileReader

entries = os.listdir('Lib_1')
entries.remove('os')

for entry in entries:
    with open(f'Lib_1/{entry}', 'r') as f:
        data = f.read()
        file= FileReader(data,entry)
        


