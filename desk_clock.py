from tkinter import *
import glob
# Change the look of the button
from tkmacosx import Button
# Current Time
import time
# Datetime and Calendar
import calendar
from datetime import datetime
# Random to generate different number
import random


# Main window for application
root = Tk()

# Create class for desktop application


class DeskApp:
    """
    GUI app to initialize calendar(months, days), 
    clock(time), and schedules(keep track what to do during the day)
    """

    def __init__(self, window):
        # Main window
        self.window = window
        # Title of mina window
        self.window.title("Hello, Jorn")
        # Dates
        self.dates = datetime.now()

        # Methods
        self.window_label()
        self.quote()
        self.desk_calendar()
        self.clock()
        self.window_display()

    # functions/methods

    # method that creates labels
    def window_label(self):
        # Current Month
        months = self.dates.strftime("%B")

        # Frame 1
        self.frame1 = LabelFrame(master=self.window, text=f"Good Morning!", width=100,
                                 height=100, bg="orange", padx=50, pady=50)
        self.frame1.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Creates labels
        # Creating a Label to display time in frame1
        self.clock_label = Label(self.frame1, font=(
            "Arial", 30, 'bold'), bg="green", fg="yellow", bd=7, width=12, height=2, relief=SUNKEN)
        self.clock_label.grid(row=1, column=1)

        # Frame 2
        # TODO Add months in f"{}"
        self.frame2 = LabelFrame(master=self.window, text=f"{months}", width=100,
                                 height=100, bg="blue", padx=50, pady=50)
        self.frame2.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def quote(self):
        quotes = {
            "bruce lee": [
                "Knowing is not enough, we must apply. Willing is not enough, we must do.",
                "Showing off is the fool's idea of glory.",
                "As you think, so shall you become.",
                "I fear not the man who has practiced 10,000 kicks once, but I fear the man who has practiced one kick 10,000 times.",
            ]
        }

        random_key = random.choice(list(quotes))
        random_quote = random.choice(quotes[random_key])
        quote_label = Label(master=self.frame1,
                            text=f"{random_quote}", width=100, height=5)
        quote_label.grid(row=0, column=1)
        quote_label.config(text=f"{random_quote}")
        quote_label.after(10000, self.quote)

    # Create a function that shows daily schedule
    def schedule(self):
        """
        Creates window when button is press
        """

        top = Toplevel()
        top.geometry("500x500")
        top.title("Schedule")

        # Schedule through the week
        SCHEDULE = {
            "7:00am": "Wake Up",
            "7:30am": "Program",
            "9:30am": "Read Book",
            "10:00am": "N/A",
            "11:00am": "Workout",
            "12:30pm": "Shower",
            "1:00pm": "Food",
            "2:45pm": "Leave House",
            "4:15pm": "Work",
            "10:30pm": "Bed Time",
        }

        l2 = Label(top, text="Today's Schedule")
        l2.pack()
        for time, task in SCHEDULE.items():
            Label(top, text=f"\n{time}: {task}").pack()

    # function that creates calendar
    def desk_calendar(self):
        # Days & Months
        month = self.dates.strftime("%-m")
        year = self.dates.strftime("%Y")
        week = self.dates.now().weekday
        day_of_the_week = self.dates.strftime("%A")
        day_of_the_month = self.dates.strftime("%-d")
        todays_date = self.dates.strftime("%x")
        my_time = self.dates.strftime("%H:%M:%p")
        calendar_days_in_month = calendar.monthrange(int(year), int(month))
        cal = calendar.monthcalendar(int(year), int(month))
        # Names of the Days
        days = calendar.day_name

        for week in range(len(cal)):
            for day in range(len(days)):
                if day == day:
                    Button(self.frame2, text=f"{days[day]}\n{cal[week][day]}",  # TODO add "command=create_window"
                           borderwidth=1, relief=RAISED, command=self.schedule).grid(row=week, column=day)
                    if days[day] == day_of_the_week and cal[week][day] == int(day_of_the_month):
                        Button(master=self.frame2, text=f"{days[day]}\n{cal[week][day]}",  # TODO add "command=create_window"
                               borderwidth=1, relief=RAISED, bg='green', command=self.schedule).grid(row=week, column=day)

    def clock(self):
        self.text_input = time.strftime("%H:%M:%S %p")
        self.clock_label.config(text=self.text_input)
        self.clock_label.after(200, self.clock)

    # When call, it will display main window
    def window_display(self):
        # Creates main window
        self.window.mainloop()


DeskApp(root)
