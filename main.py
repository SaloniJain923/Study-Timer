from tkinter import *
import math

FONT = "Arial"
STUDY = 25
SHORT_BREAK = 5
LONG_BREAK = 20
rep = 0
timer = None


def reset_timer():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    rep = 0


def start_timer():
    global rep
    rep += 1
    study_sec = STUDY * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60
    if rep % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break Time")
    elif rep % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break Time")
    else:
        count_down(study_sec)
        label.config(text="Study Time")


def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count <= 9:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(time_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        study_sessions = math.floor(rep/2)
        for _ in range(study_sessions):
            mark += "✔"
        check_marks.config(text=mark)


window = Tk()
window.title("Study Timer")
window.config(padx=100, pady=50, bg="white")

label = Label(text="Timer", font=(FONT, 35, "bold"), bg="white")
label.grid(column=1, row=0)

canvas = Canvas(width=226, height=226, highlightthickness=0)
pic = PhotoImage(file="panda.png")
canvas.create_image(112, 112, image=pic)
time_text = canvas.create_text(115, 180, text="00:00", font=(FONT, 30, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg="green", bg="white")
check_marks.grid(column=1, row=3)
window.mainloop()
