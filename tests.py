import os 
import re
from file_reader import FileReader
from ortools.linear_solver import pywraplp

entries = os.listdir('Lib_1')
entries.remove('os')
DEFAULT_TIME=120000
# Create glop Solver
solver = pywraplp.Solver.CreateSolver('GLOP')

libs = [file for file in os.listdir('.') if re.match(r'.*.txt$', file)]
print(libs)
for lib in libs:
    with open(f'./{lib}', 'r') as f:
        data = f.read()
        
        #print(file.get_matrix())
#print(file.get_i())
#print(file.get_j())
#for i in range(file.get_i()):
#    for j in range(file.get_j()):
#        print(file.get_constraint_coeffs()[i][j])