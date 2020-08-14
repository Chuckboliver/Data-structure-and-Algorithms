print("*** Odd Even ***")
typ,ite,conf = input("Enter Input : ").split(",")
if typ == "L":
    ite = ite.split()
op = {"Even":1, "Odd":0}
print(ite[op[conf]:len(ite):2])