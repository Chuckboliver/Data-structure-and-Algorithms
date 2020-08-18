from collections import OrderedDict
class funString :
    
    def __init__(self,word,flag):
        self.word = word
        self.flag = flag
        self.cmd = {"1":str(len(word)), "2":word.swapcase(), "3":word[::-1], "4":"".join(OrderedDict.fromkeys(word)) }
    def __str__(self):
        return self.cmd[flag]

word,flag = input("Enter String and Number of Function : ").split()
t1 = funString(word,flag)
print(t1) 