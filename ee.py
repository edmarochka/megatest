from customtkinter import*
from PIL import Image
from tkinter import messagebox

win = CTk()

win.geometry("250x150")
win.title("мега тест")

def qstn():
    global qstns,n,answrs

    win.withdraw()
    win2.mainloop()
    win2.deiconify()
def qstn2():
    global btn1,qstns,answrs,n,m,rez, entry1
    if n==0 and ans.get()==2:
        rez+=1
    elif n==1 and ans.get()==1:
        rez+=1
    elif n==2 and ans.get()==1:
        rez+=1
    elif n==3 and ans.get()==3:
        rez+=1
    elif n==4 and ans.get()==1:
        rez+=1
    elif n==5 and ans.get()==1:
        rez+=1



    n=n+1
    m=m+3
    print(n)
    label_win.configure(text=qstns[n])
    answer1.configure(text=answrs[m])
    answer2.configure(text=answrs[m+1])
    answer3.configure(text=answrs[m+2])
    if n==5:
        win2.withdraw()
        messagebox.showinfo("Результат",f"Ваш результат\n{entry1.get()}:  "+str(rez))

        
qstns = ["На якому язике програмування работає Roblox?","Які є версії скриптів у Roblox Studio?","Для чого зроблен Output?","Що таке Плагіни в Roblox Studio?","Що таке Client Test?",""]
answrs = ["Python","Lua","C#","ServerScript, LocalScript, ModuleScript","Script, LocalScript, OutputScript","ModuleScript, ServerScript, VisualScript","Щоб бачити свої помилки","Щоб бачити всі текстури в проєкті","Щоб писати там код","Це вікно, яке показує ігру.","Це программа яка видаляє проєкт","Це программа яка була зробленна не роблоксом, які могуть допомогти разработчику.","Client - це тест ігри, від лиця ігрока.","Client - це тест ігри, від лиця Роблокса.","Client -  це тест ігри, від лиця разработчика.","","",""]
n=0
m=0
rez=0
win2 = CTk()

win2.geometry('600x400')
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

lbl = CTkLabel(win, text="Ваше ім'я:",font=("None",20),text_color="black")
lbl.grid(row=0,column=0)

entry1=CTkEntry(win)
entry1.grid(row=0, column=3,pady=20)

btn=CTkButton(win,text="Почати тест",command=qstn)
btn.grid(row=2,column=3,pady=20)


win.mainloop()
