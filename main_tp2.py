from file_reader import FileReader
from heuristics import Heuristic
import os 
import re


def main():
    #get libs
    libs = [file for file in os.listdir('.') if re.match(r'Lib_', file)]
    libs.sort()
    
    for lib in libs:
        #get problems
        problems = [problem for problem in os.listdir(f'./{lib}/') if re.match(r'p', problem)]
        problems.sort()
        result=""
        allresults=""
        count=1
        for problem in problems:

            #open problem file
            with open(f'./{lib}/{problem}')as f:
            
                data= f.read()
                #process problem file
                file = FileReader(data,problem)
                #solve the problem
                facilities=Heuristic.sort_facilties_by_openingcost(file)
                facilities_with_clients1=Heuristic.assing_clients_to_facilties(facilities,file)
                result=Heuristic.solution(facilities_with_clients1,file)
                allresults=f'{allresults}{str(result)}\n'
                print(f'{count}:{result}')
            count+=1
        #write the solution
        with open(f'./{lib}/results_tp2_v2.txt','w') as f:
            f.write(str(allresults))
    
            
if __name__ == "__main__":
    main()