# import tkinter
# from tkinter import *

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


# label_data = Label(root)

# label_data.pack(expand=True,fill='both')

# frame1 = Frame(root,bg='red')

# frame1.pack(expand=True,fill='both')

# frame2 = Frame(root,bg='blue')

# frame2.pack(expand=True,fill='both')

# frame3 = Frame(root,bg='orange')

# frame3.pack(expand=True,fill='both')

# frame4 = Frame(root,bg='green')

# frame4.pack(expand=True,fill='both')


# btn1 = Button(frame1,text='1',font=("Verdana",20))

# btn1.pack(side=LEFT,expand=True,fill='both')

# btn2 = Button(frame1,text='2',font=("Verdana",20))

# btn2.pack(side=LEFT,expand=True,fill='both')


# btn3 = Button(frame1,text='3',font=("Verdana",20))

# btn3.pack(side=LEFT,expand=True,fill='both')

# btnplus = Button(frame1,text='+',font=("Verdana",20))

# btnplus.pack(side=LEFT,expand=True,fill='both')


# btn4 = Button(frame2,text='4',font=("Verdana",20))

# btn4.pack(side=LEFT,expand=True,fill='both')

# btn5 = Button(frame2,text='5',font=("Verdana",20))

# btn5.pack(side=LEFT,expand=True,fill='both')


# btn6 = Button(frame2,text='6',font=("Verdana",20))

# btn6.pack(side=LEFT,expand=True,fill='both')

# btnminus = Button(frame2,text='-',font=("Verdana",20))

# btnminus.pack(side=LEFT,expand=True,fill='both')


# btn7 = Button(frame3,text='7',font=("Verdana",20))

# btn7.pack(side=LEFT,expand=True,fill='both')

# btn8 = Button(frame3,text='8',font=("Verdana",20))

# btn8.pack(side=LEFT,expand=True,fill='both')


# btn9 = Button(frame3,text='9',font=("Verdana",20))

# btn9.pack(side=LEFT,expand=True,fill='both')

# btnmul = Button(frame3,text='*',font=("Verdana",20))

# btnmul.pack(side=LEFT,expand=True,fill='both')


# btnC = Button(frame4,text='C',font=("Verdana",20))

# btnC.pack(side=LEFT,expand=True,fill='both')

# btn0 = Button(frame4,text='0',font=("Verdana",20))

# btn0.pack(side=LEFT,expand=True,fill='both')


# btnequal = Button(frame4,text='=',font=("Verdana",20))

# btnequal.pack(side=LEFT,expand=True,fill='both')

# btndiv = Button(frame4,text='/',font=("Verdana",20))

# btndiv.pack(side=LEFT,expand=True,fill='both')


# root.mainloop()
