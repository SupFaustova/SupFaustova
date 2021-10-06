n = int(input())
a = []
b = []
q = 1
m = 0
for o in range(n):
    a.append([0] * n)
for qw in range(n * n):
    b += [qw + 1]
i, j = 0, 0
if n >= 1:
    a[0][0] = 1
while not m == n * 2 - 1:
    while j + 1 < len(a) and m < n * 2 - 1:
        if a[i][j + 1] == 0:
            j += 1
            a[i][j] = b[q]
            q += 1
    m += 1
    while i + 1 < len(a) and m < n * 2 - 1:
        if a[i + 1][j] == 0:
            i += 1
            a[i][j] = b[q]
            q += 1
    m += 1
    while j - 1 >= 0 and m < n * 2 - 1:
        if a[i][j - 1] == 0:
            j -= 1
            a[i][j] = b[q]
            q += 1
    m += 1
    while i - 1 > 0 and m < n * 2 - 1:
        if a[i - 1][j] == 0:
            i -= 1
            a[i][j] = b[q]
            q += 1
    m += 1
print(i, j)

print(a)
for k in range(len(a)):
    print(*a[k])