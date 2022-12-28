import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = [input().strip() for _ in range(n)]
m_list = [input().strip() for _ in range(m)]
n_set = set(n_list)
m_set = set(m_list)
sum_set = n_set & m_set
sum_list = list(sum_set)
sum_list.sort()
print(len(sum_list))
for i in sum_list:
    print(i)    