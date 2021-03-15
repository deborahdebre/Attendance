import tkinter as tk
import sheets

#Function to check correctness of code supplied
def code_check():
    student_email = email.get()
    supplied_code = code.get()
    data = sheets.sheet_data()
    
    if supplied_code != int(data[-1][0]) or student_email.lower() not in data:
        absent_function()
        print("Wrong code/email")
    else:
        present_function()
        sheets.sheet_update(student_email)
        print("Correct")
        
def present_function():
    login.destroy()
    present_window = tk.Tk()
    present_window.geometry('300x150')
    present_window.title("Present")

    present_label =tk.Label(text ="You have been marked PRESENT")
    present_label.place(x=50,y=20)

    acceptance_button =tk.Button(text="Close", command = closing)
    acceptance_button.place(x=125,y=90)


def absent_function():
    login.destroy()
    global  absent_window
    absent_window  = tk.Tk()
    absent_window.geometry('200x300')
    absent_window.title("Absent")
    
    
    absent_label = tk.Label(text="WRONG CODE/EMAIL")
    absent_label.place(x=20,y=10)
    
    retry_button = tk.Button(text="Retry",command = login_function)
    retry_button.place(x=50,y=200)

    cancel_button = tk.Button(text ="Cancel",command = closing)
    cancel_button.place(x=100, y=200)
    
def login_function():
    absent_window.destroy()
    global login
    login = tk.Tk()
    login.geometry('400x300')
    login.title('Attendance Login')
    screen(login)
    
           
def screen(login):
    login.heading = tk.Label(text ="Attendance Form",bg="grey",fg="black",width="500",height="3")
    
#Packing automatically arranges created widgets
    login.heading.pack(side="top")
    
    emailLabel = tk.Label(login,text='Ashesi Email:')
    codeLabel = tk.Label(login,text='Class Code:')
#Placing allows the use of x and y coordinates to manually place widgets
    emailLabel.place(x=90,y=100)
    codeLabel.place(x=100,y=130)
#Creating variables to store email and code user inputs
    global email
    global code
    email = tk.StringVar()
    code= tk.IntVar()

    EmailEntry = tk.Entry(login,text = email,width="30")
    CodeEntry =tk.Entry(login,text = code)

    EmailEntry =tk.Entry(login,text = email)
    CodeEntry = tk.Entry(login,text = code)

    EmailEntry.place(x=180,y=100)
    CodeEntry.place(x=180,y=130)
#To execute the get_values function when the Submit button is clicked
    submit = tk.Button(text ='Submit', command = code_check)
    submit.place(x=200,y=170)

def closing():
    exit(0)
    
    
    
global login
login = tk.Tk()
login.geometry('400x300')
login.title('Attendance Login')

screen(login)


