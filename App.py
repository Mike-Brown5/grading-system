from ctypes.wintypes import FLOAT
from platform import uname
from tokenize import Ignore
import pandas,os,csv,numpy #the required modules to run the code (PS. you can install these modules by running the commands[pip install "module_name"] but you have to make sure you have pip installed on your system first)

data = pandas.DataFrame(columns=["Student's ID","Name","Midterm Grade","Classwork Grad"]) # creating the headers for the data file with the columns for the requested variables

if os.path.exists("./data.csv") ==False: # checking the data file already exist on the current directory or not
    data.to_csv("./data.csv") #crating the csv data file in case it doesn't exist


print("***Pleas choose one of the following options****\n") #welcoming message

print("""1-Show Data
\n2-Number of students
\n3-Compute final scores
\n4-compute and show grades
\n5-Column statistics
\n6-Show Grade A students
\n7-Search by student's name
\n8-Exit""") #the requested options

user = input("Choose a number that determine one of the options above please:") # getting the user input

DataFile = open("./data.csv",newline="") #accessing the data file and store it's content in a variable

if user=="1":# setting a condition when the user choose 1
    print(pandas.read_csv(DataFile)) #showing all the data

elif user=="2":#setting a condition when the user choose 2
    total_students = len(pandas.read_csv(DataFile)) #getting the number of students in the file based on the number of rows
    print(f"Number of students is {total_students}") #printing out the number of students

elif user=="3":#setting a condition when the user choose 3

    next(csv.reader(DataFile))#skipping the headers

    scoresL = [] # creating a list to store the values of the total scores

    for c in csv.reader(DataFile):#iterating through the rows on file and assigning them to c variable
        scores =float(c[3])+ float(c[4]) #calculating the scores based on the formula midterm_grade+ classwork_grade
        
        # print(int(row[3])+ int(row[4]))
        scoresL.append(scores) #appending the calculated values to the totalScores Empty list

    df = pandas.read_csv("./data.csv")#accessing the values of the data file
    df["Final scores"] = scoresL #creating a new column and assign the calculated values of the scores to it's rows
    df.to_csv("data.csv",index=False)#adding the new column to the data file

    scoreFile = open("./data.csv",newline="") #accessing the data file after the changes
    for i in csv.reader(scoreFile):
        print(i[2]," ",i[5])
    # print(pandas.read_csv(scoreFile , index_col=0))

    # print(pandas.read_csv(scoreFile))
scoreFile = open("./data.csv",newline="")
if user=="4":
    next(csv.reader(scoreFile))
    Grades = []
    grade = ""
    for c in csv.reader(scoreFile):
        if 100>=float(c[5])>=90:
            grade = "A"
            Grades.append(grade)
        elif 90>=float(c[5])>=75:
            grade="B"
            Grades.append(grade)
        elif 75>=float(c[5])>=60:
            grade="C"
            Grades.append(grade)
        elif 60>=float(c[5])>=50:
            grade="D"
            Grades.append(grade)
        else:
            grade="F"
            Grades.append(grade)
    df = pandas.read_csv("./data.csv")
    df["Grades"] = Grades
    df.to_csv("data.csv",index=False)
    gradingF = open("./data.csv",newline="")
    for i in csv.reader(gradingF):
        print(i[1]," ",i[2]," ",i[6])
if user=="5":
    next(csv.reader(scoreFile))

    score_values = []

    for c in csv.reader(scoreFile):
        score_values.append(float(c[5]))

    print(f"""The Maximum Score is:{max(score_values)}\n
    Minimum score is:{min(score_values)}\n
    Scores Average is:{numpy.array(score_values).mean()}\n
    Standard deviation is :{numpy.array(score_values).std()}\n
    Scores variance is :{sum((x-numpy.array(score_values).mean())**2 for x in score_values) / len(score_values)} """)

gradingF = open("./data.csv",newline="")

if user=="6":
    next(csv.reader(scoreFile))
    for c in csv.reader(gradingF):
        if c[6]=="A":
            print(c[2]," ", c[6])

if user=="7":
    word = input("Enter the full name or at least the first 2 letters of the student's name: ").lower()
    next(csv.reader(gradingF))

    for row in csv.reader(gradingF):

        if word == str(list(row[2])[0]+list(row[2])[1]).lower():
            print(row)
        if word == row[2].lower():
            print (row)

if user=="8":
    print("Thanks for using our grading system..")
    exit()
