def simulate_day(friends, today_status):
    n = len(today_status)
    next_status = [0] * n  # Initialize the status for the next day

    for i in range(n):
        wfo_friends = sum(1 for friend_id in friends[i] if today_status[friend_id] == 1)
        
        # Apply the rules for WFO status update
        if today_status[i] == 1 and wfo_friends == 3:
            next_status[i] = 1
        elif today_status[i] == 0 and wfo_friends < 3:
            next_status[i] = 1
    
    return next_status

def solve():
    # Input for number of employees and friendships
    n, m = map(int, input().split())
    
    friends = [[] for _ in range(n)]  # Initialize the adjacency list
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    
    # Input for the target roster value
    k = int(input())
    myset=set()
    for i in range(10):
        myset.add(i)
    current_status = [1] * n  # All employees start with WFO status
    roster_value = n  # Initial roster value
    days = 1  # Start from day 1
    
    while roster_value < k:
        next_status = simulate_day(friends, current_status)
        
        # Count WFO employees for the day
        today_wfo = sum(next_status)
        
        roster_value += today_wfo
        current_status = next_status
        days += 1
    
    print(days)

solve()
