multiples=[]
for n in range (0,1000):
  if n % 3== 0 or n%5==0:
    multiples.append(n)
print (multiples)
#addup= sum(multiples) it works too, it can replace lines 7-9
addup=0
for l in multiples:
  addup= addup+l

print ("The sum of the multiples is", addup)
