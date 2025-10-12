from customtkinter import*
from PIL import Image
from tkinter import messagebox

win = CTk()


win.geometry("600x400")
win.title("мега тест")

def qstn():
        global qstns,n,answrs
        win2 = CTk()

        win2.geometry('400x400')
        win2.title('вопрос')
        frm = CTkFrame(win2)
        frm.pack()
        label_win = CTkLabel(frm,text=qstns[n],font=('Helvetica',25,'bold'))
        label_win.pack(pady=20)
        ans = IntVar(value=0)
        answer1 = CTkRadioButton(frm,text=answrs[n],variable=ans,value=1)
        answer1.pack(pady=20)
        answer2 = CTkRadioButton(frm,text=answrs[n+1],variable=ans,value=2)
        answer2.pack(pady=20)
        answer3 = CTkRadioButton(frm,text=answrs[n+2],variable=ans,value=3)
        answer3.pack(pady=20)

        btn1=CTkButton(frm,text="Відповсти",command=qstn2)
        btn1.pack(pady=20)

        
        win.withdraw()
        win2.mainloop()
def qstn2():
        global btn1,qstns,answrs,n
        print(n)
        n=n+1
        
        
        
qstns = ["1","2","3","4","5","6"]
answrs = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
n=0


lbl = CTkLabel(win, text="Ваше ім'я:",font=("None",20),text_color="black")
lbl.grid(row=0,column=0)


entry1=CTkEntry(win)
entry1.grid(row=0, column=3)

btn=CTkButton(win,text="Почати тест",command=qstn)
btn.grid(row=2,column=3)



win.mainloop()




