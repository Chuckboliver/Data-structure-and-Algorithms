def multiple_3_5(n):
    ans = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            ans += i
    return ans
print(multiple_3_5(10))