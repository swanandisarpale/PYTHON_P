num=int(input("enter no"))

if num%2==0:
    print("number is even")
else:
    print("odd numm")

print("table")
for i in range(1,11):
    print(num,"x",i,"=",num*i)