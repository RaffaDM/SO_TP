import os 
from file_reader import FileReader
from ortools.linear_solver import pywraplp

DEFAULT_TIME=60000
class SolverResolve:
     

     def resolve_problem(self,file):
          solver = pywraplp.Solver.CreateSolver('SCIP')
          #i=facilities,j=clients,s=capacity,d=demand,f=Fixed opening cost,c=assignment cost
          y = {}
          x = {}
          #Set Y
          for i in range(file.get_i()):
               y[i] = solver.IntVar(0,1,f'y[{i}]')
          #Set X 
          for i in range(file.get_i()):
               for j in range(file.get_j()):
                    x[j, i] = solver.IntVar(0,1,f'x[{j},{i}]')
          #Set Contrains
          for j in range(file.get_j()):
               solver.Add(solver.Sum([x[j,i] for i in range(file.get_i())])==1)

          for i in range(file.get_i()):
               solver.Add(solver.Sum([x[j,i] * file.get_d()[j] for j in range (file.get_j())]) <= file.get_s()[i]*y[i])
          #Set Objective
          objective = [sum(file.get_f()[i] * y[i] for i in range(file.get_i())),
                    sum(file.get_c()[j][i] * x[j,i] for i in range(file.get_i()) for j in range(file.get_j()))]
          solver.Minimize(solver.Sum(objective))
          #Solver with timer
          solver.SetTimeLimit(DEFAULT_TIME)
          status = solver.Solve()

          #Export Solver Model
          with open("a.mps", "w") as out_f:
               mps_text = solver.ExportModelAsLpFormat(False)
               out_f.write(mps_text)
          #Final Result
          if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
               final_result=f"\nObjective value ={solver.Objective().Value()}"
          else:
               final_result=f"\nThe problem does not have an optimal solution."
          final_result+="\nAdvanced usage:"
          final_result+="\nProblem solved in %f milliseconds" % solver.wall_time()
          final_result+="\nProblem solved in %d iterations" % solver.iterations()
          final_result+="\nProblem solved in %d branch-and-bound nodes" % solver.nodes()
          return final_result 

          



