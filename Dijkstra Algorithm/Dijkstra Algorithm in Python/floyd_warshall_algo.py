INF = float('inf')

'''
INPUT - 
4 4
0 3 10
0 1 5
1 2 3
2 3 1
'''

def printmatrix(m):
    r, c = len(m), len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j], end="\t")
        print()
    print("--------------------------------")

v, e = map(int, input().split())

m = [[INF]*v for i in range(v)]
for i in range(v):
    for j in range(v):
        if i == j:
            m[i][j] = 0
# printmatrix(m)

for i in range(e):
    s, d, w = map(int, input().split())
    m[s][d] = w
printmatrix(m)

for k in range(v):
    for i in range(v):
        for j in range(v):
            print(k, i, j)
            printmatrix(m)
            if m[i][k] + m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]
print("\n/////////////////////////////\nFinal Matrix")
printmatrix(m)