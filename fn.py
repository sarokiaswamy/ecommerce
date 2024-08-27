p=[]

for i in range(1,11):
    vote = input("Y N O ?")
    p.append(vote)
    
YL = list(filter( lambda x:x=='Y' , p))

NL = list(filter( lambda x:x=='N' , p))

OL = len(p) - (len(YL) + len(NL))

print('Yes voting ' , len(YL))
print('No voting ' , len(NL))
print('Not sure voting ' , OL)


