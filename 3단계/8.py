import sys
num = int(sys.stdin.readline())
for i in range(0,num):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a,b,a+b))