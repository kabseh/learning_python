# n = int(input())
# for i in range(1, (n+1)):
#   if n % i == 0:
#        print(i)


n = int(input())
triangle = '#'

for i in range(0, n):
    print(triangle)
    triangle += '#'
    # print(triangle)
    # for k in range(0, i+1):
    # print("#",end="")
print()
