from decimal import Decimal 
class FileReader:
    def __init__(self,file,name):
        file=file.split('\n')
        n=0

        for rows in file:
            file[n]=rows.split(' ')
            n+=1
        for x in range(len(file)):
                if('' in file[x]):
                    file[x].remove('')
        for x in range(len(file)):   
            for i in range(len(file[x])):
                file[x][i]= float(file[x][i])
        for x in range(len(file)):   
            for i in range(len(file[x])):
                file[x][i]= int(file[x][i])
        self.name=name
        self.facilities=file[0][0]
        self.customers=file[0][1]
        self.facilities_capacity=file[1]
        self.facilities_opening_cost=file[2]#max 10
        self.customers_demand= file[3]#max 20
        self.matrix=file[4:]
    
   
    
    def get_name(self):
        return self.name
    # Get  facilities
    def get_i(self):
        return self.facilities
    # Get  customers
    def get_j(self):
        return self.customers
    #Get capacity
    def get_s(self):
        return self.facilities_capacity
    #Get demand
    def get_d(self):
        return self.customers_demand
    #Get  Fixed opening cost
    def get_f(self):
        return self.facilities_opening_cost
    #Get assignment cost
    def get_c(self):
        return self.matrix