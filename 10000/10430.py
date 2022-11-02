command = list(map(int, input().split()))

print((command[0]+command[1])%command[2])
print(((command[0]%command[2]) + (command[1]%command[2]))%command[2])
print((command[0]*command[1])%command[2])
print(((command[0]%command[2])*(command[1]%command[2]))%command[2])