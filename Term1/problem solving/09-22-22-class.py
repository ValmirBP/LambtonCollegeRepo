from random import randint
count=0
average=0

while count < 100:

    for i in range(0,100):
        rand_number=randint(1,100)

        if rand_number == 35:
            count+=1
            average = count/100
            
print(count)
print(average)
