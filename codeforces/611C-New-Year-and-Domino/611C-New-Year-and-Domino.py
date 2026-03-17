import sys
input = sys.stdin.readline

h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]


horizontal = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w-1):
        if grid[i][j] == '.' and grid[i][j+1] == '.':
            horizontal[i][j] = 1


vertical = [[0]*w for _ in range(h)]

for i in range(h-1):
    for j in range(w):
        if grid[i][j] == '.' and grid[i+1][j] == '.':
            vertical[i][j] = 1


pref_h = [[0]*(w+1) for _ in range(h+1)]
pref_v = [[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        pref_h[i+1][j+1] = (
            pref_h[i+1][j] +
            pref_h[i][j+1] -
            pref_h[i][j] +
            horizontal[i][j]
        )

        pref_v[i+1][j+1] = (
            pref_v[i+1][j] +
            pref_v[i][j+1] -
            pref_v[i][j] +
            vertical[i][j]
        )


def get_sum(pref, r1, c1, r2, c2):
    return (
        pref[r2][c2]
        - pref[r1][c2]
        - pref[r2][c1]
        + pref[r1][c1]
    )

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

   
    r1 -= 1
    c1 -= 1

    
    h_count = get_sum(pref_h, r1, c1, r2, c2-1)

    
    v_count = get_sum(pref_v, r1, c1, r2-1, c2)

    print(h_count + v_count)