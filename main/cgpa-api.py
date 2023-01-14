from fastapi import FastAPI, JSONResponse

import pandas as pd

app = FastAPI()

@app.post("/calculate_gpa_cgpa")

def calculate_gpa_cgpa(level:int, sem:int, prev:float, CourseNum: int, CourseCodes: List[str], cu: List[int], grade: List[str]) -> dict:

    #Function to Calculate GPA

    def calculate_gpa():

        tcu = sum(cu)

        wp = [a*b for a,b in zip(cu,gp)]

        twp = sum(wp)

        gpa = twp/tcu

        return round(gpa,2)

    #Function to Calculate CGPA

    def calculate_cgpa():

        if level == 100:

            if sem == 1:

                cpga = 0

            if sem == 2:

                cpga = (prev + gpa)/2

                return round(cpga,2)

        if level == 200:

            if sem == 1:

                cpga =((prev *2) + gpa)/3

                return round(cpga,2)

            if sem == 2:

                cpga = ((prev*3) + gpa)/4

                return round(cpga,2)

        if level == 300:

            if sem == 1:

                cpga =((prev *4) + gpa)/5

                return round(cpga,2)

            if sem == 2:

                cpga = ((prev*5) + gpa)/6

                return round(cpga,2)

        if level == 400:

            if sem == 1:

                cpga =((prev *6) + gpa)/7

                return round(cpga,2)

            if sem == 2:

                cpga = ((prev*7) + gpa)/8

                return round(cpga,2)

        if level == 500:

            if sem == 1:

                cpga =((prev *8) + gpa)/9

                return round(cpga,2)

            if sem == 2:

                cpga = ((prev*9) + gpa)/10

                return round(cpga,2)

    # tcu - Total Course Unit, wp - Weighted Point

    # twp - Total Weighted Point, gpa - Grade Point Average

    # cpga - Cummulative Grade Point Average

    # Function that displays information on Table

    def table():

        gt = list(zip(CourseCodes,cu,grade))

        df = pd.DataFrame(gt, columns=['Course Code', 'Course Unit', 'Grade'])

        df.index = df.index+1

        return df.to_markdown()

    # acquire level

while True:

    try:

        level = int(input("Enter Your Level: "))

        if level < 100 or level > 500 or level not in (100,200,300,400,500):

            raise ValueError("Invalid input. Please enter a level between 100 - 500.")

        break

    except ValueError as e:

        print(e)

   # acquire sem

while True:

    try:

        sem = int(input("Enter Semester: "))

        if sem > 2 or sem < 1:

            raise ValueError

        break

    except ValueError:

        print("Invalid input. Please enter a valid semester between 1 and 2.")

while True:

    try:

        prev = float(input("Enter Current CGPA: "))

        break

    except ValueError:

        print("Invalid input. Please enter a number.")

print("====================")

while True:

    try:

        CourseNum = int(input("Enter Number Of Courses Attempted: "))

        break

    except ValueError:

        print("Invalid input. Please enter a valid number.")

print("====================")

# empty list to accept User Variables

CourseCodes = []

cu = []

gp = []

grade = []

# cu - Course Unit, gp - Grade Point

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

        gp.append(5)

        grade.append("A")

    elif point == "B":

        gp.append(4)

        grade.append("B")

    elif point == "C":

        gp.append(3)

        grade.append("C")

    elif point == "D":

        gp.append(2)

        grade.append("D")

    elif point == "E":

        gp.append(1)

        grade.append("E")

    elif point == "F":

        gp.append(0)

        grade.append("F")

gpa = calculate_gpa()

cgpa = calculate_cgpa()

table_data = table()

return {"GPA":gpa, "CGPA":cgpa, "table_data":table_data}
