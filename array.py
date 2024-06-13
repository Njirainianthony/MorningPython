courses=["MIT", "cyber security", "data science"]
print(courses)
#ACCCESSING AN ELEMENT IN AN ARRAY
print(courses[0])
print(courses[1])

#ADDING A NEW ELEMENT IN AN ARRAY
courses.append("Android development")
print(courses)

#DELETING AN ELEMENT IN AN ARRAY
courses.remove("cyber security")
print(courses)

#LOOPING THROUGH AN ARRAY
for course in courses:
    print(course)


