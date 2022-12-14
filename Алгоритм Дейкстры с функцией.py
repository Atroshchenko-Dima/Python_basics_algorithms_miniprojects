graph = {} # сначала необходимо реализовать граф, создаем хеш таблицу

graph["start"] = {} # для того чтобы узнать веса ребер создаем еще одну хеш таблицу
graph["start"]["a"] = 6 # вес ребра "а"
graph["start"]["b"] = 2

graph["a"] = {} # включаем в граф остальные узлы и их соседей
graph["a"]["fin"] = 1 #  расстояние от а до конечного узла
graph["b"] = {}
graph["b"]["a"] = 3 #  расстояние от "б" до "а"
graph["b"]["fin"] = 5
graph["fin"] = {}  # у конечного узла нет соседей

infinity = float("inf") # т.к мы не знаем сколько времени потребуется для достижения конечного узла 
# стоимость считается бесконечной
costs = {}  #  хеш таблица для хранения стоимостей всех узлов
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {} # создаем хеш таблицу для родителей
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

processed = [] # создаем массив для отслеживания всех уже обратонных узлов, один узел не должен 
# обрабатываться многократно

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    # Пройти через каждый узел
    for node in costs:
        cost = costs[node]

        # Если это самая низкая стоимость и до сих пор и еще не была обработана ...
        if cost < lowest_cost and node not in processed:
            # установить его как новый самый дешевый узел.
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

# Найти самый дешевый узел, который вы еще не обработали.
node = find_lowest_cost_node(costs)

# Если вы обработали все узлы, то этот цикл while завершен.
while node is not None:
    cost = costs[node]

    # Пройдите через всех соседей этого узла
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]

        # Если дешевле добраться до этого соседа, пройдя через этот узел ...
        if costs[n] > new_cost:
            # обновить стоимость для этого узла
            costs[n] = new_cost
            # Этот узел становится новым родителем для этого соседа.
            parents[n] = node
    
    # Отметить узел как обработанный.
    processed.append(node)
    # Найти следующий узел для обработки и выполните цикл.
    node = find_lowest_cost_node(costs)

print('Стоимость от начала до каждого узла:')
print(costs)