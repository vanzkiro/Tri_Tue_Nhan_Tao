def breadth_first_search(graph, start_node, goal_node):
    # 1. Khởi tạo danh sách L chỉ chứa trạng thái ban đầu
    L = [start_node]
    father = {}
    
    print(" TÌM KIẾM THEO CHIỀU RỘNG (BFS) ")
    stt = 1
    
    # 2. loop do
    while True:
        # 2.1. if L rỗng then {thông báo tìm kiếm thất bại; stop}
        if not L:
            print("Thông báo: Tìm kiếm thất bại!")
            return None
        
        # 2.2. Loại trạng thái u ở đầu danh sách L
        u = L.pop(0)
        print(f"Bước {stt}: u = {u} | L còn lại = {L}")
        stt += 1
        
        # 2.3. if u là trạng thái kết thúc then {thông báo tìm kiếm thành công; stop}
        if u == goal_node:
            print("Thông báo: Tìm kiếm thành công!")
            return father
        
        # 2.4. for mỗi trạng thái v kề u do {Đặt v vào cuối danh sách L; father(v) <- u}
        neighbors = graph.get(u, [])
        for v in neighbors:
            L.append(v)        # Đặt v vào cuối danh sách L
            father[v] = u      # father(v) <- u

graph_data = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['L', 'M'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['P', 'Q'],
    'J': ['N'],
    'K': ['S'],
    'L': ['T'],
    'P': ['U']
}

father_result = breadth_first_search(graph_data, start_node='A', goal_node='P')