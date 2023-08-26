from tkinter import *
from chatbot import answer
root=Tk()
root.configure(background="black")
txt=Text(root)
txt.insert(END,"********************************************************************************\n")
txt.insert(END,"                    WELCOME TO AICTE CHATBOT DOJOBOT\n")
txt.insert(END,"********************************************************************************\n")
def send ():
    s=e.get()
    j=answer(s)

    txt.insert(END,"DOJOBOT-\n"+j)
    txt.insert(END,"\n")


txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="SEND",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("chatbot")
root.mainloop()
