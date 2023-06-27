import csv
import itertools
import math

def read_csv(file_path):
    
    #csv파일에서 데이터를 읽어와서 배열에 저장
    nodes = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 첫 번째 행인 헤더를 건너뜁니다
        for row in reader:
            city_id = int(row[0])
            x = float(row[1])
            y = float(row[2])
            z = float(row[3])
            nodes[city_id] = (x, y, z)
    return nodes


    # 두 노드 간의 거리 계산
def Distance(node1, node2):
    x1, y1, z1 = node1
    x2, y2, z2 = node2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def create_distance(nodes):
   
    num_nodes = len(nodes)
    distance_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            distance_matrix[i][j] = Distance(nodes[i], nodes[j])
    return distance_matrix


def calculate_path_distance(path, distance_matrix):
   
    distance = 0
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]
        distance += distance_matrix[node1][node2]
    return distance

def find_shortest_path(nodes):
   
    num_nodes = len(nodes)
    indices = list(range(num_nodes))
    shortest_distance = float('inf')
    shortest_path = None
    distance_matrix = create_distance(nodes)

    num = 0
    for permutation in itertools.permutations(indices):
        
        num +=1
        print(num)
        path = list(permutation)
        path.append(path[0])  # 마지막으로 처음 노드로 돌아오도록 경로를 완성
        distance = calculate_path_distance(path, distance_matrix)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

# CSV 파일 경로
file_path = 'cities30.csv'

# CSV 파일 읽기
nodes = read_csv(file_path)

# 최단 경로 찾기
shortest_path, shortest_distance = find_shortest_path(nodes)

# 결과 출력
print("최단 경로:", shortest_path)
print("최단 거리:", shortest_distance)

# 6, 0120, 79.04128177927416