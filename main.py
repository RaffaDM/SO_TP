import os 
import re
from file_reader import FileReader
from solver_resolve import SolverResolve

def main():
    #get libs
    libs = [file for file in os.listdir('.') if re.match(r'Lib_5_', file)]
    libs.sort()
    
    for lib in libs:
        #get problems
        problems = [problem for problem in os.listdir(f'./{lib}/') if re.match(r'p', problem)]
        problems.sort()
        result=""
        for problem in problems:
            #open problem file
            with open(f'./{lib}/{problem}')as f:
                data= f.read()
                #process problem file
                file = FileReader(data,problem)
                #solve the problem
                result+=f'\n{problem}:{SolverResolve().resolve_problem(file)}'
                print(result)
        #write the solution
        with open(f'./{lib}_results.txt','w') as f:
            f.write(result)
if __name__ == "__main__":
    main()