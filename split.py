import random

x = list(licenses['name'])

random.shuffle(x)
f = open('./train.txt','w+')
y = open('./val.txt','w+')

for i in range(len(x)):
  if i % 10 ==0:
    y.write('/darknet/data/obj/'+x[i]+'\n')
  else:
    f.write('/darknet/data/obj/'+x[i]+'\n')
y.close()
f.close()
