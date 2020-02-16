
#importing libraries
from tkinter import *
import tkinter as tk
import sqlite3
import statistics
from tkinter import messagebox

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

        for F in (ActualStartPage,EditData, LookAtDatabase, InsertData,GetStudentData,UpdateMark, UpdateTargetGrade, RemoveStudent, Submit, ProceedToAnalysis,Analysis_Page):

            frame = F(container,self)

            self.frames[F] =frame
            
            frame.grid(row =0, column = 0, sticky ="nsew") #sticky does alignment +strech (north, south, east west)

        self.show_frame(ActualStartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() #riases the frame to the top


class ActualStartPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "I don't know what to name the page yet", font = LARGE_FONT)
        label.grid(column = 0, row = 0, columnspan =2, pady = 10, padx = 10)

        ##enter a text widget

        text1 = tk.Label(self, text = "Please select the option you would like to pick", height = 1, width = 50, bg = 'gray95' ) 
        text1.grid(column = 0, row = 2, columnspan =1, pady = 10, padx = 10)


        #buttons

        edit_button = tk.Button(self, text = "Edit Data",
                            command =  lambda:controller.show_frame(EditData))
                            
        edit_button.grid(row = 8 , column= 0, columnspan = 2)

        proceed_button = tk.Button(self, text = "Proceed to Analysis",
                            command =  lambda:controller.show_frame(ProceedToAnalysis))
                            
        proceed_button.grid(row = 8 , column= 1, columnspan = 2)



class EditData(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self,text = "Edit Data", font = LARGE_FONT)
        label.grid(column = 0, row = 0, columnspan = 2, pady = 10, padx =10)

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 9 , column= 1, columnspan = 2)

        #database button


        look_at_database_button = tk.Button(self, text = "Look at the database",
                            command =  lambda:controller.show_frame(LookAtDatabase))
                            
        look_at_database_button.grid(row = 2 , column= 1, columnspan = 2)

        #insert data button

        insert_data_button = tk.Button(self, text = "Insert Data",
                            command =  lambda:controller.show_frame(InsertData))
                            
        insert_data_button.grid(row = 3 , column= 1, columnspan = 2)

        #get student data button

        get_student_data_button = tk.Button(self, text = "Get Student Data",
                            command =  lambda:controller.show_frame(GetStudentData))
                            
        get_student_data_button.grid(row = 4 , column= 1, columnspan = 2)


        #update mark

        update_mark_button = tk.Button(self, text = "Update Mark",
                            command =  lambda:controller.show_frame(UpdateMark))
                            
        update_mark_button.grid(row = 5 , column= 1, columnspan = 2)

        


        #update target grade

        update_target_grade_button = tk.Button(self, text = "Update Target Grade",
                            command =  lambda:controller.show_frame(UpdateTargetGrade))
                            
        update_target_grade_button.grid(row = 6 , column= 1, columnspan = 2)


        #remove student

        remove_student_button = tk.Button(self, text = "Remove Student",
                                          command = lambda: controller.show_frame(RemoveStudent))
        remove_student_button.grid(row = 7, column =1 , columnspan = 2)
        

        

