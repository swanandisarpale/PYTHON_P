def simple_intrest(p,r,t):
    si=p*r*t/100
    return si

def factorial(n):
    if n==0 or n==1:
        return 1
    else:  
        return n*factorial(n-1)

p=float(input("eneter p"))
r=float(input("enter r"))
t=float(input("enter t"))

result_si=simple_intrest(p,r,t)
print("si",result_si)

n=int(input("enetr num for fact"))
fact=factorial(n)
print("fact",fact)


