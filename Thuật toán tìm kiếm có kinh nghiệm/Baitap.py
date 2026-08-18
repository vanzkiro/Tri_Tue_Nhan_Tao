def best_first_search(graph, heuristics, start, goal):
    # 1. Khởi tạo danh sách L chứa trạng thái ban đầu (heuristic, tên_nút)
    L = [(heuristics[start], start)]
    father = {}
    visited = set()
    
    print(f"Khởi tạo -> L = [{start}({heuristics[start]})]")

    # 2. Vòng lặp
    loop = 1
    while L:
        # 2.2. Loại trạng thái u ở đầu danh sách L
        h_u, u = L.pop(0)
        visited.add(u)
        
        # 2.3. Nếu u là trạng thái kết thúc thì dừng
        if u == goal:
            print(f"Vòng {loop}: Loại {u} -> Đích.")
            return father
            
        # 2.4. Xét các trạng thái v kề u
        for v in graph[u]:
            if v not in visited and not any(node == v for _, node in L):
                father[v] = u
                L.append((heuristics[v], v))
            
        L.sort()
        
        # Hiển thị thông tin rút gọn của vòng lặp
        l_str = ", ".join([f"{node}({h})" for h, node in L])
        print(f"Vòng {loop}: Loại {u} -> L = [{l_str}]")
        loop += 1
        
    print("Thất bại")
    return None

graph = {
    'A': ['B', 'C'], 'B': ['D'], 'C': ['D', 'E'],
    'D': ['F'], 'E': ['F'], 'F': []
}
heuristics = {'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2, 'F': 0}

final_father = best_first_search(graph, heuristics, 'A', 'F')

# Truy vết đường đi
curr = 'F'
path = []
while curr in final_father:
    path.append(curr)
    curr = final_father[curr]
path.append('A')
path.reverse()

print(f"\n=> Kết quả đường đi: {' -> '.join(path)}")