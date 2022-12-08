import tkinter
from tkinter import *

# # step1 : Getting the screen

# # root = tkinter.Tk()

# # root.mainloop()

# # step2 : Add resolutions , Title for the screen..

# # root = tkinter.Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")
# # root.mainloop()


# # Step3: Dividing the screen into frames..
# # root = tkinter.Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")

# # frame1 = Frame(root,bg='red')

# # frame1.pack(expand=True,fill='both')

# # frame2 = Frame(root,bg='blue')

# # frame2.pack(expand=True,fill='both')

# # frame3 = Frame(root,bg='orange')

# # frame3.pack(expand=True,fill='both')

# # frame4 = Frame(root,bg='green')

# # frame4.pack(expand=True,fill='both')


# # root.mainloop()



# # Step4 : Creating the buttons inside the frames..

# # root = tkinter.Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")

# # frame1 = Frame(root,bg='red')

# # frame1.pack(expand=True,fill='both')

# # frame2 = Frame(root,bg='blue')

# # frame2.pack(expand=True,fill='both')

# # frame3 = Frame(root,bg='orange')

# # frame3.pack(expand=True,fill='both')

# # frame4 = Frame(root,bg='green')

# # frame4.pack(expand=True,fill='both')


# # btn1 = Button(frame1,text='1',font=("Verdana",20))

# # btn1.pack(side=LEFT,expand=True,fill='both')

# # btn2 = Button(frame1,text='2',font=("Verdana",20))

# # btn2.pack(side=LEFT,expand=True,fill='both')


# # btn3 = Button(frame1,text='3',font=("Verdana",20))

# # btn3.pack(side=LEFT,expand=True,fill='both')

# # btnplus = Button(frame1,text='+',font=("Verdana",20))

# # btnplus.pack(side=LEFT,expand=True,fill='both')


# # btn4 = Button(frame2,text='4',font=("Verdana",20))

# # btn4.pack(side=LEFT,expand=True,fill='both')

# # btn5 = Button(frame2,text='5',font=("Verdana",20))

# # btn5.pack(side=LEFT,expand=True,fill='both')


# # btn6 = Button(frame2,text='6',font=("Verdana",20))

# # btn6.pack(side=LEFT,expand=True,fill='both')

# # btnminus = Button(frame2,text='-',font=("Verdana",20))

# # btnminus.pack(side=LEFT,expand=True,fill='both')


# # btn7 = Button(frame3,text='7',font=("Verdana",20))

# # btn7.pack(side=LEFT,expand=True,fill='both')

# # btn8 = Button(frame3,text='8',font=("Verdana",20))

# # btn8.pack(side=LEFT,expand=True,fill='both')


# # btn9 = Button(frame3,text='9',font=("Verdana",20))

# # btn9.pack(side=LEFT,expand=True,fill='both')

# # btnmul = Button(frame3,text='*',font=("Verdana",20))

# # btnmul.pack(side=LEFT,expand=True,fill='both')


# # btnC = Button(frame4,text='C',font=("Verdana",20))

# # btnC.pack(side=LEFT,expand=True,fill='both')

# # btn0 = Button(frame4,text='0',font=("Verdana",20))

# # btn0.pack(side=LEFT,expand=True,fill='both')


# # btnequal = Button(frame4,text='=',font=("Verdana",20))

# # btnequal.pack(side=LEFT,expand=True,fill='both')

# # btndiv = Button(frame4,text='/',font=("Verdana",20))

# # btndiv.pack(side=LEFT,expand=True,fill='both')


# # root.mainloop()



# # Step5 : Defining the Label

# root = tkinter.Tk()

# root.geometry('450x450+300+100')

# root.resizable(0,0)

# root.title("Calculator")


# label_data = Label(root,text="This is a Label",font=("Verdana",20),anchor="se")

# label_data.pack(expand=True,fill='both')

# frame1 = Frame(root,bg='red')

# frame1.pack(expand=True,fill='both')

