def best_first_search(graph, heuristic, start_node, goal_node):
    # 1. Khởi tạo danh sách L chỉ chứa trạng thái ban đầu
    L = [start_node]
    father = {}

    print(" TÌM KIẾM THEO CHIỀU TỐT NHẤT (BEST-FIRST SEARCH) ")
    stt = 1

    while True:
        # 2.1. Nếu L rỗng thì tìm kiếm thất bại
        if not L:
            print("Thông báo: Tìm kiếm thất bại!")
            return None

        # 2.2. Lấy trạng thái đầu danh sách L
        u = L.pop(0)

        print(f"Bước {stt}: u = {u} | L còn lại = {L}")
        stt += 1

        # 2.3. Nếu u là trạng thái kết thúc
        if u == goal_node:
            print("Thông báo: Tìm kiếm thành công!")
            return father

        # 2.4. Thêm các trạng thái kề u vào L
        neighbors = graph.get(u, [])

        for v in neighbors:
            L.append(v)
            father[v] = u

        # Sắp xếp L theo hàm đánh giá h(n) tăng dần
        L.sort(key=lambda x: heuristic[x])


# Đồ thị theo hình
graph_data = {
    'A': ['C', 'D', 'E'],
    'C': ['F'],
    'D': ['F', 'I'],
    'E': ['K', 'G'],
    'F': ['B'],
    'I': ['B', 'G'],
    'G': ['B', 'H'],
    'H': ['B'],
    'K': [],
    'B': []
}

# Hàm đánh giá h(n)
heuristic = {
    'A': 20, 'B': 0, 'C': 15, 'D': 6, 'E': 7, 'F': 10, 'I': 8, 'G': 5, 'H': 3, 'K': 12
}

father_result = best_first_search(
    graph_data,
    heuristic,
    start_node='A',
    goal_node='B'
)