
#importing libraries
from tkinter import *
import tkinter as tk
import sqlite3
import statistics

conn = sqlite3.connect('database8.db') #creates the file
#conn =sqlite3.connect(':memory:') #will create a fresh database every time. Useful for testing

cur = conn.cursor() # cursor that allows you to run sql commands

cur.execute("""CREATE TABLE IF NOT EXISTS class(  

         ID INTEGER PRIMARY KEY,
         first TEXT,
         last TEXT,
         mark INTEGER,
         target_grade TEXT,
         percentage INTEGER,
         grade TEXT
         

)""") #creating table with name 'class' and fields: ID, first, last,mark,target_grade,percentage
conn.commit() #this commits the current transaction

##cur.execute ("DELETE FROM class ")
##conn.commit()






LARGE_FONT = ("Verdana", 12) # specifying the font




class baseline (tk.Tk):  #basline is inheriting .Tk() class. Give us access to widgets and stuff

    def __init__(self, *args, **kwargs): #*args - used to pass a variable number of arguments to a function
        
        tk.Tk.__init__(self, *args, **kwargs) # **kwargs - used to pass a keyworded, variable length argument list
        container = tk.Frame(self) # self represents the instances of a class - attributes and methods

        container.pack(side = "top", fill = "both", expand = True)
        #container.configure(background = "Light Blue")

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, Submit, ProceedToAnalysis):

            frame = F(container,self)

            self.frames[F] =frame
            
            frame.grid(row =0, column = 0, sticky ="nsew") #sticky does alignment +strech (north, south, east west)

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() #riases the frame to the top




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Mark Analysis", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)

        #place the labels
        Label(self, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady =5)


        Label(self, text = "Last Name: ").grid(row =2, column = 0, padx = 10, pady =5)

        Label(self, text = "Mark: ").grid(row =3, column = 0, padx = 10, pady =5)


        Label(self, text = "Target Grade: ").grid(row =4, column = 0, padx = 10, pady =5)



        #place the text entry fields
        
        global firstname
        global lastname
        global mark__
        global targetgrade
        
        firstname = Entry(self, width = 15, bg = "white")
        firstname.grid(row = 1, column=1, padx =5, pady = 5)

        lastname = Entry(self, width = 15, bg = "white")
        lastname.grid(row = 2, column=1, padx =5, pady = 5)

        mark__ = Entry(self, width = 15, bg = "white")
        mark__.grid(row = 3, column=1, padx =5, pady = 5)

        targetgrade = Entry(self, width = 15, bg = "white")
        targetgrade.grid(row = 4, column=1, padx =5, pady = 5)


        #Buttons to navigate


        
        button1 = tk.Button(self, text = "Submit",
                            command =  self.insertintosql)
                            
        button1.grid(row = 8 , column= 0)



        button2 = tk.Button(self, text = "Proceed",
                            command = lambda:controller.show_frame(ProceedToAnalysis) )
        button2.grid(row = 8, column = 1)


#creating a function that inserts into database

        def insertintosql(self):
                  '''inserting values into the database'''

         global firstname
         global lastname
         global mark__
         global targetgrade


         first = firstname.get()
         last= lastname.get()
         mark = mark__.get()
         target_grade = targetgrade.get()
         percentage =0
         grade = "Not yet declared"

         #calling the function
         insertintosql(first,last,mark,target_grade,percentage,grade)


         firstname.delete(0,END) # clearing the entry after the user has inputted data
         lastname.delete(0,END)
         mark__.delete(0,END)
         targetgrade.delete(0,END)
         firstname.focus_set()
    




class Submit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Entry Submitted", font = LARGE_FONT)
        label.grid(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda:controller.show_frame(StartPage) )
        button1.grid(row = 8 , column= 0)

        button2 = tk.Button(self, text = "Proceed",
                            command = lambda:controller.show_frame(ProceedToAnalysis) )
        button2.grid(row = 8, column = 1)

        

class ProceedToAnalysis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Analysis", font = LARGE_FONT)
        label.grid(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda:controller.show_frame(StartPage) )
        button1.grid(row = 7 , column= 0)

        button2 = tk.Button(self, text = "Submit",
                            command = lambda:controller.show_frame(Submit) )
        button2.grid(row = 7, column = 1)






        
#Defining functions that will edit the database
        
def get_students_by_name(first,last): #function to retrieve student
    with conn:
            cur.execute('SELECT * FROM class WHERE last = :last AND first =:first',{'last':last, 'first': first})
            print(cur.fetchall())
            

def update_mark(first,last, mark): #function to update mark
    with conn:
        cur.execute(""" UPDATE class SET mark = :mark
        WHERE first = :first AND last = :last""",
        {'first': first, 'last': last, 'mark' : mark})

