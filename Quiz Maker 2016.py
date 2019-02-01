import tkMessageBox
from Tkinter import *

"This program is for Python 2.7.X ONLY!"

root = Tk()
root.title("Quiz Maker")
root.configure(background='white')






"MAIN PROGRAM"

"VARIABLES AND ARRAYS"


Question=[];
Choice=[];
Answer=[];
Right01 = 0
Wrong01 = 0
Counter=0
Num = 0
Chance = 2
Revinum = 0
Choicecount = 0
Percentage = 0
StudentAns = ""

"GET TEACHERNAME PART"
def GetTeachername():
    global Teachername
    Teachername = LogInEntry.get()
    
    "Check for errors"
    if Teachername == "" or Teachername.isspace() :
        
        tkMessageBox.showinfo( "Error!", "Please enter your name")
    else:
        tkMessageBox.showinfo( "Quiz Maker", "Welcome to Quiz Maker,  " +Teachername)
        HideWindow1()
        ShowWindow2()
        
"Get number of question that the teacher want to make"
def GetNum():
    global Num
    Num = NumOfQuestionEntry.get()
    

    "Check for error"
    if Num.isdigit() and int(Num) > 0:
        print "CONGRAT!"
        HideWindow2()
        ShowWindow3()
    else:
        if Num.isspace() or Num == "" or Num.isalpha():
            tkMessageBox.showinfo( "Error!", "Please enter the number!")
        else:
            if Num.isdigit() and int(Num) <= 0:
                tkMessageBox.showinfo( "Error!", "Number must be more than 0!")
            else:
                tkMessageBox.showinfo( "Error!", "Please enter only number!")
                
       
        
        
"Set Questions and choices part"                     
def GetQuestionsAndChoices():
    global Num
    global Question
    global Answer
    global Choice
    global Counter
    global Choicecount
    
    "Check the for the blank error"
    if QuestionEntry.get() == "" or QuestionEntry.get().isspace():
        tkMessageBox.showinfo( "Error!", "Please enter the question!")
        "Clear the field"
        Choice1Entry.delete(0, END)
        Choice2Entry.delete(0, END)
        QuestionEntry.delete(0, END)
        Checkbox1.set(0)
        Checkbox2.set(0)
    else:
        if Choice1Entry.get() == "" or Choice2Entry.get() == "" or Choice1Entry.get().isspace() or Choice1Entry.get().isspace():
            tkMessageBox.showinfo( "Error!", "Please enter all the choices!")
            "Clear the field"
            Choice1Entry.delete(0, END)
            Choice2Entry.delete(0, END)
            QuestionEntry.delete(0, END)
            Checkbox1.set(0)
            Checkbox2.set(0)
        else:
            if Checkbox1.get() == 0 and Checkbox2.get() == 0:
                 tkMessageBox.showinfo( "Error!", "Please tick one of the checkbox!")
                 "Clear the field"
                 Checkbox1.set(0)
                 Checkbox2.set(0)
                 Choice1Entry.delete(0, END)
                 Choice2Entry.delete(0, END)
                 QuestionEntry.delete(0, END)
            else:
            
                "Continue the program"
                
                Question.append(QuestionEntry.get())
                Counter = int(Counter)+1
                Choice.append(Choice1Entry.get())
                Choicecount = int(Choicecount)+1
                Choice.append(Choice2Entry.get())
                Choicecount = int(Choicecount)+1
                if Checkbox1.get() == 1:
                    Answer.append(Choice1Entry.get())
                if Checkbox2.get() == 1:
                    Answer.append(Choice2Entry.get())
                print Question
                print Choice
                print Answer
                "Clear the field"
                Checkbox1.set(0)
                Checkbox2.set(0)
                Choice1Entry.delete(0, END)
                Choice2Entry.delete(0, END)
                QuestionEntry.delete(0, END)
                
                "Check if the user set all the questions according to the number of question that he or she wanted to make"
                if int(Counter) >= int(Num):
                    tkMessageBox.showinfo( "Notify", "This question is now set! You successfully set all your questions!")
                    HideWindow3()
                    ShowWindow4()
                else:
                    tkMessageBox.showinfo( "Notify", "This question is now set! Enter you next question!")
                    
                    

