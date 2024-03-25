from tkinter import *
from tkinter import messagebox
class My_entry:
    def __init__(self, font, x, y, width):
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.value = StringVar()
        self.entry = Entry(textvariable=self.value,font = self.font)
        self.entry.place(width = self.width, x = self.x, y = self.y)
class My_button:
    def __init__(self,text, font, width, x, y, win):
        self.text = text
        self.width = width
        self.font = font
        self.x = x
        self.y = y
        self.win = win
        self.button = Button(font = self.font,text=self.text, command=self.click)
        self.button.place(width=self.width, x = self.x, y = self.y)
    def click(self):
        self.value_height = self.win.entry_height.value.get()
        self.value_weight = self.win.entry_weight.value.get()
        self.value_name = self.win.entry_name.value.get()
        self.print_file()
        self.calculate_bmi()

    def calculate_bmi(self):
        name = float(self.value_name)
        height = float(self.value_height)
        weight = float(self.value_weight)
        if name == 1:
            bmi = weight + height
            self.win.label_output1.label.config(text='Сумма: {:.2f}'.format(bmi))
        elif name == 2:
            bmi = weight - height
            self.win.label_output1.label.config(text='Разность: {:.2f}'.format(bmi))
        elif name == 3:
            bmi = weight * height
            self.win.label_output1.label.config(text='Произведение: {:.2f}'.format(bmi))
        elif name ==4:
            bmi = weight / height
            self.win.label_output1.label.config(text='Частное: {:.2f}'.format(bmi))
        else:
            self.win.label_output1.label.config(text='Калькулятор принимает только знаки:-,+,*,/.')
    def print_file(self):
        file = open('new_otchet.txt', 'a', encoding='utf8')
        file.close()
class My_label:
    def __init__(self, text, font, color, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.label = Label(text = self.text, font =  self.font, bg=self.color)
        self.label.place(x = self.x, y = self.y)
class My_window:
    def __init__(self):
        self.win = Tk()
        self.win.configure(width='1000', height='400', bg='#F00044')
        self.win.resizable(width=True, height=True)
        self.__new_label()
        self.__new_entry()
        self.__new_button()
        self.win.mainloop()
    def __new_label(self):
        self.label_title = My_label('Калькалятор', "Arial 26", "#F00044", 25, 50)
        self.label_height = My_label('x1:', 'Arial 18', '#F00044', 20, 100)
        self.label_weight = My_label('Знак:', 'Arial 18', '#F00044', 20, 150)
        self.label_name = My_label('x2:', 'Arial 18', '#F00044', 20, 200)
        self.label_output1 = My_label('Результат:', 'Arial 18', '#F00044', 350, 100)
        self.label_output2 = My_label('', 'Arial 18', '#F00044', 350, 130)
    def __new_entry(self):
        self.entry_height = My_entry('Arial 18', 90, 100, 200)
        self.entry_name = My_entry('Arial 18', 90, 150, 200)
        self.entry_weight = My_entry('Arial 18', 90, 200, 200)
    def __new_button(self):
        self.button = My_button('Произвести расчет', 'Arial 12', 200, 90 ,250, self)
new_window = My_window()
