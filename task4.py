

n = 110, 30, 34, 67, 33, 65, 19, 80, 98, 45
capacity = 200
def solve(n, capacity):
    m = [0] * (capacity + 1)
    prev = m[:]
    for w in n:
        for c in range(capacity + 1):
            m[c] = prev[c] if w > c else max(prev[c], prev[c-w] + w)
        prev, m = m, prev
    return print('Max weight:', prev[-1])
solve(n, capacity)