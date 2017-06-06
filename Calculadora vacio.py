from tkinter import*
#mascara
root=Tk()
root.title("calculadora")
operator=""
text_Input=StringVar()
txtDisplay=Entry(root,font=('arial',20,'bold'),
                 textvariable=text_Input,
                 bd=30,
                 insertwidth=4,
                 bg="powder blue",
                 justify='right').grid(columnspan=4)

btn1=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="1",bg="powder blue").grid(row=1,column=0)
btn2=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="2",bg="powder blue").grid(row=1,column=1)
btn3=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="3",bg="powder blue").grid(row=1,column=2)
btn4=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="4",bg="powder blue").grid(row=2,column=0)
btn5=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="5",bg="powder blue").grid(row=2,column=1)
btn6=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="6",bg="powder blue").grid(row=2,column=2)
btn7=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="7",bg="powder blue").grid(row=3,column=0)
btn8=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="8",bg="powder blue").grid(row=3,column=1)
btn9=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="9",bg="powder blue").grid(row=3,column=2)
btn0=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="0",bg="powder blue").grid(row=4,column=0)
#---------operaciones basicas-------------------------------------------
btnmenos=Button(root,padx=18,bd=8,fg="black",font=
            ('arial',20,'bold'),text="-",bg="powder blue").grid(row=1,column=3)
btnsuma=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',18,'bold'),text="+",bg="powder blue").grid(row=2,column=3)
btnmultiplicacion=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',18,'bold'),text="*",bg="powder blue").grid(row=3,column=3)
btndivision=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="/",bg="powder blue").grid(row=4,column=3)
btnresultado=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="=",bg="powder blue").grid(row=4,column=2)
btnborrar=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="c",bg="powder blue").grid(row=4,column=1)
root.mainloop()

