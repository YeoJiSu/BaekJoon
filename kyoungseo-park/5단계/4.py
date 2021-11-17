import sys

# 1000보다 작거나 같고, 음이 아닌 정수. 
# 첫줄에 42로 나누었을 때 서로 다른 나머지를 출력한다.

input_data = []
for a in range(10):
    xxx = [int(x) for x in sys.stdin.readline().split()][0]
    input_data.append(xxx % 42)

my_set = set(input_data) #집합set으로 변환
input_data = list(my_set) #list로 변환
print(len(input_data))