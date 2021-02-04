def integer_right_triangle(n):
    ans = list()
    for i in range(1,n):
        for j in range(i,n):
            k = n-i-j
            if k<i or k<j:
                break
            if k*k == i*i+j*j:
                ans.append((i,j,k))
    return ans
print(integer_right_triangle(12))