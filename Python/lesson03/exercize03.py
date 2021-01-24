def sum_max(a, b, c):
    if min(a, b) >= c:
        return a + b
    else:
        return max(a, b) + c


print(sum_max(9, 9, 8))