word = list(input())
for i in range(len(word)):
    if word[i].isupper():
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()
print("".join(word))