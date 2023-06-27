import csv
import math
import itertools

# 2차원 배열 사용(메모리 부족으로 실행 중단됨.)

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
    # 동적 계획법 활용
   
    num_nodes = len(nodes)
    # 모든 노드들 간의 거리를 계산하여 distance에 저장

    # 2차원 배열 초기화
    distance = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            distance[i][j] = Distance(nodes[i], nodes[j])

    # dp 배열을 생성 dp는 최단 거리를 저장
    # dp[i][j]는 현재 위치가 i이고, 방문한 노드 집합이 j일 때의 최단 거리를 의미
    # float('inf')  양의 무한대를 의미하는 특수한 부동 소수점 값입니다.
    dp = [[float('inf')] * (2 ** num_nodes) for _ in range(num_nodes)]
    dp[0][1] = 0  # 출발 노드를 0으로 설정합니다.

    # 동적 계획법을 사용하여 최단 거리를 계산합니다.
    for visited in range(1, 2 ** num_nodes):
        for current in range(num_nodes):
            if visited & (1 << current):  # current 노드가 방문되었을 때
                for prev in range(num_nodes):
                    if prev != current and visited & (1 << prev):  # prev 노드가 방문되었을 때
                        dp[current][visited] = min(
                            dp[current][visited],
                            dp[prev][visited ^ (1 << current)] + distance[prev][current])

    """
visited 변수는 현재까지 방문한 노드들의 집합을 나타냅니다. 

current 변수는 현재 위치한 노드를 나타냅니다. 

visited 변수와 current 노드를 비트 연산하여 current 노드가 방문되었는지 확인합니다. 

prev 변수는 이전에 방문한 노드들을 나타냅니다. 

prev 노드가 current 노드와 같지 않고, prev 노드가 이미 방문되었는지 확인합니다. 

최단 거리를 계산하여 dp 리스트에 2차원으로 저장합니다. 
"""

    # 최단 경로 구하기
    path = [0]
    visited = (1 << num_nodes) - 1
    current = 0
    while visited != 1:
        for next_node in range(num_nodes):
            if next_node != current and visited & (1 << next_node):
                if dp[current][visited] == dp[next_node][visited ^ (1 << current)] + distance[next_node][
                    current]:
                    path.append(next_node)
                    visited ^= (1 << current)
                    current = next_node
                    break

    return path, dp[0][(1 << num_nodes) - 1]


# CSV 파일 경로
file_path = 'cities30.csv'

# CSV 파일 읽기
nodes = read_csv(file_path)

# 최단 경로 계산
shortest_path, shortest_distance = tsp(nodes)

# 결과 출력
print("최단 경로:", shortest_path)
print("최단 거리:", shortest_distance)
