d = list(list(map(int, input().split())) for _ in range (10))

x = 1
y = 1
d[x][y] = 9

while d[x][y] != 2 :
    if d[x][y+1] != 1 :
        y += 1
        if d[x][y] == 2 :
            d[x][y] = 9
            break
        d[x][y] = 9
        continue
    
    if d[x+1][y] != 1 :
        x += 1
        if d[x][y] == 2 :
            d[x][y] =9
            break
        d[x][y] = 9
    else :
        break

for i in range (10) :
    for j in range (10) :
        print(d[i][j], end = ' ')
    print()