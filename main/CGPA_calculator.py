#!/usr/bin/python3

import pandas as pd

#Function to Calculate GPA
def calculate_gpa():
    tcu = sum(cu)
    wp = [a*b for a,b in zip(cu,gp)]
    twp = sum(wp)
    gpa = twp/tcu
    return round(gpa,2)

#Function to Calculate CGPA
def calculate_cgpa():
    cgpa =  (gpa+prev_cgpa)/2   
    if prev_cgpa == 0:
        cgpa = (gpa+gpa)/2	
    return round(cgpa,2)

    # tcu - Total Course Unit, wp - Weighted Point
    # twp - Total Weighted Point, gpa - Grade Point Average
    # cpga - Cummulative Grade Point Average

# Function that displays information on Table
def table():
    gt = list(zip(CourseCodes,cu,grade))
    df = pd.DataFrame(gt, columns=['Course Code', 'Course Unit', 'Grade'])
    df.index = df.index+1
    print(df.to_markdown())

    # Zipped the list altogether so as to be able to call it via a DataFrame


# User-defined number of Courses

prev_cgpa = eval(input("Enter Current CGPA: "))
#User inputs old CGPA 

while True:
	   try:
	       CourseNum = int(input("Enter Number Of Courses Attempted: "))
	       break
	   except ValueError:
	       print("Invalid input. Please enter a valid number.")

# empty list to accept User Variables
CourseCodes = []
cu = []
gp = []
grade = []
# cu - Course Unit, gp - Grade Point

print("====================")
print("====================")

#Running it through a loop to acquire information
for i in range(CourseNum):
    code = input("Enter Course Code{}: ".format(i+1))
    CourseCodes.append(code)
    while True:
        try:
            unit = int(input("Enter Course Unit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    cu.append(unit)
    while True:
        point = (input("Enter Grade (from 'A - F'): ")).upper()
        if point in ["A","B","C","D","E","F"]:
            break
        print("Invalid input. Please enter a valid grade.")
    if point == "A":
        gp.append(5.0)
        grade.append(point)
    if point == "B":
        gp.append(4.0)
        grade.append(point)
    if point == "C":
        gp.append(3.0)
        grade.append(point)
    if point == "D":
        gp.append(2.0)
        grade.append(point)
    if point == "E":
        gp.append(1.0)
        grade.append(point)
    if point == "F":
        gp.append(0.0)
        grade.append(point)
    print("====================")

# Calling Our functions to produce results
gpa = calculate_gpa()
cgpa = calculate_cgpa()
table()
print("====================")
print("====================")
print("Semester's GPA:", gpa)
print("====================")
print("CGPA:", cgpa)

    