def update_target_grade(first,last,target_grade): #function to update target grade
    with conn:
        cur.execute(""" UPDATE class SET target_grade = :target_grade
        WHERE first = :first AND last = :last""",
        {'first':first, 'last':last, 'target_grade' : target_grade})

def remove_student (first,last): #function to remove student
    with conn:
        cur.execute("DELETE from class WHERE first = :first AND last = :last",
                  {'first':first, 'last':last})


##cur.execute ("DELETE FROM class ")
##conn.commit()

##choice = True
##while choice ==True:
##
##    choice = int(input('Would you like to edit the data (1) or proceed to analysis(2)'))
##
##            
##    if choice ==1:  #shows the user all the records in the database
##            cur.execute("SELECT * FROM class") 
##            students = cur.fetchall()
##            for r in students:
##                print("")
##                print(r)
##            print(
##                "*"*50, "\n")
##            
##            
##            edit = True
##            while edit  == True: #list of options they can edit from
##                    edit = int(input("""Look at database (1) \nInsert Data (2) \nGet Student data (3) \nUpdate Mark (4) \nUpdate Target Grade (5) \nDelete Student (6)\nGo back to main menu (7)"""))
##
##                    if edit == 1: #looks at database
##                        print("")
##                        cur.execute("SELECT * FROM class")
##                        students = cur.fetchall()
##
##                        print( """
##
##
##                                    """)
##                        choice =True 
##                        loop = False
##                            
##                    elif edit == 2: #inserting a new record
##                        choice= False
##                        loop = True
##                        while loop == True:
##                                    
##                                
##                                    
##
##                                first = True  #validation - if 'first' contains non-alphabetical characters, ask the question again until they give a valid answer
##                                while first == True:
##
##                                    first = input("First Name: ").title()
##                                    if first.isalpha() != True:
##                                        #print(first.isalpha)
##                                        print("Must be using alphabetical characters")
##                                        first = True
##                                    
##                                
##
##                                last = True
##                                while last == True:
##                                    last =input("Last name: ").title()
##                                    if last.isalpha()!= True:
##                                            print("Must be using alphabetical characters")
##                                            last = True
##                                            
##                                            
##                                        
##                                mark = int(input("Mark:  "))
##                                while True:
##                                        try:
##                                                mark = int(input("Mark:  "))
##                                        except ValueError:
##                                                print("Has to be a valid number")
##                                                continue
##                                        else:
##                                                break
##                                        
##                                                
##
##                                target_grade = True
##                                while target_grade ==True:
##                                        target_grade = input("Target Grade: ").title()
##                                        if target_grade == "A*" or target_grade == "A" or target_grade == "B" or target_grade == "C" or target_grade == "D" or target_grade == "E" or target_grade == "F" or target_grade == "U":
##                                                continue
##                                        else:
##                                               print("Not a valid grade")
##                                               target_grade = True
##                                               
##                                percentage =0
##                                grade = "Not yet declared"
##
##                                    
##                                cur.execute("INSERT INTO class (first, last, mark, target_grade, percentage,grade) VALUES (?,?,?,?,?,?)",(first,last,mark,target_grade,percentage,grade))
##                                conn.commit() #inserting the values in the database
##                            
##
##                                repeat = True
##                                while repeat == True:
##                                    repeat = int(input("Would You like to add another student to the class? (1)Yes  (2)No " )) #adding more records
##
##                                    if repeat == 1 :
##                                            repeat = False
##                                            loop = True
##                                            
##                                    elif repeat == 2:
##                                            loop = False
##                                            choice =True
##                                    else:
##                                            print("Invalid response")
##                                            repeat = True
##
##                        
##                    elif edit == 3:
##                            first = input("First name: ").title()
##                            last = input("Last name: ").title()
##                            get_students_by_name(first,last) #function to get students is called
##                            print("")                           
##
##
##                    elif edit ==4:
##                            first = input("First name: ").title()
##                            last = input("Last name: ").title()
##                            mark = int(input("Updated Mark: "))
##                            update_mark(first, last, mark) #function to update mark is called
##                            print("")
##                    elif edit ==5:
##                            first = input("First name: ").title()
##                            last = input("Last name: ").title()
##                            target_grade = input("Updated Target Grade: ").title()
##                            update_target_grade(first, last, target_grade) #function to update target grade is called
##                            print("")
##
##                            
##                    elif edit == 6:
##                    
##                            first = input("First name: ").title()
##                            last = input("Last name: ").title()
##                            remove_student(first, last) #function to remove student is called
##                            print("")
##
##                    elif edit ==7:
##                            edit = True
##
##
##
##                    elif edit != 1 or edit != 2 or edit != 3 or edit != 4 or edit != 5 or edit != 6 or edit!=7: #if user presses an invalid key, the program asks them again
##                           print("")
##                           print("This is not an option.")
##                           print("")
##                           edit = True
##
##                    else:
##                        print("That is not an option.")
##                        edit =True
##
##    elif choice ==2:
##            
##            
##            cur.execute("SELECT (mark) FROM class")
##            result = cur.fetchall()
##            count= 0
##            a = [] #the students mark in a list
##          
##            for i in result:
##                    count += 1
##                    a.append(i[0])
##
##            a.sort()
##            max_mark = a[-1] #finding the largest number in the list
##            #print(max_mark)
##
##
##            
##
##        
##
##            asking_for_total_mark = False
##
##            while asking_for_total_mark != True: #checking to see that the total mark is not less than a student's mark.
##
##                    total_mark = int(input("What is the total mark for this test?: "))
##                    print("")
##
##
##
##                    if total_mark < max_mark:
##                            print("Error - Total mark can not be less than student's mark")
##                            #asking_for_total_mark =True
##
##                    else:
##                            asking_for_total_mark = True
##                
##                    
##
##
##            cur = conn.cursor()  #######Mia
##            cur.execute("SELECT * FROM class")
##            mark_as_per = cur.fetchall()
##            #print (mark_as_per)   ############################### Mia
##
##            b= []
##            for i in mark_as_per:  #changing the marks into a perentage value then appending it to a list
##                    mark = (i[3])
##                    percentage = round(((mark/total_mark)*100),1)
##                    b.append(percentage)
##                    #print(percentage)
##            #print(b) #list of raw marks
##
##            for i, val in enumerate(b): #goes through each primary key and updates the percentage field
##                    #print("UPDATE class SET percentage = (?) WHERE ID = (?)",(val,(i+1),))
##                    cur.execute("UPDATE class SET percentage = (?) WHERE ID = (?)",(val,(i+1),))
##            conn.commit()
##
##
###analysis:
##            
##
##            avg_mark = round(sum(a)/count,1)  #calculating the average mark
##            print("Avergage mark: ", avg_mark)
##
##            avg_percentage = round(sum(b)/count,1) #calculating the average percentage
##            
##            print("Average percentage: ",avg_percentage,"%" )
##
##            #median
##
##            def Median (a):  
##                _len = a.sort()
##                _len = len(a)
##                median = 0
##                if _len% 2 == 0:
##                    median = float((a[(_len //2) -1] + a[(_len // 2 )])/2) #index starts from 0.
##                    print("Median: ",median)
##
##                else:
##                    median = a[_len//2]
##                    print("Median: ",median)
##            Median(a)
##
##
##            mode = max(set(a), key=a.count)
##            print("Mode: ",mode)
##
##            #range
##
##            range_val = max(a) - min(a)
##            print("Range: ",range_val)
##
##
##            #standard deviation
##
##            print("Standard deviation: ", round(statistics.stdev(a),1))
##
##
##
##
##    
##
##            #Entering Grade Boundaries
##
##            print("\nPlease Enter Grade Boundaries for this test: ")  
##            
##            while True:
##                                try:
##                                        a_star = int(input("\nRaw mark to get A*: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##                                        continue
##                                else:
##                                        break
##                            
##                    
##            while True:
##                                try:
##                                        a= int(input("Raw mark to get A: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##                                        continue
##                                else:
##                                        break
##
##
##
##                                                        
##            while True:
##                                try:
##                                        b = int(input("Raw mark to get B: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##                                        continue
##                                else:
##                                        break
##
##
##                                        
##            while True:
##                                try:
##                                        c = int(input("Raw mark to get C: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##                                        continue
##                                else:
##                                        break
##                                        
##
##            while True:
##                                try:
##                                        d = int(input("Raw mark to get D: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##                                        continue
##                                else:
##                                        break
##                                        
##
##            while True:
##                                try:
##                                        e = int(input("Raw mark to get E: "))
##                                except ValueError:
##                                        print("Has to be a valid number")
##
##                                        continue
##                                else:
##                                        break
##
##
##
##
## 
###sql case statement: if mark is not within the grade parameters, do one thing, if not do the other thing
##
##            sql = '''UPDATE class   
##                         SET grade = CASE 
##                                         WHEN mark >= :a_star_prm THEN 'A*'
##                                         WHEN mark >= :a_prm AND mark < :a_star_prm THEN 'A'
##                                         WHEN mark >= :b_prm AND mark < :a_prm THEN 'B'
##                                         WHEN mark >= :c_prm AND mark < :b_prm THEN 'C'
##                                         WHEN mark >= :d_prm AND mark < :c_prm THEN 'D'
##                                         ELSE 'E'
##                                       END;
##                      '''
##            cur.execute(sql, {'a_star_prm':a_star, 'a_prm':a, 'b_prm':b, 'c_prm':c, 'd_prm':d})
##            conn.commit()
##            print("\nThe table has been updated")
##
##    
##
##
##    else:
##        print("")
##        print("This is not an option.")
##        print("")
##        choice = True
##
##
##

app = baseline()
app.mainloop()


    

