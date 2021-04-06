# ___Importing Statements___ :-
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter
import urllib.request
import webbrowser
import math
import os

# ___Root Window___ :-
root=Tk()
root.title("SK Identification Form")
root.geometry("733x550")
root.minsize(733,550)
root.maxsize(733,550)

# ___def Functions and Importing Objects___ :-
def inputtingValuesUsingClickingButton():
     
     print(f"{nameValue.get(),phoneValue.get(),genderValue.get()}\n")
     with open("records.txt","a") as f:
          f.write(f"{nameValue.get(),phoneValue.get(),genderValue.get()}\n")

def logo():
     print('\nThis is the Logo os SK Pvt. Ltd. !!!')

img1=PhotoImage(file=r"C:\Users\Sunil Kumar\Downloads\logo.png")

# ___Frames___ :-
frame1=Frame(root)
frame1.pack()

frame2=Frame(root)
frame2.pack(anchor=W)

frame3=Frame(root)
frame3.pack(anchor=W)

frame4=Frame(root)
frame4.pack(anchor=W)

frame5=Frame(root)
frame5.pack(anchor=W)

frame6=Frame(root)
frame6.pack()

# ___Content___ :-
title=ttk.Label(frame1,text="Dear Customer, Please fill this Form kindly !",foreground="black",
          font="timesnewroman 20 bold").pack(padx=80,pady=25)

# ___Name___ :-
nameLabel=ttk.Label(frame2,text="Name       :",font="timesnewroman 15",
               foreground="black").pack(anchor=W,padx=25,pady=2.5)
nameValue=StringVar()
nameEntry=ttk.Entry(frame2, width=55,textvariable=nameValue,font="timesnewroman 12").pack(padx=25,pady=2.5)

# ___Phone___ :-
phoneLabel=ttk.Label(frame3,text="Phone       :",font="timesnewroman 15",
               foreground="black").pack(anchor=W,padx=25,pady=2.5)
phoneValue=IntVar()
phoneEntry=ttk.Entry(frame3, width=55,textvariable=phoneValue,font="timesnewroman 12").pack(padx=25,pady=2.5)

# ___Gender___ :-
genderLabel=ttk.Label(frame4,text="Gender       :",font="timesnewroman 15",
                  foreground="black").pack(anchor=W,padx=25,pady=2.5)
genderValue=StringVar()
genderEntry=ttk.Entry(frame4, width=55,textvariable=genderValue,font="timesnewroman 12").pack(padx=25,pady=2.5)

# ___Submit Button___ :-
btn1=Button(frame5,text="Submit",command=inputtingValuesUsingClickingButton).pack(anchor=W,padx=25,pady=2.5)

#___All Sample Or Trials___ :-
imageBtn=Button(frame6,image=img1,command=logo).pack()

# ___Exit() Statements___ :-
root.mainloop()
input()