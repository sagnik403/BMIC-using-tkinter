from tkinter import *
from tkinter import messagebox
import math
def sum():
    a=int(t1.get())
    b=int(t2.get())
    c= (b/math.pow(a,2))
    t3.insert(0,c)
    if (c>0 and c<18.5):
        t4.insert(0,"Your BMI is low, so you are underweight. Eat some more or the wind will carry you away to distant lands.")
    elif (c >= 18.5 and c <= 24.9):
        t4.insert(0,"Your BMI is good , so you have a normal weight. GOOD...Looks you're so much concern about your fitness.")
    elif (c >= 25 and c <= 29.9):
        t4.insert(0,"Your BMI is high so you are overweight. Eat some less or one day your stomach will brust like me.")
    elif (c >= 30 and c <= 34.9):
        t4.insert(0,"Your BMI is not good, so you are obese. You don't need to eat for one year.")
    elif (c >= 35):
        t4.insert(0,"Your BMI is bad, so you are obese. You don't need to eat for one year.")
    
    elif(c<=0):
        messagebox.showerror("BMI","Please Give right information")
    else:
        messagebox.showerror("BMI","Please Give right information")


win=Tk()
win.geometry('750x300')
win['bg'] = "#074463"

l1=Label(win,text="Enter your Height in meter", bg="#074463",fg="white",font=("verdana",15,"bold"))
l1.grid(row=0,column=0,padx=10, pady=10)
t1=Entry(win,width=25,borderwidth=5)
t1.grid(row=0,column=1)

l2=Label(win,text="Enter your Weight in kg", bg="#074463",fg="white",font=("verdana",15,"bold"))
l2.grid(row=1,column=0,padx=10, pady=10)
t2=Entry(win,width=25,borderwidth=5)
t2.grid(row=1,column=1)

l3=Label(win,text="BMI", bg="#074463",fg="white",font=("verdana",15,"bold"))
l3.grid(row=2,column=0,padx=10, pady=10)
t3=Entry(win,width=25,borderwidth=5)
t3.grid(row=2,column=1)

b1=Button(win,text="Click For SUM",command=sum)
b1.grid(row=3,column=1,padx=20,pady=10)

t4=Entry(win,width=110,borderwidth=5)
t4.grid(row=4,column=0,columnspan=2,padx=20)

win.mainloop()