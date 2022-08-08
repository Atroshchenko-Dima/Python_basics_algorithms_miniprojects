states_needed = set(["mt","wa","or","id","nv","ut","ca","az",]) # Переданный массив преобразуется в множество
stations = {} # список станций из которого будет выбираться покрытие, создаем хеш
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfor"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set() # создаем структуру данных для хранения итогового набора станций

while states_needed: # цикл продолжается пока множество states_needed не станет пустым
    best_station = None # перебираем все станции и выбираем ту, которая обслуживает больше всего штатов
    states_covered = set() # содержит все штаты обслуживаемые этой станцией
    
    for station, states in stations.items():
        covered = states_needed & states # содержит штаты присутсвующие как в states_nedeed так и в states_for_station
        
        if len(covered) > len(states_covered): # проверяем покрывает ли эта станция штатов больше чем текущая станция
            best_station = station
            states_covered = covered

final_stations.add(best_station) # после завершения цикла лучшая станция добавляется в итоговый список станций
states_needed -= states_covered # те штаты которые покрывает станция больше не нужны
print(final_stations)