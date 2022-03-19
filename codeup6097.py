a, b = map(int, input().split())

p = [list(0 for i in range(b)) for j in range(a)]

n = int(input())

for i in range(n) :
    l, d, x, y = map(int, input().split())
    if (d == 0) :
        for j in range(l) :
            p[x-1][y+j-1] = 1
    else :
        for j in range(l) :
            p[x+j-1][y-1] = 1
    

for i in range (a) :
    for j in range (b) :
        print(p[i][j], end = ' ')
    print()
