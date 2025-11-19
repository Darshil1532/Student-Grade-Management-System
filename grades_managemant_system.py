# Student Grade Management System
# By Darshil Jha
def AddStudent():
    name = input("Enter the name of the student: ")
    marks = int(input("Enter the marks of the student: "))
    dict[name] = marks

def DeleteStudent():
    name = input("Enter the name u want to delete: ")
    dict.pop(name)

def ViewStudent():
    for i in dict:
            print("Student Name: ",i,"  |  Marks: ",dict[i])

def makegraph():
    import matplotlib.pyplot as plt

    names = list(dict.keys())
    marks = list(dict.values())

    if e == 1:
        plt.bar(names , marks)
        plt.xlabel('Students')
        plt.ylabel('Marks')
        plt.title('Student Marks Bar Graph')
        plt.show()
    
    elif e == 2:
        plt.pie(marks , labels=names , autopct='%1.1f%%')
        plt.title('Student Marks Pie Chart')
        plt.show()
    
    elif e == 3:
        plt.scatter(names , marks)
        plt.xlabel('Students')
        plt.ylabel('Marks')
        plt.title('Student Marks Scatter Plot')
        plt.show()
    
    else:
        print("Please enter a valid graph type.")



print("Welcome to the Student Grade Management System: ")
print("--------------------------------------------------------------")

dict = {}                    
for i in range(100):

    todo = int(input("What u want to do:\n\t1. Add Student\n\t2. Update Student\n\t3. Delete Student\n\t4. View Student\n\t5. Make the graph\n\t6. Some more option\n\t7. Exit\n-->"))
    if todo == 1 or todo == 2:
        q = int(input("Enter how many students u want to add: "))
        for w in range(q):
            AddStudent()
    
    elif todo == 3:
        DeleteStudent()
    
    elif todo == 4:
        ViewStudent()
    
    elif todo == 5:
        e = int(input("Enter which type of graph u want:\n\t1. Bar Graph\n\t2. Pie Chart\n\t3. Scatter Plot\n-->"))
        makegraph() 

    elif todo == 6:
        r = int(input("Enter what u want to do:\n\t1. View Topper marks\n\t2. View Average Marks\n\t\n-->"))
        if r == 1:
            maxmarks = max(dict.values())
            print("Topper have marks: ", maxmarks)
        
        elif r == 2:
            average = sum(dict.values()) / len(dict)
            print("The average Marks of the class is: ", average)

    elif todo == 7:
        break

    else :

        print("Enter the correct value: ")
