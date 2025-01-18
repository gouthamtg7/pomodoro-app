from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
text = ""
reset_pressed = False
#Countdown Mechanism
cycles = 0
notification_window = None

def show_notification(mins,seconds):
    global notification_window
    if notification_window is None:
        notification_window = Toplevel(window)
        notification_window.title("Reminder")
        notification_window.geometry("600x600")
        notification_window.configure(bg=YELLOW)
        label = Label(notification_window, text="Only 2 minutes left!", bg=YELLOW, font=(FONT_NAME, 20))
        label.pack(pady=20)
        notification_window.attributes('-topmost', True)
        notification_label = Label(notification_window, text=f"{mins:02d}:{seconds:02d}", bg=YELLOW,
                                   font=(FONT_NAME, 20))
        notification_label.pack(pady=20)
        notification_window.attributes('-topmost', True)  # Keep it on top

        # Update the timer in the notification window
    notification_label.config(text=f"{mins:02d}:{seconds:02d}")




def start_countdown(mins=24, seconds=59):
    global cycles
    global text
    global notification_window
    if len(text)<24:
        global reset_pressed
        if reset_pressed == False:
            canvas.itemconfig(x, text=f"{mins:02d}:{seconds:02d}")
            if mins == 0 and seconds <= 120 and seconds > 0:
                show_notification(mins,seconds)
            if seconds <= 0:
                if mins > 0 and seconds == 0:
                    window.after(1000, start_countdown, mins-1, 59)

                else:
                    if cycles % 2 == 0:
                        take_break(4,59)
                    else:
                        canvas.itemconfig(timer_heading, text="TIMER")
                        canvas.itemconfig(timer_heading, fill=GREEN)
                        canvas.itemconfig(timer_heading, font=(FONT_NAME, 40, "bold"))
                        start_countdown(24, 59)
                        cycles += 1
                        global notification_window
                        if notification_window is not None:
                            notification_window.destroy()
                            notification_window = None

            else:
                window.after(1000, start_countdown, mins, seconds - 1)
        else:
            reset_pressed = False
    else :
        canvas.itemconfig(timer_heading, text="")
        canvas.itemconfig(x,text="TIME UP!!")
        if notification_window is not None:
            notification_window.destroy()


def take_break(mins = 4,seconds=59):
        global cycles
        canvas.itemconfig(timer_heading,text="Your Break Ends In")
        canvas.itemconfig(timer_heading,fill= "red")
        canvas.itemconfig(timer_heading,font=(FONT_NAME,20,"normal"))
        if cycles % 2 == 0:
            cycles += 1
            start_countdown(4,59)
        global text
        text += "✔️"
        check_mark.config(text=text)


def reset(mins=0,seconds=0):
    canvas.itemconfig(x, text=f"{mins:02d}:{seconds:02d}")
    global reset_pressed
    reset_pressed = True
    global text
    text = ""
    check_mark.config(text=text)
    global notification_window
    if notification_window is not None:
        notification_window.destroy()
        notification_window = None


#Create the window
window = Tk()
window.title("PRODUCTIVITY TIMER")
window.config(bg=YELLOW)

#Create the canvas
canvas = Canvas(width=300,height=324,bg=YELLOW, highlightthickness=1)
bg_image = PhotoImage(file="tomato.png")
img = canvas.create_image(150,172,image=bg_image)
x = canvas.create_text(150,182,text="00:00",font=(FONT_NAME,20,"bold"),fill="white")
timer_heading = canvas.create_text(150,40,text="TIMER",font=(FONT_NAME,40,"bold"),fill=GREEN)
canvas.grid(row=1,column=1,rowspan = 2, columnspan=1)

start_button = Button(text="Start",highlightthickness=0,bg="white",command=start_countdown)
start_button.grid(row=3,column=0,padx=(30,0),pady=30)

reset_button = Button(text="Reset",highlightthickness=0,bg="white",command=reset)
reset_button.grid(row=3,column=3,padx=(0,30),pady=30)


check_mark = Label(text=text, bg=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()