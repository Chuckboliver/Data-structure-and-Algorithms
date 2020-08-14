s = input("Enter String : ")
mapping = dict()
index = -1
for char in s:
    if char not in mapping.keys():
        index += 1
    mapping.setdefault(char,index)
print([mapping[char] for char in s])
