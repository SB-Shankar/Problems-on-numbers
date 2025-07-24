def head(n):
    if n==0:
        return
    print(n)
    head(n-1)
num=int(input("enter a numbers:"))
head(num)    