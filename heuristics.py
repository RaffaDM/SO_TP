from file_reader import FileReader

class Heuristic:

    def sort_facilties_by_openingcost(file:FileReader):
        facilities={}
        for n_facility in range(int(file.get_i())):
            facilities[n_facility]=file.get_f()[n_facility]
        sorted_facilities_by_cost=dict(sorted(facilities.items(), key=lambda item: item[1]))
        return sorted_facilities_by_cost

    def assing_clients_to_facilties(sorted_facilities_by_cost,file:FileReader):
        clients_used=[]
        facilities_with_clients={}
        for n_facility in sorted_facilities_by_cost.keys():
            clients={}
            file.get_s()[n_facility]
            for n_client in range(int(file.get_j())):
                clients[n_client]=file.get_c()[n_client][n_facility]
            sorted_clients_by_cost=dict(sorted(clients.items(), key=lambda item: item[1]))
            total_demand=0
            for n_client in sorted_clients_by_cost:
                if not n_client in clients_used:
                    if not n_facility in facilities_with_clients.keys():
                        facilities_with_clients[n_facility]=[]
                    if file.get_d()[n_client]+total_demand<=file.get_s()[n_facility]:
                        facilities_with_clients[n_facility].append(n_client)
                        clients_used.append(n_client)
                        total_demand=file.get_d()[n_client]+total_demand
                    else:
                        break
        return facilities_with_clients
    
    def sort_facilties_by_openingcost_v2(file:FileReader):
        facilities={}
        for n_facility in range(int(file.get_i())):
            facilities[n_facility]=file.get_f()[n_facility]/file.get_s()[n_facility]
        sorted_facilities_by_cost=dict(sorted(facilities.items(), key=lambda item: item[1]))
        return sorted_facilities_by_cost
    
    def assing_clients_to_facilties_v2(sorted_facilities_by_cost,file:FileReader):
        clients_used=[]
        facilities_with_clients={}
        for n_facility in sorted_facilities_by_cost.keys():
            clients={}
            file.get_s()[n_facility]
            for n_client in range(int(file.get_j())):
                clients[n_client]=file.get_c()[n_client][n_facility]/file.get_d()[n_client]
            sorted_clients_by_cost=dict(sorted(clients.items(), key=lambda item: item[1]))
            total_demand=0
            for n_client in sorted_clients_by_cost:
                if not n_client in clients_used:
                    if not n_facility in facilities_with_clients.keys():
                        facilities_with_clients[n_facility]=[]
                    if file.get_d()[n_client]+total_demand<=file.get_s()[n_facility]:
                        facilities_with_clients[n_facility].append(n_client)
                        clients_used.append(n_client)
                        total_demand=file.get_d()[n_client]+total_demand
                    else:
                        break
        return facilities_with_clients

    def solution(facilities_with_clients,file:FileReader):
        custo_total= 0
        for n_facility in facilities_with_clients:
            custo_total=file.get_f()[n_facility]+custo_total
            for n_client in facilities_with_clients[n_facility]:
                custo_total=file.get_c()[n_client][n_facility]+custo_total
        return custo_total