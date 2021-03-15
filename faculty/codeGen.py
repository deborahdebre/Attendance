import random as r
import tkinter as tk
import sheets

def generator():
    randomizer = r.randint(1000,9999)
    sheets.code_updater(randomizer)
    return randomizer

def newcode():
    exp.destroy()
    
    exp1=tk.Tk()
    exp1.geometry('400x300')
    exp1.title ('Attendance PRO')

    exp1.configure(background ='#ffffff')

    lecturer(exp1)
       
    
    
def lecturer (login):
    codeLabel = tk.Label(login,text = 'Code:',bg='light grey')
    codeLabel.place(x=165,y=100)
    
    code = tk.Label (login,text = str(generator()))
    code.place(x=165,y=120)

    generate = tk.Button (text ='Generate', command = newcode)
    generate.place(x=130, y=170)

    quitbutton = tk.Button (text ='Quit', command = closing)
    quitbutton.place(x=210,y=170)

def closing():
    generator()
    exit(0)    
 
exp=tk.Tk()
exp.geometry('400x300')
exp.title ('Attendance CHECKER')

exp.configure(background ='#ffffff')

lecturer(exp)
                     
