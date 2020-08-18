def gen_pattern(chars):
    line = list()
    for i in range(len(chars)):
        s = ".".join(chars[i:len(chars)])
        line.append((s[::-1]+s[1:]).center(4*len(chars)-3,"."))
    print("\n".join(line[:0:-1]+line))
gen_pattern("XY")