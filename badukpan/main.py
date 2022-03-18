p = []
for i in range(19) :
    p.append([])
    for j in range(19) :
        p[i].append(0)

n = int(input())
for i in range(n) :
    X, Y = input().split()
    x = int(X)
    y = int(Y)
    if (p[x-1][y-1] == 0) :
        p[x-1][y-1] += 1

for i in range(19) :
    for j in range(19) :
        print(p[i][j], end = ' ')
    print()