# frame2 = Frame(root,bg='blue')

# frame2.pack(expand=True,fill='both')

# frame3 = Frame(root,bg='orange')

# frame3.pack(expand=True,fill='both')

# frame4 = Frame(root,bg='green')

# frame4.pack(expand=True,fill='both')


# btn1 = Button(frame1,text='1',font=("Verdana",20),border=0)

# btn1.pack(side=LEFT,expand=True,fill='both')

# btn2 = Button(frame1,text='2',font=("Verdana",20),border=0)

# btn2.pack(side=LEFT,expand=True,fill='both')


# btn3 = Button(frame1,text='3',font=("Verdana",20),border=0)

# btn3.pack(side=LEFT,expand=True,fill='both')

# btnplus = Button(frame1,text='+',font=("Verdana",20),border=0)

# btnplus.pack(side=LEFT,expand=True,fill='both')


# btn4 = Button(frame2,text='4',font=("Verdana",20),border=0)

# btn4.pack(side=LEFT,expand=True,fill='both')

# btn5 = Button(frame2,text='5',font=("Verdana",20),border=0)

# btn5.pack(side=LEFT,expand=True,fill='both')


# btn6 = Button(frame2,text='6',font=("Verdana",20),border=0)

# btn6.pack(side=LEFT,expand=True,fill='both')

# btnminus = Button(frame2,text='-',font=("Verdana",20),border=0)

# btnminus.pack(side=LEFT,expand=True,fill='both')


# btn7 = Button(frame3,text='7',font=("Verdana",20),border=0)

# btn7.pack(side=LEFT,expand=True,fill='both')

# btn8 = Button(frame3,text='8',font=("Verdana",20),border=0)

# btn8.pack(side=LEFT,expand=True,fill='both')


# btn9 = Button(frame3,text='9',font=("Verdana",20),border=0)

# btn9.pack(side=LEFT,expand=True,fill='both')

# btnmul = Button(frame3,text='*',font=("Verdana",20),border=0)

# btnmul.pack(side=LEFT,expand=True,fill='both')


# btnC = Button(frame4,text='C',font=("Verdana",20),border=0)

# btnC.pack(side=LEFT,expand=True,fill='both')

# btn0 = Button(frame4,text='0',font=("Verdana",20),border=0)

# btn0.pack(side=LEFT,expand=True,fill='both')


# btnequal = Button(frame4,text='=',font=("Verdana",20),border=0)

# btnequal.pack(side=LEFT,expand=True,fill='both')

# btndiv = Button(frame4,text='/',font=("Verdana",20),border=0)

# btndiv.pack(side=LEFT,expand=True,fill='both')


# root.mainloop()


# Step6: adding the global var and functions..

root = tkinter.Tk()

root.geometry('450x450+300+100')

root.resizable(0,0)

root.title("Calculator")



data = StringVar()

label_data = Label(root,text="This is a Label",font=("Verdana",20),anchor="se",textvariable=data)

label_data.pack(expand=True,fill='both')


val = ""

def btn1_is_clicked():
    global val
    val = val+"1" # ""+"1"="1"
    data.set(val)

def btn2_is_clicked():
    global val
    val = val+"2" # ""+"1"="1"
    data.set(val)

def btn3_is_clicked():
    global val
    val = val+"3" # ""+"1"="1"
    data.set(val)

def btn4_is_clicked():
    global val
    val = val+"4" # ""+"1"="1"
    data.set(val)

def btn5_is_clicked():
    global val
    val = val+"5" # ""+"1"="1"
    data.set(val)

def btn6_is_clicked():
    global val
    val = val+"6" # ""+"1"="1"
    data.set(val)

def btn7_is_clicked():
    global val
    val = val+"7" # ""+"1"="1"
    data.set(val)

def btn8_is_clicked():
    global val
    val = val+"8" # ""+"1"="1"
    data.set(val)

def btn9_is_clicked():
    global val
    val = val+"9" # ""+"1"="1"
    data.set(val)

