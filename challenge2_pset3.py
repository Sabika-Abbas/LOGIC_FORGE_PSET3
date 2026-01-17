def solve(N, Q, limit, weights, priority, queries):
    people = list(range(N))
    people.sort(key=lambda i: weights[i])
    
    priority_people = [i for i in people if priority[i] == 1]
    non_priority_people = [i for i in people if priority[i] == 0]
    
    p_left, p_right = 0, len(priority_people) - 1
    np_left, np_right = 0, len(non_priority_people) - 1
    boats = 0
    
    while p_left <= p_right and np_left <= np_right:
        if weights[priority_people[p_left]] + weights[non_priority_people[np_right]] <= limit:
            boats += 1
            p_left += 1
            np_right -= 1
        else:
            boats += 1
            p_left += 1
    
    if p_left <= p_right:
        boats += (p_right - p_left + 1)
    
    if np_left <= np_right:
        np_list = non_priority_people[np_left:np_right+1]
        l, r = 0, len(np_list) - 1
        while l <= r:
            if l == r:
                boats += 1
                break
            elif weights[np_list[l]] + weights[np_list[r]] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
    
    min_boats = boats
    results = [f"Minimum boats = {min_boats}"]
    
    for query in queries:
        cmd = query[0]
        
        if cmd == "CANPAIR":
            X, Y = query[1], query[2]
            weight_ok = (weights[X] + weights[Y] <= limit)
            priority_ok = not (priority[X] == 1 and priority[Y] == 1)
            results.append("Yes" if weight_ok and priority_ok else "No")
            
        else: 
            B = query[1]
            p_left, p_right = 0, len(priority_people) - 1
            np_left, np_right = 0, len(non_priority_people) - 1
            boats_used, saved = 0, 0
            
            while p_left <= p_right and np_left <= np_right and boats_used < B:
                if weights[priority_people[p_left]] + weights[non_priority_people[np_right]] <= limit:
                    saved += 2
                    boats_used += 1
                    p_left += 1
                    np_right -= 1
                else:
                    saved += 1
                    boats_used += 1
                    p_left += 1
            
            while p_left <= p_right and boats_used < B:
                saved+=1
                boats_used+=1
                p_left+=1
            
            if np_left<=np_right and boats_used < B:
                np_list=non_priority_people[np_left:np_right+1]
                l, r=0, len(np_list)-1
                while l<=r and boats_used<B:
                    if l==r:
                        saved+=1
                        boats_used+=1
                        break
                    elif weights[np_list[l]]+weights[np_list[r]]<=limit:
                        saved += 2
                        boats_used += 1
                        l += 1
                        r -= 1
                    else:
                        saved += 1
                        boats_used += 1
                        r -= 1
            
            results.append(str(N - saved))
    
    return results


if __name__ == "__main__":
    N1 = 6
    Q1 = 3
    limit1 = 100
    weights1 = [30, 50, 60, 40, 70, 80]
    priority1 = [1, 0, 1, 0, 0, 1]
    queries1 = [
        ["CANPAIR", 0, 1],
        ["CANPAIR", 0, 2],
        ["REMAINING", 2]
    ]
    
    results1 = solve(N1, Q1, limit1, weights1, priority1, queries1)
    for result in results1:
        print(result)
