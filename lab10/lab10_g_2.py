from collections import deque
left, right = input("Enter Input : ").split('/')
left, right = list(map(int, left.split())), list(map(int, right.split()))
left.sort()
Q = deque(sorted(right))
for n  in left:
    if  len(Q) > 0 and n > Q[0]:
        Q.popleft()
        print(n)
for i in range(len(Q)):
    print("No First Greater Value")  
        