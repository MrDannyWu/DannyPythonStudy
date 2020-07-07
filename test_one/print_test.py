import time
t1 = time.time()*1000
sum = 0
for i in range(100000000):
    sum += i
    #print(i)

t2 = time.time()*1000
print(sum)
print("Python Time: ",(t2 - t1)/1000) 