"This is a fucnction in pseudocode/flowchart"
"This function is to get student username and password"
def Studentlogin():
    Username = UsernameEntry.get()
    Password = PasswordEntry.get()
    
    
"Student log in part"    
def CheckStudentloginPassword():
    global Chance
    Studentlogin()
    "3 Chances authentication part"
    if UsernameEntry.get() == "" or UsernameEntry.get().isspace() or PasswordEntry.get() == "" or PasswordEntry.get().isspace():
        tkMessageBox.showinfo( "Error", "Do not leave username or password blank!")
        "Clear the field"
        UsernameEntry.delete(0, END)
        PasswordEntry.delete(0, END)
    else:
        "Check weather password is correct or not"
        if PasswordEntry.get() != "123" and Chance >= 1:
            tkMessageBox.showinfo( "Error", "Password is incorrect!")
            Chance = int(Chance) - 1
            "Clear the field"
            UsernameEntry.delete(0, END)
            PasswordEntry.delete(0, END)
        else:
            if PasswordEntry.get() == "123":
                tkMessageBox.showinfo( "Message", "Congratulation!")
                "Then go to next window"
                HideWindow4()
                ShowWindow5()
            else:
                tkMessageBox.showinfo( "Notify", "You run out of chance! The program will exit!")
                EndProgram()
            
"Checkbox part"
"If one of the checkbox is ticked, another one will be unticked"
def CheckTickbox1():
    if(Checkbox1.get()):
       Checkbox2.set(0)
      

def CheckTickbox2():
    if(Checkbox2.get()):
       Checkbox1.set(0)
       
"Get number of question that the student want to answer"       
def GetRevinum():
    global Num
    global Revinum
    global Counter
    Revinum = RevinumEntry.get()
    if Revinum.isdigit() and int(Revinum) > 0 and int(Revinum) <= int(Num):
        Counter = 0
        "Continue to another window"
        HideWindow5()
        ShowWindow6()
    else:
        tkMessageBox.showinfo( "Error!", "Exceed available questions or it is not a number more than 0")
        HideWindow5()
        ShowWindow7()
        
"If student click on the first(left) choice button, it will compare that choice with the answer weather  it match or not(if not matched, then the student got wrong!)"    
def GetChoice1Button():
    global Question
    global Choice
    global Choicecount
    global Answer
    global Counter
    global Right01
    global Wrong01
    global Revinum
    if Revinum > 0:
        StudentAns = Choice1ButtonText.get()
        if StudentAns == Answer[Counter]:
            Right01 = int(Right01)+1
            tkMessageBox.showinfo( "Notify!", "Correct!")
            print "Correct!!"
        else:
            Wrong01 = int(Wrong01)+1
            tkMessageBox.showinfo( "Notify!", "Wrong!")
            print "Wrong!!"
        Counter = int(Counter)+1
        Revinum = int(Revinum)-1
        if Revinum != 0:
            PlayQuestionText.set(Question[Counter])
            Choice1ButtonText.set(Choice[Choicecount])
            Choicecount = int(Choicecount)+1
            Choice2ButtonText.set(Choice[Choicecount])
            Choicecount = int(Choicecount)+1
    if Revinum == 0:
        HideWindow6()
        ShowWindow7()
        
    
"If student click on the second(right) choice button, it will compare that choice with the answer weather it match or not (if not matched, then the student got wrong!)"     
def GetChoice2Button():
    global Question
    global Choice
    global Choicecount
    global Answer
    global Counter
    global Right01
    global Wrong01
    global Revinum
    if Revinum > 0:
        StudentAns = Choice2ButtonText.get()
        if StudentAns == Answer[Counter]:
            Right01 = int(Right01)+1
            tkMessageBox.showinfo( "Notify!", "Correct!")
            print "Correct!!"
        else:
            Wrong01 = int(Wrong01)+1
            tkMessageBox.showinfo( "Notify!", "Wrong!")
            print "Wrong!!"
        Counter = int(Counter)+1
        Revinum = int(Revinum)-1
        if Revinum != 0:
            PlayQuestionText.set(Question[Counter])
            Choice1ButtonText.set(Choice[Choicecount])
            Choicecount = int(Choicecount)+1
            Choice2ButtonText.set(Choice[Choicecount])
            Choicecount = int(Choicecount)+1
    if Revinum == 0:
        HideWindow6()
        ShowWindow7()
        
