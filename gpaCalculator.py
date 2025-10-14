from time import sleep

def calculateGPA(gradeList: list):
    sumOfGrades = sum(gradeList)
    gradeCount = len(gradeList)
    return sumOfGrades / gradeCount
print("Welcome to the GPA calculator! Make sure to input your grades in the 4.0 scale!")

while True:
    try:
        gradeAmount = int(input("How many grades do you have?\n> "))
        break
    except:
        print("Please enter a proper value for how many grades you have") 
grades = []
for gradeCount in range(1, gradeAmount+1): # +1 allows for input statements to be formatted more clearly
    while True:
        try:
            grade = float(input(f"What is your grade for class {gradeCount}?\n> "))
            break
        except:
            print("Please enter a number, and do not include any symbols or letters")

    while True:
        if grade > 4 or grade < 0:
            print("Please enter a number between 0 and 4")
            grade = float(input(f"What is your grade for class {gradeCount}?\n> "))
        else:
            break
    
    grades.append(grade)

gpa = calculateGPA(grades)
print("Calculating...")
sleep(2)
print(f"Your current GPA is {gpa}!")
sleep(3)
print(f"Your GPA for your first two classes is {calculateGPA(grades[:2])}")
sleep(3)
print(f"Your GPA for your last two classes is {calculateGPA(grades[-2:])}")


# grades = input("Please enter your grades, in the format grade1, grade2, grade3, etc. Please enter them in a 4.0 format\n> ")
# grades = grades.split(",")

# while True:
#     try:
#         grades = [float(grade) for grade in grades]
#         break
#     except:
#         print("Please enter correct values for each grade. Make sure they have no letters in them")
#         grades = input("> ")
#         grades = grades.split(",")

# validGrades = True if all([True for grade in grades if abs(grade) == grade and (grade > 0 and grade < 4)]) else False
# while not validGrades:
#     print("You either have negative values in your grade list or your grades exceeed the 4 point scale. Please enter them again")
#     grades = input("> ")
#     grades = grades.split(",")
#     validGrades = True if all([True for grade in grades if abs(grade) == grade and (grade > 0 and grade < 4)]) else False


# gpa = calculateGPA(grades)
