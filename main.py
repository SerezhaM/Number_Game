import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

root = tk.Tk()

root.geometry(f"600x400+300+200")
root.title("Угадай число")
root.resizable(False, False)

fontExample = tkFont.Font(family="Segoe UI", size=18, weight="bold")
fontExit = tkFont.Font(family="Segoe UI", size=16, slant="italic")
fontStart = tkFont.Font(family="Segoe UI", size=20)

background_image=tk.PhotoImage(file = '/Users/sergeymashokha/PycharmProjects/Number_game/img.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

play = ''
count = 0
number_name = ''
label_enter_number = ''
label_your_number = ''
label_max = ''
label_end = ''
btn1 = ''
btn_number_yes = ''
btn_number_no = ''
btn_number_max = ''
btn_number_min = ''
btn_start = ''
btn_exit = ''
random_number = random.randint(1, 100)
number = [1, 100]



def start_game():
    global number_name
    global label_enter_number
    global btn1

    label_start.place(relx=-1, rely=-1, anchor="center")
    btn_yes.place(relx=-1, rely=-1, anchor="center")
    btn_no.place(relx=-1, rely=-1, anchor="center")

    label_enter_number = tk.Label(root, text = 'Загадай число от 1 до 100: ', font=fontExample)
    label_enter_number.place(relx=0.5, rely=0.23, anchor="center")

    number_name = tk.Entry(root, font=fontExample)
    number_name.place(relx=0.5, rely=0.3, anchor="center")

    btn1 = tk.Button(root, text='Ввести число',
                     command=check_game, font=fontExample)
    btn1.place(relx=0.5, rely=0.38, anchor="center")

    btn_reset = tk.Button(root, text='Сброс',
                        command=reset_game, font=fontExit)
    btn_reset.place(relx=0.9, rely=0.9, anchor="center")

def check_game():
    global number_name
    value = number_name.get()
    try:
        value_int = int(value)
        if (type(value_int) == int):
            if (1 <= value_int) and (value_int <= 100):
                go_game()
            else:
                messagebox.showinfo(title='Внимание', message='Число вне диапазона')
    except:
        messagebox.showinfo(title='Внимание', message='Ты ввел не число')

def go_game():
    global count
    global number_name
    global label_enter_number
    global label_your_number
    global btn1
    global random_number
    global btn_number_yes
    global btn_number_no

    label_enter_number.place(relx=-1, rely=-1, anchor="center")
    number_name.place(relx=-1, rely=-1, anchor="center")
    btn1.place(relx=-1, rely=-1, anchor="center")

    answer = f'Твое число это: {random_number}?'
    count += 1

    label_your_number = tk.Label(root, text=answer, font=fontExample)
    label_your_number.place(relx=0.5, rely=0.3, anchor="center")

    btn_number_yes = tk.Button(root, text='Да',
                     command=yes_game, font=fontExample)
    btn_number_no = tk.Button(root, text='Нет',
                     command=no_game, font=fontExample)

    btn_number_yes.place(relx=0.43, rely=0.38, anchor="center")
    btn_number_no.place(relx=0.57, rely=0.38, anchor="center")

def no_game():
    global random_number
    global label_max
    global label_your_number
    global btn_number_yes
    global btn_number_no
    global btn_number_max
    global btn_number_min

    label_your_number.place(relx=-1, rely=-1, anchor="center")
    btn_number_yes.place(relx=-1, rely=-1, anchor="center")
    btn_number_no.place(relx=-1, rely=-1, anchor="center")

    answer = f'Твое число больше или меньше, чем {random_number}?'

    label_max = tk.Label(root, text=answer, font=fontExample)
    label_max.place(relx=0.5, rely=0.3, anchor="center")

    btn_number_max = tk.Button(root, text='Больше',
                               command=max, font=fontExample)
    btn_number_min = tk.Button(root, text='Меньше',
                              command=min, font=fontExample)

    btn_number_max.place(relx=0.38, rely=0.38, anchor="center")
    btn_number_min.place(relx=0.62, rely=0.38, anchor="center")


def max():
    global number
    global random_number
    global label_max
    global btn_number_max
    global btn_number_min

    btn_number_max.place(relx=-1, rely=-1, anchor="center")
    btn_number_min.place(relx=-1, rely=-1, anchor="center")
    label_max.place(relx=-1, rely=-1, anchor="center")

    number[0] = random_number
    random_number = (number[0] + number[1]) // 2

    go_game()

def min():
    global number
    global random_number
    global label_max
    global btn_number_max
    global btn_number_min

    btn_number_max.place(relx=-1, rely=-1, anchor="center")
    btn_number_min.place(relx=-1, rely=-1, anchor="center")
    label_max.place(relx=-1, rely=-1, anchor="center")

    number[1] = random_number
    random_number = (number[0] + number[1]) // 2

    go_game()

def yes_game():
    global count
    global label_end
    global btn_number_yes
    global btn_number_no
    global btn_number_max
    global btn_number_min
    global btn_start
    global btn_exit

    btn_number_yes.place(relx=-1, rely=-1, anchor="center")
    btn_number_no.place(relx=-1, rely=-1, anchor="center")
    btn_number_max.place(relx=-1, rely=-1, anchor="center")
    btn_number_min.place(relx=-1, rely=-1, anchor="center")

    label_end = tk.Label(root, text=f'Ура, я угадал твое число с {count} попыток! \n Сыграем еще раз?', font=fontExample)
    label_end.place(relx=0.5, rely=0.3, anchor="center")

    btn_start = tk.Button(root, text='Сыграть еще раз',
                               command=reset_game, font=fontExample)
    btn_exit = tk.Button(root, text='Выход',
                               command=exit, font=fontExit)

    btn_start.place(relx=0.5, rely=0.5, anchor="center")
    btn_exit.place(relx=0.5, rely=0.6, anchor="center")

def reset_game():
    global count
    global number
    global random_number
    global number_name
    global label_enter_number
    global label_your_number
    global label_max
    global label_end
    global btn1
    global btn_number_yes
    global btn_number_no
    global btn_number_max
    global btn_number_min
    global btn_start
    global btn_exit

    try:
        count = 0
        number = [1, 100]
        random_number = random.randint(1, 100)
    except:
        pass

    try:
        number_name = ''
        number_name.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        label_start.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        label_end.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        label_max.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        label_enter_number.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        label_your_number.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_yes.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_no.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_number_yes.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_number_no.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
       btn_number_max.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_number_min.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_start.place(relx=-1, rely=-1, anchor="center")
    except:
        pass

    try:
        btn_exit.place(relx=-1, rely=-1, anchor="center")
    except:
        pass
    start_game()
#----

label_start = tk.Label(root, text='Вы хотите сыграть в игру?', font=fontExample)
label_start.place(relx=0.5, rely=0.5, anchor="center")

btn_yes = tk.Button(root, text='Да',
                 command=start_game, font=fontExit)
btn_no = tk.Button(root, text='Нет',
                 command=exit, font=fontExit)

btn_yes.place(relx=0.43, rely=0.6, anchor="center")
btn_no.place(relx=0.57, rely=0.6, anchor="center")

root.mainloop()