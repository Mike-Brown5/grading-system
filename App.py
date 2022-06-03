import pandas,os,csv,numpy #the required modules to run the code (PS. you can install these modules by runing the commands[pip install "module_name"] but you have to make sure you have pip installed on your system first)

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
\n8-Exit""") #the requsetd options

user = input("Choose a number that determine one of the options above please:") # getting the user input

DataFile = open("./data.csv",newline="") #accessing the data file and store it's content in a variable

if user=="1":# setting a condition when the user choose 1
    print(pandas.read_csv(DataFile)) #showing all the data

elif user=="2":#setting a condition when the user choose 2
    total_students = len(pandas.read_csv(DataFile)) #getting the number of students in the file based on the number of rows
    print(f"Number of students is {total_students}") #printing out the number of students

elif user=="3":#setting a condition when the user choose 3

    next(csv.reader(DataFile))
    scoresL = []
    for c in csv.reader(DataFile):
        scores =float(c[3])+ float(c[4]) 
        
        # print(int(row[3])+ int(row[4]))
        scoresL.append(scores)

    df = pandas.read_csv("./data.csv")
    df["Final scores"] = scoresL
    df.to_csv("data.csv")
    # print(scoresL)
    newFile = open("./data.csv",newline="")
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
if user=="5":
    next(csv.reader(newFile))

    score_values = []

    for c in csv.reader(newFile):
        score_values.append(int(c[4]))

    print(f"""The Maximum Score is:{max(score_values)}\n
    Minimum score is:{min(score_values)}\n
    Scores Average is:{numpy.array(score_values).mean()}\n
    Standard deviation is :{numpy.array(score_values).std()}\n
    Scores variance is :{sum((x-numpy.array(score_values).mean())**2 for x in score_values) / len(score_values)} """)

gradingF = open("./Grading.csv",newline="")

if user=="6":
    next(csv.reader(newFile))
    for c in csv.reader(gradingF):
        if c[6]=="A":
            print(c[3]," ", c[6])

if user=="7":
    word = input("Enter the full name or at leasst the first 2 letters of the student's name: ").lower()
    next(csv.reader(gradingF))

    for row in csv.reader(gradingF):

        if word == str(list(row[3])[0]+list(row[3])[1]).lower():
            print(row)
        if word == row[3].lower():
            print (row)

if user=="8":
    print("Tnahks for using our grading system..")
    exit()
