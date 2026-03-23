"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    graph = {i:[] for i in range(vertices)}

    # 화살표를 단 한 번도 받지 않는 노드(진입 차수가 0인 노드)도 포함되어야 하기 때문에 모두 0으로 초기화함
    in_degree = [0]*vertices
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for i , j in edges:
        graph[i].append(j)
        in_degree[j] += 1 # 화살표를 받는 쪽이 올라야 함
    
    zero_ver = [i for i in range(vertices) if in_degree[i] == 0]
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    que = deque(zero_ver)

    # TODO: 큐가 빌 때까지 반복
    result = []
    while que:
        ## 큐에서 정점 꺼내기
        curr = que.popleft()
        result.append(curr)

        ## 인접한 정점들의 진입 차수 감소
        for k in graph[curr]:
            in_degree[k] -= 1
        
            # 만약 k의 차수가 0이 되었다면, 큐에 추가
            if in_degree[k] == 0:
                que.append(k)

    return result

def topological_sort_2(ver, edges):
    adj = {v:[] for v in ver}
    indg = {v:0 for v in ver}

    for u, v in edges:
        adj[u].append(v)
        indg[v] += 1

    que = deque([v for v in ver if indg[v] == 0])
    result = []

    while que:
        curr = que.popleft()
        result.append(curr)

        for neib in adj[curr]:
            indg[neib] -= 1
            if indg[neib] == 0:
                que.append(neib)
        
    return result


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
