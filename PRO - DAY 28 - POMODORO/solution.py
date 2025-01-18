from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
TOTAL_HOURS = 5
TOTAL_MINUTES = TOTAL_HOURS   # 15 hours = 900 minutes

# ---------------------------- VARIABLES ------------------------------- #
reset_pressed = False
cycle_count = 0
text = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    countdown(WORK_MIN, 0)  # Start with the work timer

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(mins, seconds):
    global reset_pressed, cycle_count

    if reset_pressed:
        return  # Stop the timer if reset is pressed

    canvas.itemconfig(timer_text, text=f"{mins:02d}:{seconds:02d}")

    if mins > 0 or seconds > 0:
        if seconds == 0:
            window.after(1000, countdown, mins - 1, 59)  # Decrement minutes
        else:
            window.after(1000, countdown, mins, seconds - 1)  # Decrement seconds
    else:
        # Timer is done, increment cycle count
        cycle_count += 1

        if cycle_count < TOTAL_MINUTES // (WORK_MIN + SHORT_BREAK_MIN):
            if cycle_count % 2 == 0:
                break_timer(SHORT_BREAK_MIN, 0)  # Start break after work cycle
            else:
                countdown(WORK_MIN, 0)  # Start work after break cycle
        else:
            canvas.itemconfig(timer_text, text="Finished!")  # Total 15 hours completed

# ---------------------------- BREAK TIMER ------------------------------- #
def break_timer(mins, seconds):
    global reset_pressed

    if reset_pressed:
        return  # Stop the timer if reset is pressed

    canvas.itemconfig(timer_text, text=f"{mins:02d}:{seconds:02d}")

    if mins > 0 or seconds > 0:
        if seconds == 0:
            window.after(1000, break_timer, mins - 1, 59)  # Decrement minutes
        else:
            window.after(1000, break_timer, mins, seconds - 1)  # Decrement seconds
    else:
        countdown(WORK_MIN, 0)  # Start work after break is done

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reset_pressed, cycle_count, text
    reset_pressed = True
    cycle_count = 0
    text = ""
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text=text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Productivity Timer")
window.config(bg=YELLOW, padx=50, pady=50)

# Canvas for the tomato image and timer text
canvas = Canvas(width=300, height=324, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")  # Make sure the image file is in the correct location
canvas.create_image(150, 172, image=bg_image)
timer_text = canvas.create_text(150, 182, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.create_text(150,40,text="TIMER",font=(FONT_NAME,40,"bold"),fill=GREEN)
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark label for completed cycles
check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()
