import math
import tkinter
from tkinter import font

window = tkinter.Tk()

# 设置窗口名称
window.title('calculator')
# 设置窗口大小
window.geometry('395x675')
# 设置窗口背景颜色
window.config(background='#000000')

# 设置当前显示的数字'0'
current_number = tkinter.StringVar()
current_number.set('0')

# 是否按下运算符
IS_CALC = False

# 显示框最多显示多少个字符
MAX_SHOW_LEN = 8

# 设置计算器显示区域
label = tkinter.Label(window, textvariable=current_number,
                      fg='#ffffff', bg='#000000', font=('firacode', 50), anchor='se')
label.place(x=15, y=0, width=365, height=200)


# 按下数字键位
def press_number(number):
    if current_number.get() == '0':
        # 按下'0'，不增加数字
        current_number.set(number)
    elif len(current_number.get()) <= MAX_SHOW_LEN:
        current_number.set(current_number.get() + number)


# 按下小数点
def press_decimal_point(point):
    pass


    # 设置按钮
button1_1 = tkinter.Button(
    window, text='AC', font=('firacode', 23), bg='#a5a5a5')
button1_1.place(x=15, y=200, width=80, height=80)

button1_2 = tkinter.Button(
    window, text='+/-', font=('firacode', 23), bg='#a5a5a5')
button1_2.place(x=110, y=200, width=80, height=80)

button1_3 = tkinter.Button(
    window, text='%', font=('firacode', 23), bg='#a5a5a5')
button1_3.place(x=205, y=200, width=80, height=80)

button1_4 = tkinter.Button(
    window, text='/', font=('firacode', 23), bg='#efa53c', fg='#ffffff')
button1_4.place(x=300, y=200, width=80, height=80)

button2_1 = tkinter.Button(
    window, text='7', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('7'))
button2_1.place(x=15, y=295, width=80, height=80)

button2_2 = tkinter.Button(
    window, text='8', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('8'))
button2_2.place(x=110, y=295, width=80, height=80)

button2_3 = tkinter.Button(
    window, text='9', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('9'))
button2_3.place(x=205, y=295, width=80, height=80)

button2_4 = tkinter.Button(
    window, text='*', font=('firacode', 23), bg='#efa53c', fg='#ffffff')
button2_4.place(x=300, y=295, width=80, height=80)

button3_1 = tkinter.Button(
    window, text='4', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('4'))
button3_1.place(x=15, y=390, width=80, height=80)

button3_2 = tkinter.Button(
    window, text='5', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('5'))
button3_2.place(x=110, y=390, width=80, height=80)

button3_3 = tkinter.Button(
    window, text='6', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('6'))
button3_3.place(x=205, y=390, width=80, height=80)

button3_4 = tkinter.Button(
    window, text='-', font=('firacode', 23), bg='#efa53c', fg='#ffffff')
button3_4.place(x=300, y=390, width=80, height=80)

button4_1 = tkinter.Button(
    window, text='3', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('3'))
button4_1.place(x=15, y=485, width=80, height=80)

button4_2 = tkinter.Button(
    window, text='2', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('2'))
button4_2.place(x=110, y=485, width=80, height=80)

button4_3 = tkinter.Button(
    window, text='1', font=('firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('1'))
button4_3.place(x=205, y=485, width=80, height=80)

button4_4 = tkinter.Button(
    window, text='+', font=('firacode', 23), bg='#efa53c', fg='#ffffff')
button4_4.place(x=300, y=485, width=80, height=80)

button5_1 = tkinter.Button(window, text='0', font=(
    'firacode', 23), bg='#333333', fg='#ffffff', command=lambda: press_number('0'))
button5_1.place(x=15, y=580, width=175, height=80)

button5_2 = tkinter.Button(window, text='.', font=(
    'firacode, 23'), bg='#333333', fg='#ffffff', command=lambda: press_decimal_point('.'))
button5_2.place(x=205, y=580, width=80, height=80)

button5_3 = tkinter.Button(window, text='=', font=(
    'firacode, 23'), bg='#efa53c', fg='#ffffff')
button5_3.place(x=300, y=580, width=80, height=80)


window.mainloop()
