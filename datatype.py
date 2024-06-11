#Datatype

number=60 #this is an integer
convertnum=str(number)
num=45.36 #float
greeting="Hello there" #string
isPythonInteresting=True #boolean

fruits=["apple","banana","mango"] #LIST

cars=("bmw","mercedes","toyota","v8") #TUPLE

countries={"Kenya","Tanzania","Uganda"} #SET

student={
    "firstname":"Gold",
    "age":19,
    "course":"MIT",
    "nationality":"Kenyan"
}
#THIS IS A DICTIONARY

print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])

# DETERMINING DATA TYPE
print(type(isPythonInteresting))
print(type(cars))

#TYPE CASTING (CONVERTING ONE DATA TYPE TO ANOTHER

print(int(num))
print(float(number))
print(type(convertnum))


