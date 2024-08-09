from tkinter import *

window = Tk()
window.title("DECIMAL TO BINARY CONVERTER")
window.geometry("400x500")
window.resizable(False, False)
window.config(bg="black")

# Decimal to binary conversion algorithm
def converter(num):
    binary_ver = []
    while num > 0:
        kalan = num % 2
        binary_ver.append(kalan)
        num = num // 2
    binary_ver.reverse()
    return ''.join(map(str, binary_ver))

def checking_the_number():
    try:
        num = int(expression_field.get())
        binary = converter(num)
        label2.config(text=f"Binary: {binary}")
        label3.config(text="")
    except ValueError:
        label3.config(text="Please enter a valid integer",fg="red")
    if int(expression_field.get()) == 0:
        label3.config(text="Please enter a number greater than 0",fg="red")

# Functions
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
    label2.config(text="Binary:  ")

def pad(n):
    return n

# Labels
label1 = Label(window, text="DECIMAL TO BINARY CONVERTER", font=("Arial", 12), bg="black", fg="lightblue")
label2 = Label(window, text="Your binary number will be here", font=("Arial", 15), bg="black", fg="yellow")
label3 = Label(window, text="Your status will be here", font=("Arial", 10), fg="black", bg="black")

# Buttons
button1 = Button(window, text='1', fg='black', bg='grey', command=lambda: press(1), height=2, width=5) 
button2 = Button(window, text='2', fg='black', bg='grey', command=lambda: press(2), height=2, width=5) 
button3 = Button(window, text='3', fg='black', bg='grey', command=lambda: press(3), height=2, width=5) 
button4 = Button(window, text='4', fg='black', bg='grey', command=lambda: press(4), height=2, width=5) 
button5 = Button(window, text='5', fg='black', bg='grey', command=lambda: press(5), height=2, width=5) 
button6 = Button(window, text='6', fg='black', bg='grey', command=lambda: press(6), height=2, width=5) 
button7 = Button(window, text='7', fg='black', bg='grey', command=lambda: press(7), height=2, width=5)
button8 = Button(window, text='8', fg='black', bg='grey', command=lambda: press(8), height=2, width=5) 
button9 = Button(window, text='9', fg='black', bg='grey', command=lambda: press(9), height=2, width=5) 
button0 = Button(window, text='0', fg='black', bg='grey', command=lambda: press(0), height=2, width=5) 

clear_but = Button(window, text='Clear', fg='black', bg='red', command=clear, height=2, width=5)  
check_but = Button(window, text="convert", command=checking_the_number, height=2, width=5)

# Text entry box
expression = "" 
equation = StringVar() 
expression_field = Entry(window, textvariable=equation, font=("Arial", 12), width=20)

# Place labels and entry box in the center
label1.grid(row=0, column=0, columnspan=3, pady=(60,5))
label2.grid(row=1, column=0, columnspan=3, pady=(10,5))
label3.grid(row=2, column=0, columnspan=3, pady=5)
expression_field.grid(row=3, column=0, columnspan=3, pady=(5,10),padx=(0,10))

# Place buttons in the center
button1.grid(row=4, column=0, padx=(pad(100),pad(15)), pady=5)
button2.grid(row=4, column=1, padx=(pad(15),pad(15)), pady=5)
button3.grid(row=4, column=2, padx=(pad(15),pad(110)), pady=5)
button4.grid(row=5, column=0, padx=(pad(100),pad(15)), pady=5)
button5.grid(row=5, column=1, padx=(pad(15),pad(15)), pady=5)
button6.grid(row=5, column=2, padx=(pad(15),pad(110)), pady=5)
button7.grid(row=6, column=0, padx=(pad(100),pad(15)), pady=5)
button8.grid(row=6, column=1, padx=(pad(15),pad(15)), pady=5)
button9.grid(row=6, column=2, padx=(pad(15),pad(110)), pady=5)
button0.grid(row=7, column=0, padx=(pad(100),pad(15)), pady=5)
clear_but.grid(row=7, column=1, padx=(pad(15),pad(15)), pady=5)
check_but.grid(row=7, column=2,padx=(pad(15),pad(110)), pady=5)

window.mainloop()
