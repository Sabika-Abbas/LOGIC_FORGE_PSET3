from collections import defaultdict
import io

def main():
    N,Q,K=map(int,input().split())
    
    subscriptions=defaultdict(set)
    messages=[]
    next_id=1
    
    for time in range(Q):
        parts=input().split()
        op=parts[0]
        
        if op=='B':
            u=int(parts[1])
            m=int(parts[2])
            critical=(m % 3 == 0)
            messages.append((next_id, u, time, critical))
            next_id+=1
            
        elif op=='S':
            u=int(parts[1])
            v=int(parts[2])
            subscriptions[u].add(v)
            
        elif op=='U':
            u=int(parts[1])
            v=int(parts[2])
            if v in subscriptions[u]:
                subscriptions[u].remove(v)
                
        elif op=='F':
            u=int(parts[1])
            visible=[]
            
            for msg_id, sender, msg_time, critical in messages:
                if sender==u or sender in subscriptions[u]:
                    visible.append((msg_time, critical, msg_id))
            
            visible.sort(key=lambda x: (-x[0], -x[1]))
            
            sender_counts=defaultdict(int)
            filtered=[]
            for msg_time, critical, msg_id in visible:
                for m_id, sndr, m_time, m_crit in messages:
                    if m_id==msg_id:
                        sender=sndr
                        break
                
                if sender_counts[sender] < K:
                    filtered.append(msg_id)
                    sender_counts[sender]+=1
                
                if len(filtered)>=10:
                    break
            
            if filtered:
                print(' '.join(map(str, filtered)))
            else:
                print('EMPTY')

if __name__ == "__main__":
    test_input = """3 9 2
S 1 2
S 1 3
B 2 5
B 3 9
F 1
U 1 2
B 3 6
F 1
F 2"""
    import sys
    sys.stdin = io.StringIO(test_input)
    main()