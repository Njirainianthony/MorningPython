#WHILE LOOP
#Incrementing
num=20 #initialize
while num<=25: #condition
    print(num)
    num+=1


number=105
while number<=110:
    print("Number is", number)
    number+=1


#Decrementing
num2=10
while num2>=1:
    print(num2)
    num2-=1



#BREAK AND CONTINUE STATEMENT
a=25
while a<=30:
    print(a)
    if a==27:
        break #break statement
    a+=1


b=0
while b<=5:
    b+=1
    if b==3:
        continue
    print(b)


#FOR LOOP
for y in range(7):
    print(y)

for z in range(40,45):
    print(z)

for mynum in range(100,110,3):
    print(mynum)


languages=["Python", "Php", "Kotlin", "Java"]
for lang in languages:
    print(lang)