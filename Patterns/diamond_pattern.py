# diamond pattern

n = int(input())

print("")
temp = 1
for i in range(n):
    print((" "*(n-i-1)) + ("*"*temp))
    temp+=2

temp-=4
for i in range(n-1,0,-1):
    print((" "*(n-i)) + ("*"*temp))
    temp-=2
