import tkinter as tk

root = tk.Tk()
root.title('Máquina')

root['bg']='cyan'


largura=800 
altura=650  

linhas_quadrado=(int(altura/12))-3   
colunas_quadrado=(int((largura)/4))+7    
def desenhar():
    for i in range(-1, colunas_quadrado):
        for k in range (-1 , linhas_quadrado ):
            if ((i+k)%2==0 and not(((i%2)==0 or (k%2)==0 )) ) :





                canvas=tk.Canvas(root,width=largura,height=altura,)
           
                        


root.geometry('500x500')

label = tk.Label(root, text='Calculadora', font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=80, pady=80)



buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('Arial', 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('Arial', 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text='9', font=('Arial', 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn0 = tk.Button(buttonframe, text='0', font=('Arial', 18))
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

btnx = tk.Button(buttonframe, text='x', font=('Arial', 18))
btnx.grid(row=3, column=0, sticky=tk.W+tk.E)

btnx = tk.Button(buttonframe, text='=', font=('Arial', 18))
btnx.grid(row=3, column=2, sticky=tk.W+tk.E)





buttonframe.pack(fill='x')














root.mainloop()