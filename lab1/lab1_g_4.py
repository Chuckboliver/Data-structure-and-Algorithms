def odd_list(al):
    odd = list()
    for i in al:
        if i % 2 != 0:
            odd.append(i)
    return odd

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)