from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
counter = 0
reps = 0
time = "00:00"
work_secs = 25 * 60
short_break_secs = 5 * 60 
long_break_secs = 20 * 60

def reset():
    global reps, check_marks, time
    reps = 0
    upper_text.config(text="Timer")
    check_marks.config(text="")
    timer.itemconfig(timer_text, text="00:00")
    timer.after_cancel(timer_id)

def start():
    global reps, short_break_secs, long_break_secs, work_secs, counter, time
    
    reps += 1
    if reps % 8 == 0:
        counter = long_break_secs
        upper_text.config(text="Break",foreground=PINK)
        check_marks.config(text=check_marks.cget("text") + "✔")
    elif reps % 2 == 0:
        counter = short_break_secs
        upper_text.config(text="Break",foreground=RED)
        check_marks.config(text=check_marks.cget("text") + "✔")
    elif reps % 2 ==1 :
        counter = work_secs
        upper_text.config(text="Work",foreground=GREEN)
    else:
          upper_text.config(text="Finished", foreground=GREEN)
          
    update_timer_display()
    count()

def count():
    global counter, timer_id

    if counter > 0:
        counter -= 1
        update_timer_display()
        timer_id = timer.after(1000, count)
    else:
         start()

def update_timer_display():
    minutes, seconds = divmod(counter, 60)
    time = f"{minutes:02d}:{seconds:02d}"
    timer.itemconfig(timer_text, text=time)

root = Tk()
root.config(background=YELLOW)
root.title("Pomodoro Technique")

window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

upper_text = Label(text="Timer", font=("Arial", 40, "bold"), foreground=GREEN, background=YELLOW)
upper_text.grid(column=1, row=0, pady=(25, 0))

tomato = PhotoImage(file="./tomato.png")

timer = Canvas(root, highlightthickness=0, background=YELLOW, width=200, height=220)
timer.create_image(100, 100, image=tomato)
timer_text = timer.create_text(100, 120, text=time, font=("Arial", 20, "bold"), fill=GREEN)

timer.grid(column=1, row=1, pady=(20, 0))

reset_button = Button(text="Reset", command=reset, bg=GREEN, relief=FLAT, highlightbackground=RED, borderwidth=2)
reset_button.config(cursor="hand2", width=10)
reset_button.grid(column=2, row=2, padx=20, pady=20)

start_button = Button(text="Start", command=start, bg=GREEN, relief=FLAT, highlightbackground=RED, borderwidth=2)
start_button.config(cursor="hand2", width=10)
start_button.grid(column=0, row=2, padx=20, pady=20)

check_marks = Label(text="", font=("Arial", 30, "bold"),fg=RED, bg=YELLOW)
check_marks.grid(column=1,row=3, pady=20)

root.mainloop()