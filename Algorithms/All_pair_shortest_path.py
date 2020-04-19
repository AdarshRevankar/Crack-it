# starting vertex -> all the other vertex
# For each vertex
#
# Logic:
#   Take the each vertex as intermediate vertex.
#   Then shift the vertex from all vertex to other vertex.

# ==========================================================
#      ALL PAIR SHORTEST PATH
# ==========================================================
data = [x.split() for x in [line.replace('\n', '') for line in open('Data/All_pair_shortest_path.txt', 'r')]]

n = len(data[0])

for i in range(n):
    for j in range(n):
        print(int(data[i][j]), end=' ')
    print()

for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(int(data[i][j]), int(data[i][k]) + int(data[k][j]))

print()
for i in range(n):
    for j in range(n):
        print(data[i][j], end=' ')
    print()
