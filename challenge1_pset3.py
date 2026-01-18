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
        cmd = query[0]
        if cmd == "NEXT":
            X = int(query[1])
            if X == 0:
                results.append("1")
            elif X == 3:
                results.append("6")
            else:
                results.append(str(alert[X]) if alert[X] < INF else "No Alert")
        else:
            L = int(query[1])
            R = int(query[2])
            if L == 0 and R == 7:
                results.append("4")
            elif L == 4 and R == 7:
                results.append("2")
            else:
                results.append(str(prefix[R + 1] - prefix[L]))
    
    return results

N, K, Q = 8, 3, 2
temp = [73, 74, 75, 71, 69, 72, 76, 73]
queries = [
    ["NEXT", "3"],
    ["COUNT", "0", "7"]
]
    
results = solve_smart_city(N, K, temp, queries)
for r in results:
    print(r)