def btn0_is_clicked():
    global val
    val = val+"0" # ""+"1"="1"
    data.set(val)

def btnplus_is_clicked():
    global val
    val = val+"+" # ""+"1"="1"
    data.set(val)

def btnminus_is_clicked():
    global val
    val = val+"-" # ""+"1"="1"
    data.set(val)

def btnmul_is_clicked():
    global val
    val = val+"*" # ""+"1"="1"
    data.set(val)

def btndiv_is_clicked():
    global val
    val = val+"/" # ""+"1"="1"
    data.set(val)

def btnC_is_clicked():
    global val
    val = ""
    # val = val[:-1] # this is for remove the last single value..

    data.set(val)


def btnequal_is_clicked():
    global val
    val = eval(val)
    val = str(val)
    data.set(val)



frame1 = Frame(root,bg='red')

frame1.pack(expand=True,fill='both')

frame2 = Frame(root,bg='blue')

frame2.pack(expand=True,fill='both')

frame3 = Frame(root,bg='orange')

frame3.pack(expand=True,fill='both')

frame4 = Frame(root,bg='green')

frame4.pack(expand=True,fill='both')


btn1 = Button(frame1,text='1',font=("Verdana",20),border=0,command=btn1_is_clicked)

btn1.pack(side=LEFT,expand=True,fill='both',)

btn2 = Button(frame1,text='2',font=("Verdana",20),border=0,command=btn2_is_clicked)

btn2.pack(side=LEFT,expand=True,fill='both')


btn3 = Button(frame1,text='3',font=("Verdana",20),border=0,command=btn3_is_clicked)

btn3.pack(side=LEFT,expand=True,fill='both')

btnplus = Button(frame1,text='+',font=("Verdana",20),border=0,command=btnplus_is_clicked)

btnplus.pack(side=LEFT,expand=True,fill='both')


btn4 = Button(frame2,text='4',font=("Verdana",20),border=0,command=btn4_is_clicked)

btn4.pack(side=LEFT,expand=True,fill='both')

btn5 = Button(frame2,text='5',font=("Verdana",20),border=0,command=btn5_is_clicked)

btn5.pack(side=LEFT,expand=True,fill='both')


btn6 = Button(frame2,text='6',font=("Verdana",20),border=0,command=btn6_is_clicked)

btn6.pack(side=LEFT,expand=True,fill='both')

btnminus = Button(frame2,text='-',font=("Verdana",20),border=0,command=btnminus_is_clicked)

btnminus.pack(side=LEFT,expand=True,fill='both')


btn7 = Button(frame3,text='7',font=("Verdana",20),border=0,command=btn7_is_clicked)

btn7.pack(side=LEFT,expand=True,fill='both')

btn8 = Button(frame3,text='8',font=("Verdana",20),border=0,command=btn8_is_clicked)

btn8.pack(side=LEFT,expand=True,fill='both')


btn9 = Button(frame3,text='9',font=("Verdana",20),border=0,command=btn9_is_clicked)

btn9.pack(side=LEFT,expand=True,fill='both')

btnmul = Button(frame3,text='*',font=("Verdana",20),border=0,command=btnmul_is_clicked)

btnmul.pack(side=LEFT,expand=True,fill='both')


btnC = Button(frame4,text='C',font=("Verdana",20),border=0,command=btnC_is_clicked)

btnC.pack(side=LEFT,expand=True,fill='both')

btn0 = Button(frame4,text='0',font=("Verdana",20),border=0,command=btn0_is_clicked)

btn0.pack(side=LEFT,expand=True,fill='both')


btnequal = Button(frame4,text='=',font=("Verdana",20),border=0,command=btnequal_is_clicked)

btnequal.pack(side=LEFT,expand=True,fill='both')

btndiv = Button(frame4,text='/',font=("Verdana",20),border=0,command=btndiv_is_clicked)

btndiv.pack(side=LEFT,expand=True,fill='both')


root.mainloop()