class LookAtDatabase (tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Database", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 3, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)

        #entering the database


        print_records = ''

        cur.execute("SELECT * FROM class") 
        students = cur.fetchall()

        for records in students:
            print_records += str(records) + "\n"


        text1 = tk.Text(self, height = 15, width = 70, bg = 'gray95' ) #adding textbox frame

        text1.insert(tk.INSERT,print_records) #insert text inside textbox frame
        text1.grid(column = 0, row = 2, columnspan =2, pady = 10, padx = 10)

        




class InsertData(tk.Frame):

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
        


        self.firstname = Entry(self, width = 15, bg = "white")
        self.firstname.grid(row = 1, column=1, padx =5, pady = 5)

        self.lastname = Entry(self, width = 15, bg = "white")
        self.lastname.grid(row = 2, column=1, padx =5, pady = 5)

        self.mark__ = Entry(self, width = 15, bg = "white")
        self.mark__.grid(row = 3, column=1, padx =5, pady = 5)

        self.targetgrade = Entry(self, width = 15, bg = "white")
        self.targetgrade.grid(row = 4, column=1, padx =5, pady = 5)



        #Buttons to navigate


        
        button1 = tk.Button(self, text = "Submit",
                            command =  self.insertintosql)
                            
        button1.grid(row = 8 , column= 0)



        button2 = tk.Button(self, text = "Proceed",
                            command = lambda:controller.show_frame(ProceedToAnalysis) )
        button2.grid(row = 8, column = 1)

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 3, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)


    #creating a function that inserts into database

        
    
    def insertintosql(self):
        '''inserting into database'''


        first = self.firstname.get().title()
        last= self.lastname.get().title()
        mark = self.mark__.get()
        target_grade = self.targetgrade.get().upper()
        percentage =0
        grade = "Not yet declared"

        

        #print(target_grade)
        #print(first)


        #checking to see if the error boxes have the correct format


        if first =="" or first.isalpha() != True or last =="" or last.isalpha() != True:
            messagebox.showerror("Error", "Please enter valid data with no special characters")

        if mark.isdigit() != True or mark == 0:
            messagebox.showerror ("Error", "Please enter a valid number")

        if target_grade == "A*" or target_grade == "A" or target_grade == "B" or target_grade == "C" or target_grade == "D" or target_grade == "E":
            pass
        else:
            messagebox.showerror ("Error", "Please enter a valid grade")


        #5: error displayed but still enters in the database? 
  
 
        #calling the function
        cur.execute("INSERT INTO class (first, last, mark, target_grade, percentage,grade) VALUES (?,?,?,?,?,?)",(first,last,mark,target_grade,percentage,grade))
        conn.commit() #inserting the values in the database


        self.firstname.delete(0,END) # clearing the entry after the user has inputted data
        self.lastname.delete(0,END)
        self.mark__.delete(0,END)
        self.targetgrade.delete(0,END)
        self.firstname.focus_set()


class GetStudentData(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Student Data", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)



        #place the labels
        Label(self, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady =5)


        Label(self, text = "Last Name: ").grid(row =2, column = 0, padx = 10, pady =5)


        #placing entry widgets

        self.firstname = Entry(self, width = 15, bg = "white")
        self.firstname.grid(row = 1, column=1, padx =5, pady = 5)

        self.lastname = Entry(self, width = 15, bg = "white")
        self.lastname.grid(row = 2, column=1, padx =5, pady = 5)


        #buttons

        find_button = tk.Button(self, text = "Find",
                                command = self.get_students_by_name)
        find_button.grid(row = 8, column = 1)

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 3, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 0, columnspan = 2)





    def get_students_by_name(self):#function to retrieve student
        with conn:
            first = self.firstname.get().title()
            last= self.lastname.get().title()
            cur.execute('SELECT * FROM class WHERE last = :last AND first =:first',{'last':last, 'first': first})
            #print(cur.fetchall())




            #1: code a validation box. If name is not in database, display a message box



        text1 = tk.Text(self, height = 15, width = 70, bg = 'gray95' ) #adding textbox frame

        text1.insert(tk.INSERT,cur.fetchall()) #insert text inside textbox frame
        text1.grid(column = 0, row = 2, columnspan =2, pady = 10, padx = 10)


            



class UpdateMark(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Update Student's Mark", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)




        #place the labels
        Label(self, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady =5)


        Label(self, text = "Last Name: ").grid(row =2, column = 0, padx = 10, pady =5)

        Label(self, text = "New Mark: ").grid(row =3, column = 0, padx = 10, pady =5)
        


        #placing entry widgets

        self.firstname = Entry(self, width = 15, bg = "white")
        self.firstname.grid(row = 1, column=1, padx =5, pady = 5)

        self.lastname = Entry(self, width = 15, bg = "white")
        self.lastname.grid(row = 2, column=1, padx =5, pady = 5)

        self.new_mark = Entry(self, width = 15, bg = "white")
        self.new_mark.grid(row = 3, column=1, padx =5, pady = 5)


        




        #buttons

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 3, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)

        update_button = tk.Button(self, text = "Update",
                                command = self.update_mark)
        update_button.grid(row = 8, column = 2)




    def update_mark(self): #function to update mark
        with conn:
            first = self.firstname.get().title()
            last = self.lastname.get().title()
            mark = self.new_mark.get().title()
            cur.execute(""" UPDATE class SET mark = :mark
            WHERE first = :first AND last = :last""",
            {'first': first, 'last': last, 'mark' : mark})


            #2: should automatically update database (look at database button) when i press go back?
            #3: message saying: mark updated

    

