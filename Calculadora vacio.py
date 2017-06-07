from builtins import eval
from tkinter import*
import math
#funciones
def Boton(numero):
    global operador
    operador = operador + str(numero)
    text_Input.set(operador)
def limpiar():
    global operador
    operador = ""
    text_Input.set("")
def resultado():
    global operador
    resp = str(eval(operador))
    print(operador)
    text_Input.set(resp)
    operador = ""

#mascara
root=Tk()
root.title("calculadora")
operador=""
text_Input=StringVar()
txtDisplay=Entry(root,font=('arial',20,'bold'),
                 textvariable=text_Input,
                 bd=30,
                 width=31,
                 bg="powder blue",
                 justify='right').grid(columnspan=5)

btn1=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",width=4,
            bg="powder blue",command=lambda:Boton(1)).grid(row=1,column=0)

btn2=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",width=4,
            bg="powder blue",command=lambda:Boton(2)).grid(row=1,column=1)

btn3=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",width=4,
            bg="powder blue",command=lambda:Boton(3)).grid(row=1,column=2)

btn4=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",width=4,
            bg="powder blue",command=lambda:Boton(4)).grid(row=2,column=0)

btn5=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",width=4,
            bg="powder blue",command=lambda:Boton(5)).grid(row=2,column=1)

btn6=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",width=4,
            bg="powder blue",command=lambda:Boton(6)).grid(row=2,column=2)

btn7=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",width=4,
            bg="powder blue",command=lambda:Boton(7)).grid(row=3,column=0)

btn8=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",width=4,
            bg="powder blue",command=lambda:Boton(8)).grid(row=3,column=1)

btn9=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",width=4,
            bg="powder blue",command=lambda:Boton(9)).grid(row=3,column=2)

btn0=Button(root,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",width=4,
            bg="powder blue",command=lambda:Boton(0)).grid(row=4,column=0)
#---------operaciones basicas-------------------------------------------
btnmenos=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="-", width=2,bg="powder blue",command = lambda: Boton("-")).grid(row=1,column=3)
btnsuma=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="+", width=2,bg="powder blue",command = lambda: Boton("+")).grid(row=2,column=3)
btnmultiplicacion=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="*", width=2,bg="powder blue",command = lambda: Boton("*")).grid(row=3,column=3)
btndivision=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="/", width=2,bg="powder blue",command = lambda: Boton("/")).grid(row=4,column=3)
btnresultado=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="=", width=4,bg="powder blue",command= resultado).grid(row=4,column=2)
btnborrar=Button(root,padx=16,bd=8,fg="black",font=
            ('arial',20,'bold'),text="c", width=4,bg="powder blue",command=limpiar).grid(row=4,column=1)
bntSen = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "sen", width=4, bg = "powder blue", command = lambda: Boton("math.sin")).grid(row = 5, column = 0)
bntCos = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "cos", width=4,bg = "powder blue", command = lambda: Boton("math.cos")).grid(row = 5, column = 1)
bntTan = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "tan", width=4,bg = "powder blue", command = lambda: Boton("math.tan")).grid(row = 5, column = 2)
bntLog = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "log", width=7,bg = "powder blue", command = lambda: Boton("math.log")).grid(row = 5, column = 3,columnspan=2)
btnpotencia = Button(root, padx = 16, bd = 8, fg = "black", font =
                     ('arial', 20, 'bold'), text = "^", width=2, bg = "powder blue", command = lambda: Boton("**")).grid(row = 1, column = 4)

btnraiz = Button(root, padx = 16, bd = 8, fg = "black", font =
                     ('arial', 20, 'bold'), text = "√", width=2, bg = "powder blue", command = lambda: Boton("math.sqrt")).grid(row = 2, column = 4)

btnparentecisizq = Button(root, padx = 16, bd = 8, fg = "black", font =
                     ('arial', 20, 'bold'), text = "(", width=2,bg = "powder blue", command = lambda: Boton("(")).grid(row = 3, column = 4)

btnparentecisder = Button(root, padx = 16, bd = 8, fg = "black", font =
                     ('arial', 20, 'bold'), text = ")", width=2,bg = "powder blue", command = lambda: Boton(")")).grid(row = 4, column = 4)

bntSenh = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "senh", width=4, bg = "powder blue", command = lambda: Boton("math.sinh")).grid(row = 6, column = 0)
bntCosh = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "cosh", width=4,bg = "powder blue", command = lambda: Boton("math.cosh")).grid(row = 6, column = 1)
bntTanh = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "tanh", width=14,bg = "powder blue", command = lambda: Boton("math.tanh")).grid(row = 6, column = 2,columnspan=3)

bntASen = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "ArcSen", width=4, bg = "powder blue", command = lambda:Boton("math.asin")).grid(row = 7, column = 0)
bntACos = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "ArcCos", width=4,bg = "powder blue", command = lambda: Boton("math.acos")).grid(row = 7, column = 1)
bntATan = Button(root, padx = 16, bd = 8, fg = "black", font =
            ('arial', 20, 'bold'),text = "ArcTan", width=14,bg = "powder blue", command = lambda: Boton("math.atan")).grid(row = 7, column = 2,columnspan= 3)

root.mainloop()

