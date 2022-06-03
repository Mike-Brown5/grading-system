import pandas,os,csv

data = pandas.DataFrame(columns=["Student's ID","Name","Midterm Grade","Classwork Grad"]) # creating the headers for the data file with the columns for the requested variables
# data.loc[:, ~data.columns.str.contains('Unnamed^')]

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
\n8-Exit""") #the requsetd options

user = input("Choose a number that determine one of the options above please:")

fileRead = open("./data.csv",newline="")

if user=="1":
    # reader = csv.reader(fileRead)
    # for row in reader:
    #     print(row)
    print(pandas.read_csv(fileRead))
elif user=="2":
    total_students = len(pandas.read_csv(fileRead))
    print(f"Number of students is {total_students}")
elif user=="3":

    next(csv.reader(fileRead))
    scoresL = []
    for c in csv.reader(fileRead):
        scores =int(c[3])+ int(c[4]) 
        
        # print(int(row[3])+ int(row[4]))
        scoresL.append(scores)

    df = pandas.read_csv("./data.csv")
    df["Final scores"] = scoresL
    df.to_csv("Scores.csv")
    # print(scoresL)
    newFile = open("./Scores.csv",newline="")
    for i in csv.reader(newFile):
        print(i[3]," ",i[6])
    # print(pandas.read_csv(newFile , index_col=0))

    # print(pandas.read_csv(newFile))
newFile = open("./newCSV.csv",newline="")
if user=="4":
    next(csv.reader(newFile))
    Grades = []
    grade = ""
    for c in csv.reader(newFile):
        if 100>=int(c[5])>=90:
            grade = "A"
            Grades.append(grade)
        elif 90>=int(c[5])>=75:
            grade="B"
            Grades.append(grade)
        elif 75>=int(c[5])>=60:
            grade="C"
            Grades.append(grade)
        elif 60>=int(c[5])>=50:
            grade="D"
            Grades.append(grade)
        else:
            grade="F"
            Grades.append(grade)
    df = pandas.read_csv("./data.csv")
    df["Grades"] = Grades
    df.to_csv("Grading.csv")
    gradingF = open("./Grading.csv",newline="")
    for i in csv.reader(gradingF):
        print(i[2]," ",i[3]," ",i[6])
