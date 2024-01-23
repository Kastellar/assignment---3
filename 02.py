def squacube(n):
    result = [x**2 if x % 2 == 0 else x**3 for x in range(1, n+1)]
    return result

n = int(input())
result_list = squacube(n)
print(result_list)
