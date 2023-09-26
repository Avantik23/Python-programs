# def octal(n):
#     print(oct(n))

# def reverse_int(n):
#     r=0
#     while(n!=0):
#         r=r*10+n%10
#         n//=10
#     print(r)

# def fib(n):
#     if (n == 0):
#         return 0
#     elif(n == 1):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)


# octal(29)
# reverse_int(302)
# for i in range(3):
#     print(fib(i),end=" ")

# print("\nFourth fibonacci number:",fib(4))
import re
s="John000Wick"
a=re.split('0',s)
print(a)