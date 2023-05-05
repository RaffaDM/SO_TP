import os 
from file_reader import FileReader
from ortools.linear_solver import pywraplp

entries = os.listdir('Lib_1')
entries.remove('os')
DEFAULT_TIME=120000
# Create glop Solver
solver = pywraplp.Solver.CreateSolver('GLOP')


with open(f'Lib_1/p1', 'r') as f:
        data = f.read()
        file= FileReader(data,'p1')
        #print(file.get_matrix())
print(file.get_i())
print(file.get_j())
for i in range(file.get_i()):
    for j in range(file.get_j()):
        print(file.get_constraint_coeffs()[i][j])