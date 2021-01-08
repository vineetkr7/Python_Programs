# triangle patterns

n = int(input())

print("\n1.")
for i in range(n):
    print("*"*(i+1))

print("\n2.")
for i in range(n):
    print((" "*(n-i-1)) + ("*"*(i+1)))

print("\n3.")
for i in range(n,0,-1):
    print("*"*i)

print("\n4.")
for i in range(n,0,-1):
    print((" "*(n-i)) + ("*"*(i)))

print("\n5.")
temp = 1
for i in range(n):
    print((" "*(n-i-1)) + ("*"*temp))
    temp+=2

print("\n6.")
temp-=2
for i in range(n,0,-1):
    print((" "*(n-i)) + ("*"*temp))
    temp-=2

print("\n7.")
for i in range(n):
    print((" "*(n-i-1)) + ("*"*(i+1)))
for i in range(n-1,0,-1):
    print((" "*(n-i)) + ("*"*(i)))

print("\n8.")
for i in range(n):
    print("*"*(i+1))
for i in range(n-1,0,-1):
    print("*"*i)
