from tkinter import *
import winsound
import sys
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label1.config(text='Timer')
    checkmark_label2.config(text='')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps<=8:
        if reps==8:
            count_down(long_break_sec)
            title_label1.config(text='Break',fg=RED)

        elif reps%2==1:
            count_down(work_sec)
            title_label1.config(text='Work', fg=GREEN)
        else:
            count_down(short_break_sec)
            title_label1.config(text='Break', fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_sec=count%60
    if count_sec<10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text,text=f'{count//60}:{count_sec}')
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        winsound.MessageBeep()
        start_timer()
        if reps%2==0:
            t=reps//2*'✓'
            checkmark_label2.config(text=t)


# ---------------------------- UI SETUP ------------------------------- #

def get_image_path(filename):
    if getattr(sys, 'frozen', False):
        # 如果程序是打包成了单个文件
        base_path = sys._MEIPASS
    else:
        # 如果程序是从脚本运行
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)

window=Tk()
window.title('tomato')
window.config(padx=100,pady=50,bg=YELLOW)
window.after(1000,)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file=get_image_path('tomato.png'))
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)


title_label1=Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label1.grid(row=0,column=1)

checkmark_label2=Label(text='',fg=GREEN,bg=YELLOW)
checkmark_label2.grid(row=3,column=1)

button_start=Button(text='Start',highlightthickness=0,command=start_timer)
button_start.grid(row=2,column=0)


button_reset=Button(text='Reset',highlightthickness=0,command=reset_timer)
button_reset.grid(row=2,column=2)


window.mainloop()