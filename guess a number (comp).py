
import random
s=100
hs=0
c=random.randint(1,100)
print("guess the number between 1 and 100 ,U have got 10 chances")
for i in range(10):
    a=int(input("guess the no :"))
    if a>c:
        print("predict less")
        s-=10
    elif a<c:
        print("predict greater")
        s-=10
    if a==c:
        print("U have guessed it right")
        print("score:", s)
       
        break


            
        