sub_set = set()


s = input()

for i in range(len(s)):
    for j in range(len(s)+1):
        sub_set.add(s[i:j])

print(len(sub_set)-1)