"If student click Retry button, it will go to window5 and re get the number of question that the student want to asnwer!"       
def RetryQuestion():
    global Right01
    global Wrong01
    ShowWindow5()
    HideWindow7()
    Right01 = 0
    Wrong01 = 0
    
"if student click on End button, program will end"
def EndProgram():
    root.destroy()
        
                                
    
 
"GUI PROGRAM PART"
"SHOW AND HIDE GUI FUNCTION "

def HideWindow1():
    LabelWelcome.grid_forget()
    LabelLogin.grid_forget()
    LogInEntry.grid_forget()
    LogInButton.grid_forget()
    
def ShowWindow2():
    LabelGetQuestion.grid(row=1, column=1, pady=12, padx=5)
    NumOfQuestionEntry.grid(row=2, column=1, ipady=3,  pady=10, padx=3)
    NumOfQuestionButton.grid(sticky=W, row=3, ipady=10, ipadx=3, column=1, pady=30, padx=7)

def HideWindow2():
    LabelGetQuestion.grid_forget()
    NumOfQuestionEntry.grid_forget()
    NumOfQuestionButton.grid_forget()
    
def ShowWindow3():
    LabelSetQuestion.grid(row=1, column=1, pady=12, padx=10)
    QuestionEntry.grid(row=3, column=1, ipady=3,  pady=8, padx=8)
    LabelQuestion.grid(row=2, column=1, ipady=3,  pady=1, padx=1)
    LabelChoice1.grid(row=4, column=1, ipady=3,  pady=1, padx=1)
    Choice1Entry.grid(row=5, column=1, ipady=3,  pady=8, padx=1, )
    LabelChoice2.grid(row=6, column=1, ipady=3,  pady=1, padx=1)
    Choice2Entry.grid(row=7, column=1, ipady=3,  pady=8, padx=1, )
    SetQuestionAndAnswerButton.grid(sticky=W, row=8, ipady=10, ipadx=3, column=1, pady=30, padx=7)
    ChoiceBox1.grid(row=5, column=1, sticky=E, padx=5,columnspan=1)
    ChoiceBox2.grid(row=7, column=1, sticky=E, padx=5,columnspan=1)
    
def HideWindow3():
    LabelSetQuestion.grid_forget()
    QuestionEntry.grid_forget()
    LabelQuestion.grid_forget()
    LabelChoice1.grid_forget()
    Choice1Entry.grid_forget()
    LabelChoice2.grid_forget()
    Choice2Entry.grid_forget()
    SetQuestionAndAnswerButton.grid_forget()
    ChoiceBox1.grid_forget()
    ChoiceBox2.grid_forget()

def ShowWindow4():
    LabelStudentWelcome.grid(row=0, column=1, pady=15, padx=9, ipadx=10, ipady=8)
    LabelUsername.grid( sticky=W, row=1, column=1, pady=3, padx=5)
    UsernameEntry.grid(row=2, column=1, ipady=3, pady=5, padx=7)
    LabelPassword.grid( sticky=W, row=3, column=1, pady=3, padx=5)
    PasswordEntry.grid(row=4, column=1, ipady=3, pady=5, padx=7)
    StudentLogInButton.grid(sticky=W, row=5, ipady=10, ipadx=3, column=1, pady=30, padx=7)

def HideWindow4():
    LabelStudentWelcome.grid_forget()
    LabelUsername.grid_forget()
    UsernameEntry.grid_forget()
    LabelPassword.grid_forget()
    PasswordEntry.grid_forget()
    StudentLogInButton.grid_forget()

