def add_min_mul_div(a,b):
    return a+b,a-b,a*b,a/b


sum,min,mul,div =add_min_mul_div(4,2)

print("sum:",sum)
print("min:",min)
print("mul:",mul)
print("div:",div)

# sum=add_min_mul_div(4,2)
# sum => ()사용, 튜플 
# print("sum",sum[2])