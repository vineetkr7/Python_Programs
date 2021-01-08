# number triangle patterns

n = int(input())

for i in range(n):
    print(str(i+1)*(i+1))

print("\n")
for i in range(n):
    print((" "*(n-i-1)) + (str(i+1)*(i+1)))

print("")
for i in range(n,0,-1):
    print(str(i)*i)

print("")
for i in range(n,0,-1):
    print((" "*(n-i)) + (str(i)*(i)))

print("")
temp = 1
for i in range(n):
    print((" "*(n-i-1)) + (str(i+1)*temp))
    temp+=2

print("")
temp-=2
for i in range(n,0,-1):
    print((" "*(n-i)) + (str(i)*temp))
    temp-=2

print("")
for i in range(n):
    print((" "*(n-i-1)) + (str(i+1)*(i+1)))
for i in range(n-1,0,-1):
    print((" "*(n-i)) + (str(i)*(i)))

print("")
for i in range(n):
    print(str(i+1)*(i+1))
for i in range(n-1,0,-1):
    print(str(i)*i)