def ShowWindow5():
    LabelGetRevinum.grid(row=1, column=1, pady=12, padx=5)
    RevinumEntry.grid(row=2, column=1, ipady=3,  pady=10, padx=3)
    RevinumButton.grid(sticky=W, row=3, ipady=10, ipadx=3, column=1, pady=30, padx=7)

def HideWindow5():
    LabelGetRevinum.grid_forget()
    RevinumEntry.grid_forget()
    RevinumButton.grid_forget()

def ShowWindow6():
    global Question
    global Counter
    global Choicecount
    global Choice
    Counter = 0
    Choicecount = 0
    PlayQuestionText.set(Question[Counter])
    LabelPlayQuestion.grid(row=1, column=1, pady=15, padx=5, ipadx=200, ipady=15, columnspan=2)
    Choice1ButtonText.set(Choice[Choicecount])
    Choicecount = int(Choicecount)+1
    Choice2ButtonText.set(Choice[Choicecount])
    Choicecount = int(Choicecount)+1
    PlayChoice1Button.grid(sticky=E, row=2, ipady=10, ipadx=30, column=0, pady=30, padx=30, columnspan=2)
    PlayChoice2Button.grid(sticky=W, row=2, ipady=10, ipadx=30, column=2, pady=30, padx=30, columnspan=2)

def HideWindow6():
    PlayChoice1Button.grid_forget()
    PlayChoice2Button.grid_forget()
    LabelPlayQuestion.grid_forget()

def ShowWindow7():
    global Revinum
    global Num
    global Right01
    global Wrong01
    global Percentage
    RightCountText.set(Right01)
    WrongCountText.set(Wrong01)
    if (int(Right01) + int(Wrong01)) != 0:
        Percentage = (float(Right01)/(int(Right01)+int(Wrong01)))*100
        Percentage = int(Percentage)
        PercentageCountText.set(Percentage)
    print Percentage
    ResultLabel.grid(row=0, column=1, pady=11, padx=100, ipadx=10, ipady=8 , columnspan=2)
    RightLabel.grid(row=1, column=1, pady=11, padx=9, ipadx=10, ipady=8)
    RightCountLabel.grid(row=1, column=2, pady=11, padx=9, ipadx=10, ipady=8)
    WrongLabel.grid(row=2, column=1, pady=11, padx=9, ipadx=10, ipady=8)
    WrongCountLabel.grid(row=2, column=2, pady=11, padx=9, ipadx=10, ipady=8)
    OverallText1.set(Right01)
    OverallText2.set(int(Right01)+int(Wrong01))
    PercentageLabel.grid(row=3, column=1, pady=11, padx=9, ipadx=10, ipady=8)
    PercentageCountLabel.grid(row=3, column=2, pady=11, padx=9, ipadx=10, ipady=8)
    OverallLabel1.grid(row=4,sticky=W, column=1, pady=11, padx=9, ipadx=10, ipady=8,columnspan=2)
    OverallLabel2.grid(row=4, sticky=E, column=1, pady=11, padx=9, ipadx=10, ipady=8,columnspan=1)
    OverallLabel3.grid(row=4,sticky=W, column=2, pady=11, padx=9, ipadx=10, ipady=8,columnspan=2)
    OverallLabel4.grid(row=4,  sticky=E,column=2, pady=11, padx=9, ipadx=10, ipady=8,columnspan=1)
    RetryButton.grid( row=5, ipady=10, ipadx=3, column=0, pady=30, padx=15,columnspan=2)
    EndButton.grid(sticky=W, row=5, ipady=10, ipadx=10, column=2, pady=30, padx=15,columnspan=2)
    

def HideWindow7():
    ResultLabel.grid_forget()
    RightLabel.grid_forget()
    RightCountLabel.grid_forget()
    WrongLabel.grid_forget()
    WrongCountLabel.grid_forget()
    RetryButton.grid_forget()
    EndButton.grid_forget()
    OverallLabel1.grid_forget()
    OverallLabel2.grid_forget()
    OverallLabel3.grid_forget()
    OverallLabel4.grid_forget()
    PercentageCountLabel.grid_forget()
    PercentageLabel.grid_forget()
    
    
        
    
    
    
    
    
    

