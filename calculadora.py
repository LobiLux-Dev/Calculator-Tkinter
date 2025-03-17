import tkinter as tk
from tkinter import StringVar

ventana=tk.Tk()
ventana.title("Calculadora :3")
ventana.geometry("445x550")

#tamaño de los botones
anch = 8
larg = 3

#botones 
def click(num):
    global operador
    operador= operador+ str(num)
    a.set(operador)
    
# funciones de las operaciones de cada boton
def click(num):
    global operador
    operador=operador+str(num)
    a.set(operador)

def clear():
    global operador
    operador=""
    a.set(operador)

def operacion():
    global operador
    try:
        opera=eval(operador)
    except:
        clear()
        opera=("ERROR")
    a.set(opera)
    
a= StringVar()
campo1 = StringVar()
campo2 = StringVar()
campo3 = StringVar()
operador=""


botonraiz = tk.Button(ventana, text="√", width=anch, height=larg, command=lambda: click("√"))
botonraiz.place(x=1, y=85)
botonexpo = tk.Button(ventana, text="EXP", width=anch, height=larg, command=lambda: click("**"))
botonexpo.place(x=90, y=85)
botonlog = tk.Button(ventana, text="log", width=anch, height=larg, command=lambda: click("log10("))
botonlog.place(x=179, y=85)
botonln = tk.Button(ventana, text="ln", width=anch, height=larg, command=lambda: click("log("))
botonln.place(x=268, y=85)
botonsin = tk.Button(ventana, text="sin", width=anch, height=larg, command=lambda: click("sin("))
botonsin.place(x=357, y=85)

botoncos = tk.Button(ventana, text="cos", width=anch, height=larg, command=lambda: click("cos("))
botoncos.place(x=1, y=143)
botontan = tk.Button(ventana, text="tan", width=anch, height=larg, command=lambda: click("tan("))
botontan.place(x=90, y=143)
botonarcsin = tk.Button(ventana, text="asin", width=anch, height=larg, command=lambda: click("asin("))
botonarcsin.place(x=179, y=143)
botonarccos = tk.Button(ventana, text="acos", width=anch, height=larg, command=lambda: click("acos("))
botonarccos.place(x=268, y=143)
botonarctan = tk.Button(ventana, text="atan", width=anch, height=larg, command=lambda: click("atan("))
botonarctan.place(x=357, y=143)
botonarctan = tk.Button(ventana, text="arctan", width=anch, height=larg, command=lambda: click("atan("))
botonarctan.place(x=357, y=143)
botonsec = tk.Button(ventana, text="sec", width=anch, height=larg, command=lambda: click("1/cos("))
botonsec.place(x=1, y=201)
botoncsc = tk.Button(ventana, text="csc", width=anch, height=larg, command=lambda: click("1/sin("))
botoncsc.place(x=90, y=201)
botoncot = tk.Button(ventana, text="cot", width=anch, height=larg, command=lambda: click("1/tan("))
botoncot.place(x=179, y=201)
botonpariz = tk.Button(ventana, text="(", width=anch, height=larg, command=lambda: click("("))
botonpariz.place(x=268, y=201)
botonparde = tk.Button(ventana, text=")", width=anch, height=larg, command=lambda: click(")"))
botonparde.place(x=357, y=201)

boton7 = tk.Button(ventana, text="7", width=anch, height=larg, command=lambda: click(7))
boton7.place(x=1, y=259)
boton8 = tk.Button(ventana, text="8", width=anch, height=larg, command=lambda: click(8))
boton8.place(x=90, y=259)
boton9 = tk.Button(ventana, text="9", width=anch, height=larg, command=lambda: click(9))
boton9.place(x=179, y=259)
botonAC = tk.Button(ventana, text="AC", width=anch, height=larg, command=clear)
botonAC.place(x=268, y=259)
botonDEL = tk.Button(ventana, text="DEL", width=anch, height=larg, command=lambda: click("remove"))
botonDEL.place(x=357, y=259)
boton4 = tk.Button(ventana, text="4", width=anch, height=larg, command=lambda: click(4))
boton4.place(x=1, y=317)
boton5 = tk.Button(ventana, text="5", width=anch, height=larg, command=lambda: click(5))
boton5.place(x=90, y=317)
boton6 = tk.Button(ventana, text="6", width=anch, height=larg, command=lambda: click(6))
boton6.place(x=179, y=317)
botonmult = tk.Button(ventana, text="x", width=anch, height=larg, command=lambda: click("*"))
botonmult.place(x=268, y=317)
botondivi = tk.Button(ventana, text="/", width=anch, height=larg, command=lambda: click("/"))
botondivi.place(x=357, y=317)

boton1 = tk.Button(ventana, text="1", width=anch, height=larg, command=lambda: click(1))
boton1.place(x=1, y=375)
boton2 = tk.Button(ventana, text="2",width=anch, height=larg, command=lambda: click(2))
boton2.place(x=90, y=375)
boton3 = tk.Button(ventana, text="3", width=anch, height=larg, command=lambda: click(3))
boton3.place(x=179, y=375)
botonsuma = tk.Button(ventana, text="+", width=anch, height=larg, command=lambda: click("+"))
botonsuma.place(x=268, y=375)
botonresta = tk.Button(ventana, text="-", width=anch, height=larg, command=lambda: click("-"))
botonresta.place(x=357, y=375)

boton0 = tk.Button(ventana, text="0", width=anch, height=larg, command=lambda: click(0))
boton0.place(x=1, y=433)
botoncoma = tk.Button(ventana, text=".", width=anch, height=larg, command=lambda: click("."))
botoncoma.place(x=90, y=433)
botonpi = tk.Button(ventana, text="π", width=anch, height=larg, command=lambda: click("pi"))
botonpi.place(x=179, y=433)
botonporc = tk.Button(ventana, text="%", width=anch, height=larg, command=lambda: click("%"))
botonporc.place(x=268, y=433)
botonres1 = tk.Button(ventana, text="=", width=anch, height=larg, command=operacion)
botonres1.place(x=357, y=433)

entrada1 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo1, width=30, bd=5,insertwidth=3, bg="powder blue",justify="left")
entrada1.place(x=5, y=4)
efix = tk.Label(ventana, text=":Infix", font=("Arial", 14))
efix.place(x=350, y=5)
entrada2 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo2, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
entrada2.place(x=5, y=45)
epos = tk.Label(ventana, text=":Postfix", font=("Arial", 14))
epos.place(x=350, y=45)
entrada3 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo3, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
entrada3.place(x=5, y=500)
r = tk.Label(ventana, text=":Resultado", font=("Arial", 14))
r.place(x=346, y=500)




ventana.mainloop()


















