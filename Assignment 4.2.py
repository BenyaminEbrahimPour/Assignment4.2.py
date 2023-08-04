import random
x=int(input('lenght of S::'))
S=[]
# i=1
# while i<=x:
for x in range(x) :
    e=random.randint(1,10000)
    # t=0
    t=1
    S.append(e)
    # while t<i:
    for t in range(t):
            if e==S[t] :
                e=random.randint(1,100)
                t=t+1
                S.append(e)
                #print(S)
                # i=i+1
            #else :
                #S.append(e)
                # i=i+1
print(S)