def length(txt):     
    #Code Here
    l = list(txt)
    n = 0
    if txt == "":
        return 0
    if l!=[]:
        print(f"{l.pop(0)}*",end="")
        n += 1
    if l !=[]:
        print(f"{l.pop(0)}~",end="")
        n += 1
    return  n + length("".join(l))
        
    
print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)