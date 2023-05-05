import os 
from file_reader import FileReader
from ortools.linear_solver import pywraplp
from ortools.constraint_solver import pywrapcp


entries = os.listdir('Lib_1')
entries.remove('os')
DEFAULT_TIME=120000

# Create SCIP Solver
solver = pywraplp.Solver.CreateSolver('SCIP')


with open(f'Lib_1/p1', 'r') as f:
        data = f.read()
        file= FileReader(data,'p1')


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
     for j in range(file.get_j()):
          solver.Add(solver.Sum([x[j,i] * file.get_demand()[j]]) <= file.get_capacity()[i]*y[i])


print(file.get_opening_cost()[i] )
objective = []

objective.append(sum(file.get_opening_cost()[i] * y[i] for i in range(file.get_i())))
objective.append(sum(file.get_constraint_coeffs()[j][i] * x[j,i] for i in range(file.get_i()) for j in range(file.get_j())))

solver.Minimize(solver.Sum(objective))

#solver.SetTimeLimit(DEFAULT_TIME)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
     print("Objective value =", solver.Objective().Value())
for i in range(file.get_i()):
     for j in range(file.get_j()):
          print(f"Customer {j} assigned to facility {j}")
          #print("x =", x.solution_value())
          #print("y =", y.solution_value())
          #print(f"Cost {file.get_constraint_coeffs[i][j]}")
     
else:
     print("The problem does not have an optimal solution.")
print("Problem solved in %f milliseconds" % solver.wall_time())
print("Problem solved in %d iterations" % solver.iterations())
print("Problem solved in %d branch-and-bound nodes" % solver.nodes())