class UpdateTargetGrade(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Update Student's Target Grade", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)




        #buttons

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 3, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)

        update_button = tk.Button(self, text = "Update",
                                command = self.update_target_grade)
        update_button.grid(row = 8, column = 2)

        


     #place the labels
        Label(self, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady =5)


        Label(self, text = "Last Name: ").grid(row =2, column = 0, padx = 10, pady =5)

        Label(self, text = "New Target Grade: ").grid(row =3, column = 0, padx = 10, pady =5)
        


        #placing entry widgets

        self.firstname = Entry(self, width = 15, bg = "white")
        self.firstname.grid(row = 1, column=1, padx =5, pady = 5)

        self.lastname = Entry(self, width = 15, bg = "white")
        self.lastname.grid(row = 2, column=1, padx =5, pady = 5)

        self.new_target_grade = Entry(self, width = 15, bg = "white")
        self.new_target_grade.grid(row = 3, column=1, padx =5, pady = 5)


    def update_target_grade(self): #function to update target grade
        with conn:
            first = self.firstname.get().title()
            last = self.lastname.get().title()
            target_grade = self.new_target_grade.get().title()
            
            cur.execute(""" UPDATE class SET target_grade = :target_grade
            WHERE first = :first AND last = :last""",
            {'first':first, 'last':last, 'target_grade' : target_grade})


class RemoveStudent(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # parent is the main class, i.e. basline

        label = tk.Label(self, text = "Remove Student", font = LARGE_FONT)
        label.grid(column = 0,row = 0 ,columnspan = 2, pady = 10, padx = 10)


        #place the labels
        Label(self, text = "First Name: ").grid(row =1, column = 0, padx = 10, pady =5)


        Label(self, text = "Last Name: ").grid(row =2, column = 0, padx = 10, pady =5)

        


        #placing entry widgets

        self.firstname = Entry(self, width = 15, bg = "white")
        self.firstname.grid(row = 1, column=1, padx =5, pady = 5)

        self.lastname = Entry(self, width = 15, bg = "white")
        self.lastname.grid(row = 2, column=1, padx =5, pady = 5)


        #buttons

        home_button = tk.Button(self, text = "Back to home",
                            command =  lambda:controller.show_frame(ActualStartPage))
                            
        home_button.grid(row = 8 , column= 5, columnspan = 2)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)

        remove_button = tk.Button(self, text = "Remove Student",
                                command = self.remove_student)
        remove_button.grid(row = 8, column = 2, columnspan =2)


     def remove_student (self): #function to remove student
        with conn:
            first = self.firstname.get().title()
            last = self.lastname.get().title()
            cur.execute("DELETE from class WHERE first = :first AND last = :last",
                      {'first':first, 'last':last})



            #3: Display a list of students with firstname and last name and select from the list

        

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
        button2.grid(row = 8, column = 3)

        back_button = tk.Button(self, text = "Go Back",
                            command = lambda: controller.show_frame(EditData))
        back_button.grid(row = 8, column = 1, columnspan = 2)

        

class ProceedToAnalysis(tk.Frame):





    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Analysis", font = LARGE_FONT)
        label.grid(pady = 10, padx = 10)


        #buttons

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda:controller.show_frame(ActualStartPage) )
        button1.grid(row = 7 , column= 3)

        enter_button = tk.Button(self, text = "Enter",
                                 command = lambda:[self.check_total_mark(), self.percentage()])

        #enter_button = tk.Button(self, text = "Enter",
                                 #command = self.percentage)


        #enter_button = tk.Button(self, text = "Enter",
                                 #command = lambda:controller.show_frame(Analysis_Page))

        
        enter_button.grid(row = 1, column = 3)


            
        cur.execute("SELECT (mark) FROM class")
        result = cur.fetchall()
        #count= 0
        a = [] #the students mark in a list
        
      
        for i in result:
                #count += 1
                a.append(i[0])

        a.sort()
        #print(a)

        global max_mark
        max_mark = a[-1] #finding the largest number in the list
        #print(max_mark)


        #place the labels
        Label(self, text = "Total Mark: ").grid(row =1, column = 0, padx = 10, pady =5)

        #place entry widgets


        self.total_mark = Entry(self, width = 15, bg = "white")
        self.total_mark.grid(row = 1, column=1, padx =5, pady = 5)

        

    def check_total_mark(self):
        

        total_mark = int(self.total_mark.get())
        
        #print("This is the total mark: ", total_mark)
        #print(max_mark)

        print("max mark: ", max_mark, "Total Mark:", total_mark)

        check = True
        

        if total_mark < max_mark:
                messagebox.showerror("Error", "Total Mark cannot be lower than a student's grade")
                self.total_mark.delete(0,END)
                self.total_mark.focus_set()
                check = True
        else:
            pass


    def percentage(self):

        total_mark = int(self.total_mark.get())

        cur = conn.cursor() 
        cur.execute("SELECT * FROM class")
        rows = cur.fetchall()
        #print ("This is rows: ", rows) 

        

        b= []
        for i in rows:  #changing the marks into a perentage value then appending it to a list
                mark = (i[3])
                percentage = round(((mark/total_mark)*100),1)
                b.append(percentage)
                print("This is the percentage", percentage)
        #print(b) #list of raw marks

        for i, val in enumerate(b): #goes through each primary key and updates the percentage field
                #print("UPDATE class SET percentage = (?) WHERE ID = (?)",(val,(i+1),))
                cur.execute("UPDATE class SET percentage = (?) WHERE ID = (?)",(val,(i+1),))
        conn.commit()

    
    


