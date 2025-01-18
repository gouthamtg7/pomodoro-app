from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

reset_pressed = False
k = 1
def countdown(mins=0, seconds=5):
    global reset_pressed
    if reset_pressed == False:
        canvas.itemconfig(x, text=f"{mins}:{seconds:02d}")
        if mins>0 and seconds >0:
            if seconds==0:
                     window.after(1000, countdown, mins - 1, 59)
            else:
                # Just decrement seconds
                window.after(1000, countdown, mins, seconds - 1)
        else:
            global k
            if k%2!=0:
               break_timer(mins=0,seconds=2)
            else :
                countdown(mins=0,seconds=5)
    else :
        reset_pressed = False
def reset_timer(mins=0, seconds=0):
    canvas.itemconfig(x, text=f"{mins}:{seconds:02d}")
    global reset_pressed
    reset_pressed = True
    global text
    text = ""
    check_mark.config(text = text)


def break_timer(mins,seconds):
    global k
    k+=1
    canvas.itemconfig(x, text=f"{mins}:{seconds:02d}")
    if mins>0 or seconds >0:
         if seconds >0:
             countdown(mins=0, seconds=2)# Continue counting down the break timer
         else:
           window.after(1000, break_timer, mins, seconds - 1)
    else :
         countdown(mins=0, seconds=5)






window = Tk()
window.title("PRODUCTIVITY TIMER")
window.config(bg=YELLOW)
canvas = Canvas(width=300,height=324,bg=YELLOW, highlightthickness=1)
bg_image = PhotoImage(file="tomato.png")
img = canvas.create_image(150,172,image=bg_image)
x = canvas.create_text(150,182,text="00:00",font=(FONT_NAME,20,"bold"),fill="white")
canvas.create_text(150,40,text="TIMER",font=(FONT_NAME,40,"bold"),fill=GREEN)
canvas.grid(row=1,column=1,rowspan = 2, columnspan=1)

start_button = Button(text="Start",highlightthickness=0,bg="white",command=countdown)
start_button.grid(row=3,column=0,padx=(30,0),pady=30)

reset_button = Button(text="Reset",highlightthickness=0,bg="white",command=reset_timer)
reset_button.grid(row=3,column=3,padx=(0,30),pady=30)


check_mark = Label(text=text, bg=YELLOW)
check_mark.grid(row=3,column=1)


print("")













window.mainloop()
