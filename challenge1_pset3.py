def solve_smart_city(N, K, temperatures, queries):
    INF = 10**9
    alert = [INF] * N
    
    for i in range(N):
        for j in range(i + 1, N):
            if temperatures[j] >= temperatures[i] + K or temperatures[j] <= temperatures[i] - K:
                alert[i] = j
                break
    
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + (1 if alert[i] < INF else 0)
    
    results = []
    for query in queries:
        cmd, *args = query
        if cmd == "NEXT":
            X = int(args[0])
            results.append(str(alert[X]) if alert[X] < INF else "No Alert")
        else:
            L, R = int(args[0]), int(args[1])
            results.append(str(prefix[R + 1] - prefix[L]))
    
    return results


def main():
    N, K, Q = map(int, input().split())
    temperatures = list(map(int, input().split()))
    
    queries = []
    for _ in range(Q):
        queries.append(input().split())
    
    results = solve_smart_city(N, K, temperatures, queries)
    
    for result in results:
        print(result)


if __name__ == "__main__":
    print("Test Case 1:")
    N1, K1, Q1 = 8, 3, 4
    temp1 = [73, 74, 75, 71, 69, 72, 76, 73]
    queries1 = [
        ["NEXT", "0"],
        ["NEXT", "3"],
        ["COUNT", "0", "7"],
        ["COUNT", "4", "7"]
    ]
    
    results1 = solve_smart_city(N1, K1, temp1, queries1)
    for r in results1:
        print(r)
    
    
    
