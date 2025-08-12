l=eval(input())
rep=[]
for n in l:
    if n>1:
        i=2
        while i<=n//2+1:
            if n%i==0:
               if n%2==0:
                   rep.append('even')
               else:
                   rep.append('odd')
               break
            i+=1
        else:
            rep.append('prime')
    else:
        rep.append('odd')
print(rep)
