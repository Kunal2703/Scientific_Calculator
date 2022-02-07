from tkinter import *
from math import *

class calculate:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("500x610")
        self.root.config(bg="#607B8B")
        self.root.maxsize(500, 610)
        self.root.minsize(500, 610)
        self.resultwindow = Entry(self.root, borderwidth=15, width=41, relief=SUNKEN)
        self.resultwindow.grid(row=0, column=0, columnspan=10, pady=10)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()

        # Buttons
        self.buttonlog10 = Button(self.root, text="log10", width=8, height=3,
                                  command=lambda: self.btn('log10('),
                                  relief=RAISED,
                                  bg='light green')
        self.buttonlog10.grid(row=1, column=0, padx=5, pady=5)
        self.buttonlog10.config(font=("Arial", 18))
        self.buttonexp = Button(self.root, text="exp", width=8, height=3,
                                command=lambda: self.btn('exp('),
                                relief=RAISED,
                                bg='light green')
        self.buttonexp.grid(row=1, column=1, padx=3, pady=3)
        self.buttonexp.config(font=("Arial", 18))
        self.buttonsin = Button(self.root, text="sin", width=8, height=3,
                                command=lambda: self.btn('sin('),
                                relief=RAISED,
                                bg='light green')
        self.buttonsin.grid(row=1, column=2, padx=3, pady=3)
        self.buttonsin.config(font=("Arial", 18))
        self.buttoncos = Button(self.root, text="cos", width=8, height=3,
                                command=lambda: self.btn('cos('),
                                relief=RAISED,
                                bg='#FFEE58')
        self.buttoncos.grid(row=1, column=3, padx=3, pady=3)
        self.buttoncos.config(font=("Arial", 18))
        self.buttontan = Button(self.root, text="tan", width=8, height=3,
                                command=lambda: self.btn('tan('),
                                relief=RAISED,
                                bg='#FFEE58')
        self.buttontan.grid(row=1, column=4, padx=3, pady=3)
        self.buttontan.config(font=("Arial", 18))
        self.buttonlog2 = Button(self.root, text="log2", width=8, height=3,
                                 command=lambda: self.btn('log2('),
                                 relief=RAISED,
                                 bg='light green')
        self.buttonlog2.grid(row=2, column=0, padx=5, pady=5)
        self.buttonlog2.config(font=("Arial", 18))
        self.buttonradians = Button(self.root, text="radians", width=8, height=3,
                                    command=lambda: self.btn('radians('),
                                    relief=RAISED,
                                    bg='light green')
        self.buttonradians.grid(row=2, column=1, padx=3, pady=3)
        self.buttonradians.config(font=("Arial", 18))
        self.buttonasin = Button(self.root, text="asin", width=8, height=3,
                                 command=lambda: self.btn('asin('),
                                 relief=RAISED,
                                 bg='light green')
        self.buttonasin.grid(row=2, column=2, padx=3, pady=3)
        self.buttonasin.config(font=("Arial", 18))
        self.buttonacos = Button(self.root, text="acos", width=8, height=3,
                                 command=lambda: self.btn('acos('),
                                 relief=RAISED,
                                 bg='#FFEE58')
        self.buttonacos.grid(row=2, column=3, padx=3, pady=3)
        self.buttonacos.config(font=("Arial", 18))
        self.buttonatan = Button(self.root, text="atan", width=8, height=3,
                                 command=lambda: self.btn('atan('),
                                 relief=RAISED,
                                 bg='#FFEE58')
        self.buttonatan.grid(row=2, column=4, padx=3, pady=3)
        self.buttonatan.config(font=("Arial", 18))
        self.buttonfactorial = Button(self.root, text="factorial", width=8, height=3,
                                      command=lambda: self.btn('factorial('),
                                      relief=RAISED,
                                      bg='light green')
        self.buttonfactorial.grid(row=3, column=0, padx=5, pady=5)
        self.buttonfactorial.config(font=("Arial", 18))
        self.buttonpow = Button(self.root, text="pow", width=8, height=3,
                                command=lambda: self.btn('pow('),
                                relief=RAISED,
                                bg='light green')
        # ------> pow(9,3) = 729

        self.buttonpow.grid(row=3, column=1, padx=3, pady=3)
        self.buttonpow.config(font=("Arial", 18))
        self.buttonsqrt = Button(self.root, text="sqrt", width=8, height=3,
                                 command=lambda: self.btn('sqrt('),
                                 relief=RAISED,
                                 bg='light green')
        self.buttonsqrt.grid(row=3, column=2, padx=3, pady=3)
        self.buttonsqrt.config(font=("Arial", 18))
        self.buttondiv = Button(self.root, text="/", width=8, height=3,
                                command=lambda: self.btn('/'),
                                relief=RAISED,
                                bg='#FFEE58')
        self.buttondiv.grid(row=3, column=3, padx=3, pady=3)
        self.buttondiv.config(font=("Arial", 18))
        self.buttonmod = Button(self.root, text="%", width=8, height=3,
                                command=lambda: self.btn('%'),
                                relief=RAISED,
                                bg='#FFEE58')
        self.buttonmod.grid(row=3, column=4, padx=3, pady=3)
        self.buttonmod.config(font=("Arial", 18))
        self.button1 = Button(self.root, text="1", width=8, height=3, command=lambda:
        self.btn('1'), relief=RAISED,
                              bg='light green')
        self.button1.grid(row=4, column=0, padx=5, pady=5)
        self.button1.config(font=("Arial", 18))
        self.button2 = Button(self.root, text="2", width=8, height=3, command=lambda:
        self.btn('2'), relief=RAISED,
                              bg='light green')
        self.button2.grid(row=4, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))
        self.button3 = Button(self.root, text="3", width=8, height=3, command=lambda:
        self.btn('3'), relief=RAISED,
                              bg='light green')
        self.button3.grid(row=4, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))
        self.button4 = Button(self.root, text="4", width=8, height=3, command=lambda:
        self.btn('4'), relief=RAISED,
                              bg='light green')
        self.button4.grid(row=5, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))
        self.button5 = Button(self.root, text="5", width=8, height=3, command=lambda:
        self.btn('5'), relief=RAISED,
                              bg='light green')
        self.button5.grid(row=5, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))
        self.button6 = Button(self.root, text="6", width=8, height=3, command=lambda:
        self.btn('6'), relief=RAISED,
                              bg='light green')
        self.button6.grid(row=5, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))
        self.button7 = Button(self.root, text="7", width=8, height=3, command=lambda:
        self.btn('7'), relief=RAISED,
                              bg='light green')
        self.button7.grid(row=6, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))
        self.button8 = Button(self.root, text="8", width=8, height=3, command=lambda:
        self.btn('8'), relief=RAISED,
                              bg='light green')
        self.button8.grid(row=6, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))
        self.button9 = Button(self.root, text="9", width=8, height=3, command=lambda:
        self.btn('9'), relief=RAISED,
                              bg='light green')
        self.button9.grid(row=6, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="0", width=8, height=3, command=lambda:
        self.btn('0'), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=7, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button_open = Button(self.root, text="(", width=8, height=3,
                                  command=lambda: self.btn('('), relief=RAISED)
        self.button_open.grid(row=7, column=1, padx=3, pady=3)
        self.button_open.config(font=("Arial", 18))
        self.button_close = Button(self.root, text=")", width=8, height=3,
                                   command=lambda: self.btn(')'), relief=RAISED)
        self.button_close.grid(row=7, column=2, padx=3, pady=3)
        self.button_close.config(font=("Arial", 18))

        # Operations Buttons
        self.buttonplus = Button(self.root, text="+", width=8, height=3,
                                 command=lambda: self.btn('+'), relief=RAISED)
        self.buttonplus.grid(row=4, column=3, padx=3, pady=3)
        self.buttonplus.config(font=("Arial", 18))
        self.buttonminus = Button(self.root, text="-", width=8, height=3,
                                  command=lambda: self.btn('-'), relief=RAISED)
        self.buttonminus.grid(row=4, column=4, padx=3, pady=3)
        self.buttonminus.config(font=("Arial", 18))
        self.buttondivide = Button(self.root, text="•", width=8, height=3,
                                   command=lambda: self.btn('.'), relief=RAISED)
        self.buttondivide.grid(row=5, column=3, padx=3, pady=3)
        self.buttondivide.config(font=("Arial", 18))
        self.buttonmultiply = Button(self.root, text="", width=8, height=3,
                                     command=lambda: self.btn(''),
                                     relief=RAISED)
        self.buttonmultiply.grid(row=5, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))
        self.buttoncancel = Button(self.root, text="AC", width=8, height=3,
                                   command=lambda: self.cancel(),
                                   relief=RAISED,
                                   bg='#EF5350', fg='black')
        self.buttoncancel.grid(row=6, column=4, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))
        self.buttondeleteall = Button(self.root, text="DEL", width=8, height=3,
                                      command=lambda: self.delete_all(),
                                      relief=RAISED)
        self.buttondeleteall.grid(row=6, column=3, padx=3, pady=3)
        self.buttondeleteall.config(font=("Arial", 18))
        self.buttonresult = Button(self.root, text="=", width=17, height=3,
                                   command=lambda: self.calculate(),
                                   relief=RAISED,
                                   bg='#FFEE58')
        self.buttonresult.grid(row=7, column=3, padx=3, pady=3, columnspan=2)
        self.buttonresult.config(font=("Arial", 18))
        self.root.mainloop()

    def btn(self, val):
        self.resultwindow.insert(END, val)

    def cancel(self):
        self.resultwindow.delete(0, 'end')

    def delete_all(self):
        x = self.resultwindow.get()
        self.resultwindow.delete(0, 'end')
        y = x[:-1]
        self.resultwindow.insert(0, y)

    def calculate(self):
        x = self.resultwindow.get()
        answer = eval(x)
        self.resultwindow.delete(0, 'end')
        self.resultwindow.insert(0, answer)


if __name__ == "__main__":
    calculate()
