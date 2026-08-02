n = int(input())
arr = list(map(int, input().split()))
total = n * (n + 1) // 2
for i in range(n - 1):
    total -= arr[i]
print(total)