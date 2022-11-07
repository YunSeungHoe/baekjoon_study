import sys
n = int(sys.stdin.readline())
word = []

for i in range(n):
    word.append(sys.stdin.readline().strip())
word = set(word)
word = list(word)
word.sort()
word.sort(key= len)

for i in range(len(word)):
    print(word[i])