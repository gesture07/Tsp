import csv
import math
import itertools

# 1차원 배열 사용

def read_csv(file_path):

    #csv파일에서 데이터를 읽어와서 배열에 저장

    nodes = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 첫 번째 행을 건너뜁니다.
        for row in reader:
            nodes.append((float(row[1]), float(row[2]), float(row[3])))
    return nodes



def Distance(node1, node2):
    # 두 노드 간의 거리 계산
    
    x1, y1, z1 = node1
    x2, y2, z2 = node2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def tsp(nodes):
    num_nodes = len(nodes)

    # 거리 행렬 계산
    # 2차원 리스트 초기화
    distance = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            distance[i][j] = Distance(nodes[i], nodes[j])

    # dp 배열 초기화
    dp = [float('inf')] * (2 ** num_nodes)
    dp[1] = 0  # 출발 노드를 0으로 설정

    # 동적 계획법
    for visited in range(1, 2 ** num_nodes):
        for current in range(num_nodes):
            if visited & (1 << current):  # current 노드가 방문되었을 때
                prev_visited = visited ^ (1 << current)
                for prev in range(num_nodes):
                    if prev != current and prev_visited & (1 << prev):  # prev 노드가 방문되었을 때
                        dp[visited] = min(dp[visited], dp[prev_visited] + distance[prev][current])

    # 최단 경로 구하기
    path = []
    visited = (2 ** num_nodes) - 1
    current = 0
    while visited != 0:
        path.append(current)
        next_node = min(range(num_nodes), key=lambda x: dp[visited] + distance[x][current])
        visited ^= (1 << current)
        current = next_node

    return path, dp[(2 ** num_nodes) - 1]



# CSV 파일 경로
file_path = 'cities30.csv'

# CSV 파일 읽기
nodes = read_csv(file_path)

# 최단 경로 계산
shortest_path, shortest_distance = tsp(nodes)

# 결과 출력
print("최단 경로:", shortest_path)
print("최단 거리:", shortest_distance)