"CREATE AND HIDE ALL GUI WHEN PROGRAM STARTED (Except window 1 widgets becuase when we start the program we need to show it anyway)"
"TEACHER LOGIN Window(Window1)"

LabelWelcome = Label(root, text="Welcome to Quiz Maker!", bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ))
LabelWelcome.grid(row=0, column=1, pady=15, padx=9, ipadx=10, ipady=8)

LabelLogin = Label(root, text="Name", fg="gray22", font=("Lucida Sans Unicode",11, ), bg="white",)
LabelLogin.grid( sticky=W, row=1, column=1, pady=3, padx=5)

LogInEntry = Entry(root, bg="lavender", width=50)
LogInEntry.grid(row=2, column=1, ipady=3, pady=5, padx=7)

LogInButton = Button(root, bg="SlateBlue4", fg="White", text="LOGIN", font=("Lucida Sans Unicode",8, "bold"), command=GetTeachername)
LogInButton.grid(sticky=W, row=3, ipady=10, ipadx=3, column=1, pady=30, padx=7)


"Get Number of question window(Window2)"

LabelGetQuestion = Label(root, text="Enter number of question(s) you want to create", fg="white", font=("Lucida Sans Unicode",12, ), bg="SlateBlue4",)
LabelGetQuestion.grid_forget()

NumOfQuestionEntry = Entry(root, bg="lavender", width=30)
NumOfQuestionEntry.grid_forget()


NumOfQuestionButton = Button(root, bg="SlateBlue4", fg="White", text="PROCEED", font=("Lucida Sans Unicode",8, "bold"), command=GetNum)
NumOfQuestionButton.grid_forget()

"Set Question and Answer (Window3)"

LabelSetQuestion = Label(root, text="Enter your question(s) and choices.Tick for the correct choice.", fg="white", font=("Lucida Sans Unicode",12), bg="SlateBlue4")
LabelSetQuestion.grid_forget()

LabelQuestion = Label(root, text="Question", fg="gray22", font=("Lucida Sans Unicode", 11), bg="white")
LabelQuestion.grid_forget()

QuestionEntry = Entry(root, bg="lavender", width=70)
QuestionEntry.grid_forget()

Choice1Entry = Entry(root, bg="lavender", width=55)
Choice1Entry.grid_forget()

Choice2Entry = Entry(root, bg="lavender", width=55)
Choice2Entry.grid_forget()

LabelChoice1 = Label(root, text="Choice 1", fg="gray22", font=("Lucida Sans Unicode", 11), bg="white")
LabelChoice2 = Label(root, text="Choice 2", fg="gray22", font=("Lucida Sans Unicode", 11), bg="white")
LabelChoice1.grid_forget()
LabelChoice2.grid_forget()

SetQuestionAndAnswerButton = Button(root, bg="SlateBlue4", fg="White", text="PROCEED", font=("Lucida Sans Unicode",8, "bold"), command=GetQuestionsAndChoices )
SetQuestionAndAnswerButton.grid_forget()

"Checkboxes"
Checkbox1 = 0
Checkbox2 = 0
Checkbox1=IntVar()
ChoiceBox1 = Checkbutton(root, bg="white",text='1   ', variable=Checkbox1, command=CheckTickbox1)
ChoiceBox1.grid_forget()
Checkbox2=IntVar()
ChoiceBox2 = Checkbutton(root, bg="white", text='2   ', variable=Checkbox2, command=CheckTickbox2)
ChoiceBox2.grid_forget()




"STUDENT LOGIN window (Window4)"

