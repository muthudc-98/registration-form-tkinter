from tkinter import *

a=Tk()
a.geometry('1000x750')
a.title('Registration form')
a.configure(bg='purple')

def form():
    global get1,get2,get3,get4,get5
    get1=entry1.get()
    get2=entry2.get()
    get3=entry3.get()
    get4=entry4.get()
    get5=entry5.get()
    result=Text(a, height=6, width=30)
    result.insert(INSERT,get1  )
    result.insert(INSERT,get2 )
    result.insert(INSERT,get3 )
    result.insert(INSERT,get4 )
    result.place(x=200,y=520)

a1=Label(a,text='Registration form: ', background='white', foreground='black',font=('Times new roman',20,'bold') )
a1.place(x=320,y=20)

name1=Label(a,text='Name: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name1.place(x=100,y=100)
entry1=Entry(a,width=25)
entry1.place(x=250,y=102)

name2=Label(a,text='Department: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name2.place(x=100,y=150)
entry2=Entry(a,width=25)
entry2.place(x=250,y=152)

name3=Label(a,text='Address: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name3.place(x=100,y=200)
entry3=Entry(a,width=25)
entry3.place(x=250,y=202)

name4=Label(a,text='Age: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name4.place(x=100,y=250)
entry4=Entry(a,width=25)
entry4.place(x=250,y=252)

name5=Label(a,text='Gender: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name5.place(x=100,y=300)
entry5=Entry(a,width=25)
entry5.place(x=250,y=302)

name6=Label(a,text='Qualification: ', background='white', foreground='black',font=('Times new roman',13,'bold'))
name6.place(x=100,y=350)
entry6=Entry(a,width=25)
entry6.place(x=250,y=352)

sub=Button(a,text='Submit: ',command=form, background='green', foreground='white',font=('Times new roman',13,'bold'),height=1,width=7 )
sub.place(x=400,y=450)

a.mainloop()