class Analysis_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Analyis of the Class", font = LARGE_FONT)
        label.grid(pady = 10, padx = 10)


        next_button = tk.Button(self, text = "Next",
                                command = self.enter_grade())
        next_button.grid(row = 3, column = 3)

        

        Label(self, text = "A* ").grid(row =1, column = 0, padx = 10, pady =5)
        Label(self, text = "A ").grid(row =2, column = 0, padx = 10, pady =5)
        Label(self, text = "B ").grid(row =3, column = 0, padx = 10, pady =5)
        Label(self, text = "C").grid(row =4, column = 0, padx = 10, pady =5)
        Label(self, text = "D ").grid(row =5, column = 0, padx = 10, pady =5)
        Label(self, text = "E ").grid(row =6, column = 0, padx = 10, pady =5)
        Label(self, text = "F ").grid(row =7, column = 0, padx = 10, pady =5)
        



        self.a_star = Entry(self, width = 15, bg = "white")
        self.a_star.grid(row = 1, column = 1, padx= 5, pady=5)

        self.a = Entry(self, width = 15, bg = "white")
        self.a.grid(row = 2, column = 1, padx= 5, pady=5)

        self.b = Entry(self, width = 15, bg = "white")
        self.b.grid(row = 3, column = 1, padx= 5, pady=5)

        self.c = Entry(self, width = 15, bg = "white")
        self.c.grid(row = 4, column = 1, padx= 5, pady=5)

        self.d = Entry(self, width = 15, bg = "white")
        self.d.grid(row = 5, column = 1, padx= 5, pady=5)

        self.e = Entry(self, width = 15, bg = "white")
        self.e.grid(row = 6, column = 1, padx= 5, pady=5)

        self.f = Entry(self, width = 15, bg = "white")
        self.f.grid(row = 7, column = 1, padx= 5, pady=5)




        
        a_star = self.a_star.get()
        a = self.a.get()
        b = self.b.get()
        c= self.c.get()
        d = self.d.get()
        e= self.e.get()
        f= self.f.get()

        


    def enter_grade(self):
        a_star = self.a_star.get()
        print(a_star)





    

        
#Defining functions that will edit the database
        
##def get_students_by_name(first,last): #function to retrieve student
##    with conn:
##            cur.execute('SELECT * FROM class WHERE last = :last AND first =:first',{'last':last, 'first': first})
##            print(cur.fetchall())
##            
##
##def update_mark(first,last, mark): #function to update mark
##    with conn:
##        cur.execute(""" UPDATE class SET mark = :mark
##        WHERE first = :first AND last = :last""",
##        {'first': first, 'last': last, 'mark' : mark})
##
##def update_target_grade(first,last,target_grade): #function to update target grade
##    with conn:
##        cur.execute(""" UPDATE class SET target_grade = :target_grade
##        WHERE first = :first AND last = :last""",
##        {'first':first, 'last':last, 'target_grade' : target_grade})
##
##def remove_student (first,last): #function to remove student
##    with conn:
##        cur.execute("DELETE from class WHERE first = :first AND last = :last",
##                  {'first':first, 'last':last})


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


    

