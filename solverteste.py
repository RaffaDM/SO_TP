import os 
from file_reader import FileReader
from ortools.linear_solver import pywraplp



entries = os.listdir('Lib_1')
entries.remove('os')
DEFAULT_TIME=60000

# Create SCIP Solver
solver = pywraplp.Solver.CreateSolver('SCIP')


with open(f'Lib_1/p1', 'r') as f:
        data = f.read()
        file= FileReader(data,'p1')


# i facilities
# j clients

y = {}
x = {}
for i in range(file.get_i()):
     y[i] = solver.IntVar(0,1,f'y[{i}]')
     

for i in range(file.get_i()):
     for j in range(file.get_j()):
        x[j, i] = solver.IntVar(0,1,f'x[{j},{i}]')

for j in range(file.get_j()):
     solver.Add(solver.Sum([x[j,i] for i in range(file.get_i())])==1)

for i in range(file.get_i()):
     solver.Add(solver.Sum([x[j,i] * file.get_d()[j] for j in range (file.get_j())]) <= file.get_s()[i]*y[i])

objective = [sum(file.get_f()[i] * y[i] for i in range(file.get_i())),
             sum(file.get_c()[j][i] * x[j,i] for i in range(file.get_i()) for j in range(file.get_j()))]

solver.Minimize(solver.Sum(objective))

#solver.SetTimeLimit(DEFAULT_TIME)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
     final_result=f"Objective value ={solver.Objective().Value()}"
     print(final_result)
      
else:
     print("The problem does not have an optimal solution.")

print("\nAdvanced usage:")
print("Problem solved in %f milliseconds" % solver.wall_time())
print("Problem solved in %d iterations" % solver.iterations())
print("Problem solved in %d branch-and-bound nodes" % solver.nodes())


with open("a.mps", "w") as out_f:
     mps_text = solver.ExportModelAsLpFormat(False)
     out_f.write(mps_text)
