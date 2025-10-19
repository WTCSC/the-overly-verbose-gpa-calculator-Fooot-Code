from time import sleep

def calculateGPA(gradeList: list):
    """
    Returns GPA value from grade list by taking the sum of the grades given, and
    dividing it by the number of grades in the list.
    """
    sumOfGrades = sum(gradeList)
    gradeCount = len(gradeList)
    return sumOfGrades / gradeCount
print("Welcome to the GPA calculator! Make sure to input your grades in the 4.0 scale!")

# Grade amount/how many classes a person has
while True:
    try:
        gradeAmount = int(input("How many grades do you have?\n> "))
        break
    except:
        print("Please enter a proper value for how many grades you have") 


while gradeAmount <= 0:
    print("Please enter a non-negative, non-zero value")
    while True:
        try:
            gradeAmount = int(input("> "))
            break
        except:
            print("Please enter a proper value for how many grades you have") 
        

# Gathers grades from each class, ensuring correct data format
grades = []
for gradeCount in range(1, gradeAmount+1): # +1 allows for input statements to be formatted more clearly
    while True:
        try:
            grade = float(input(f"What is your grade for class {gradeCount}?\n> "))
            break
        except:
            print("Please enter a number, and do not include any symbols or letters")

    while grade > 4 or grade < 0:
        print("Please enter a number between 0 and 4")
        try:
            grade = float(input("> "))
            break
        except:
            print("Please enter a number, and do not include any symbols or letters")
    
    grades.append(grade)

# Calculates overall, first semester, and second semester GPAs
gpa = calculateGPA(grades)
print("Calculating...")
sleep(2)
print(f"Your current GPA is {round(gpa, 2)}!")
sleep(3)
gradeAmount = len(grades)

# If odd, first semester gets the extra class
mid = (gradeAmount + 1) // 2  

firstSemesterGPA = calculateGPA(grades[:mid])
lastSemesterGPA = calculateGPA(grades[mid:])

consistent4 = True if firstSemesterGPA == 4 and lastSemesterGPA == 4 else False # Has a 4.0 through both semesters.


print(f"Your GPA for your first semester is {round(firstSemesterGPA, 2)}!")
sleep(3)
print(f"Your GPA for your last semester is {round(lastSemesterGPA, 2)}!")
sleep(3)
if firstSemesterGPA > lastSemesterGPA:
    print(f"You didn't improve your GPA from last semester! You must improve it now!")
elif lastSemesterGPA > firstSemesterGPA:
    print(f"Good job, your GPA has improved between semesters!")
elif consistent4:
    print(f"WOW! You are really good at school, great job maintaining a 4.0 throughout both semesters!")
else: # Got the same grade they did last semester
    print(f"You have not improved on your GPA yet.")

sleep(3)

if not consistent4:

    # Asks if they would like to maintain or improve their GPA, and then validates this answer
    maintainOrImprove = input("Would you like to maintain or improve your GPA?\n> ")
    while maintainOrImprove.lower() not in ["maintain", "improve"]:
        print('Please type either "maintain" or "improve"')
        maintainOrImprove = input("> ")

    if maintainOrImprove.lower() == "maintain":
        if gpa < 2:
            print(f"Okay, but I would consider improving your GPA, a {round(gpa, 1)} is not very good.") # Rounds to 1 decimal for emphasis
        else:
            print(f"Sounds good, good work on your GPA!")

    elif maintainOrImprove.lower() == "improve":

        # Prompts the user for a target GPA and ensures it is a valid input
        while True:
            try:
                targetGPA = float(input("Good choice! What is your target GPA? \n> "))
                break
            except:
                print("Please enter a number with valid characters")
        
        while targetGPA > 4.0 or targetGPA <= gpa:
            print("Please do not enter a negative number, a number below your current GPA, or a number above 4!")
            try:
                targetGPA = float(input("> "))
                break
            except:
                print("Please enter a number with valid characters")

        # Creates the person's new grades with the updated 4.0
        newGrades = grades.copy()
        lowestGradeIndex = newGrades.index(min(newGrades))
        newGrades[lowestGradeIndex] = 4.0 # Selects the lowest grade in the grades, and makes it a 4.0
        print(f"If you were to improve your grade in Class {lowestGradeIndex + 1}, your grades would look like this:")
        sleep(2)
        
        # Displays their new class grades with the updated grade
        for classNumber, grade in enumerate(newGrades, 1):
            print(f"    Class {classNumber}: {grade}")
            sleep(.5)

        # Calculates their new GPA, and tells them if they can improve it or not.
        newGPA = calculateGPA(newGrades)
        print(f"New GPA: {round(newGPA, 2)}")
        if newGPA >= targetGPA:
            print(f"Congrats! If you improve class {lowestGradeIndex + 1}, then you will reach your goal GPA of {round(targetGPA, 2)}.")
            sleep(3)
            print("Time to start working on improving your grade :>")
            
        else:
            print(f"Sadly, if you improve your grade in class {lowestGradeIndex + 1} to a 4, you still won't achieve an average GPA of {round(targetGPA, 2)}")
            sleep(3)
            print("In this case, you will have to improve multiple grades.")

sleep(3) # buffer give time to read last printed message