LabelStudentWelcome = Label(root, text="Enter student username and password!", bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",14, ))
LabelStudentWelcome.grid_forget()

LabelUsername = Label(root, text="Username", fg="gray22", font=("Lucida Sans Unicode",11, ), bg="white",)
LabelUsername.grid_forget()

UsernameEntry = Entry(root, bg="lavender", width=50)
UsernameEntry.grid_forget()

LabelPassword = Label(root, text="Password", fg="gray22", font=("Lucida Sans Unicode",11, ), bg="white",)
LabelPassword.grid_forget()

PasswordEntry = Entry(root, bg="lavender", width=50)
PasswordEntry.grid_forget()


StudentLogInButton = Button(root, bg="SlateBlue4", fg="White", text="LOGIN", font=("Lucida Sans Unicode",8, "bold"), command=CheckStudentloginPassword )
StudentLogInButton.grid_forget()



"Get Revinum window(Window5)"

LabelGetRevinum = Label(root, text="Enter number of question(s) you want to answer", fg="white", font=("Lucida Sans Unicode",12, ), bg="SlateBlue4",)
LabelGetRevinum.grid_forget()

RevinumEntry = Entry(root, bg="lavender", width=30)
RevinumEntry.grid_forget()


RevinumButton = Button(root, bg="SlateBlue4", fg="White", text="PROCEED", font=("Lucida Sans Unicode",8, "bold"), command=GetRevinum)
RevinumButton.grid_forget()


"Answering window (Window6)"

PlayQuestionText = StringVar()
PlayQuestionText.set("Place question here")
LabelPlayQuestion = Label(root, textvariable=PlayQuestionText, bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ))
LabelPlayQuestion.grid_forget()

Choice1ButtonText = StringVar()
Choice1ButtonText.set("Place choice1 here")
PlayChoice1Button = Button(root, textvariable=Choice1ButtonText, bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ),command=GetChoice1Button)
PlayChoice1Button.grid_forget()

Choice2ButtonText = StringVar()
Choice2ButtonText.set("Place choice2 here")
PlayChoice2Button = Button(root, textvariable=Choice2ButtonText, bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ),command=GetChoice2Button)
PlayChoice2Button.grid_forget()


"Result window!(Window7)"

ResultLabel = Label(root, text="Result", bg="white", fg="gray22", font=("Lucida Sans Unicode",17, ))
ResultLabel.grid_forget()

RightLabel = Label(root, text="Right", bg="white", fg="green", font=("Lucida Sans Unicode",11, ))
RightLabel.grid_forget()

RightCountText = IntVar()
RightCountText.set("0")
RightCountLabel = Label(root, textvariable=RightCountText, bg="white", fg="green", font=("Lucida Sans Unicode",11, ))
RightCountLabel.grid_forget()
WrongCountText= IntVar()
WrongCountText.set("0")
WrongCountLabel = Label(root, textvariable=WrongCountText, bg="white", fg="red", font=("Lucida Sans Unicode",11, ))
WrongCountLabel.grid_forget()

WrongLabel = Label(root, text="Wrong", bg="white", fg="red", font=("Lucida Sans Unicode",11, ))
WrongLabel.grid_forget()

PercentageLabel = Label(root, text="Percentage", bg="white", fg="blue", font=("Lucida Sans Unicode",11, ))
PercentageLabel.grid_forget()
PercentageCountText= IntVar()
PercentageCountText.set("0")
PercentageCountLabel= Label(root, textvariable=PercentageCountText, bg="white", fg="blue", font=("Lucida Sans Unicode",11, ))
PercentageCountLabel.grid_forget()

OverallText1 = IntVar()
OverallText1.set("0")
OverallText2 = IntVar()
OverallText2.set("0")
OverallLabel1 = Label(root, bg="white", text="You got",fg="gray22", font=("Lucida Sans Unicode",11, ))
OverallLabel2 = Label(root, bg="white", textvariable=OverallText1,fg="green", font=("Lucida Sans Unicode",11, ))
OverallLabel3 = Label(root, bg="white", text="out of",fg="gray22", font=("Lucida Sans Unicode",11, ))
OverallLabel4 = Label(root, bg="white", textvariable=OverallText2,fg="gray22", font=("Lucida Sans Unicode",11, ))
OverallLabel4.grid_forget()
OverallLabel3.grid_forget()
OverallLabel1.grid_forget()
OverallLabel2.grid_forget()

RetryButton = Button(root, text="Retry", bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ),command=RetryQuestion)
RetryButton.grid_forget()
EndButton = Button(root, text="End", bg="SlateBlue4", fg="white", font=("Lucida Sans Unicode",15, ),command=EndProgram)
EndButton.grid_forget()











root.mainloop()
