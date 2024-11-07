#Name: Niklaus Guenther W0414211
#Program: Tech check 4 grade calculator

def calculateNumericGrade(courseName):
    letterToPoints = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    modifyGrade = {'+': 0.3, '-': -0.3, '': 0.0}
    letter = input(f"Please enter a letter grade for {courseName}: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")
    baseGrade = letterToPoints.get(letter)
    adjustment = modifyGrade.get(modifier)
    numericGrade = baseGrade + adjustment
    
    if numericGrade > 4.0:
        numericGrade = 4.0
    elif numericGrade < 0.0:
        numericGrade = 0.0
    return numericGrade

def main():
    
    print("Grade Point Average Calculator")
    courses = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"]
    totalGradePoints = 0.0 
    
    for course in courses:
        numericGrade = calculateNumericGrade(course) 
        print(f"The numeric value for {course} is: {numericGrade:.1f}")  
        totalGradePoints += numericGrade  

    gpa = totalGradePoints / len(courses)
    print(f"Your grade point average for the semester is: {gpa:.1f}")

if __name__ == "__main__":
    main()