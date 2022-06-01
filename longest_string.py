txt = input()

words=txt.split()
count=0
num=[]
i=0
for word in words :
    count=len(word)    
    num.append(count)

longest=max(num)

for n in range(0,len(num)):
  if num[n]==longest:
    l=n
    
print(words[l])

