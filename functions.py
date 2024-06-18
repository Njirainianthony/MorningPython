#IN-BUILT FUNCTIONS (STANDARD LIBRARY FUNCTIONS) - ALREADY EXIST

y=max(243,788,23,78,98)
print(y)

x=min(243,788,23,78,98)
print("The minimum value is",x)

z=pow(2,8)
print(z)

#USER-DEFINED FUNCTIONS

def student():
    print("Anthony Njiraini")

student() #CALLING A FUNCTION


def person():
    print("Person is walking")

person()



#PARAMETERS AND ARGUMENTS
def add(x,y):
    print(x+y)


add(7,8)
add(4,6)



#EMPLOYEE DETAILS PROGRAM

def employee(name,age,email,marital,posistion):
    print(name+age+email+marital+posistion)

employee("Anthony Njiraini ","23 ","njirainianthony@gamil.com ","single ","CEO")
employee("Isaac Rwamba ","45 ","issac@gmail,com ","married ","Secretary ")
employee("Cristiano Ronaldo ","39 ","cr7@gmail,com ","married ","GOAT ")
employee("Mike Tyson ","57 ","ironmike@gmail,com ","married ","South paw ")
employee("Floyd Mayweather ","50 ","moneymay@gmail,com ","married ","Orthodox ")


