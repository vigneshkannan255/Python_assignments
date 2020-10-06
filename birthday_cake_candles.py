n=int(input())
x=[int(j) for j in input().split()[:n]]
print(x.count(max(x)))

